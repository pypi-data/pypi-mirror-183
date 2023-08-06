import logging
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django_registration.forms import RegistrationFormUniqueEmail
from guardian.shortcuts import assign_perm, get_anonymous_user


logger = logging.getLogger(__name__)


User = get_user_model()


if settings.USE_LDAP:
    import ldap
    from ldap import modlist


class UserCreateForm(RegistrationFormUniqueEmail):
    def clean_email(self):
        data = self.cleaned_data["email"].lower()
        if not any([data.endswith(s) for s in ["jh.edu", "jhu.edu", "jhmi.edu"]]) and data not in settings.EMAIL_WHITELIST:
            raise ValidationError("Email address must end with 'jh.edu', 'jhu.edu', or 'jhmi.edu' (or be explicitly permitted by the site administrator)")
        else:
            return data
    def clean_username(self):
        name = self.cleaned_data["username"].lower()
        return name
    class Meta(RegistrationFormUniqueEmail.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name"]
    def save(self, *argv, **argd):
        if settings.USE_LDAP:
            ld = ldap.initialize(settings.AUTH_LDAP_SERVER_URI)
            if settings.AUTH_LDAP_START_TLS == True:
                ld.set_option(ldap.OPT_X_TLS_CACERTFILE, settings.LDAP_CERTFILE)
                ld.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_DEMAND)
                ld.set_option(ldap.OPT_X_TLS_NEWCTX, 0)
                ld.start_tls_s()
                ld.simple_bind_s(settings.AUTH_LDAP_BIND_DN, settings.AUTH_LDAP_BIND_PASSWORD)
            else:
                ld.bind_s(settings.AUTH_LDAP_BIND_DN, settings.AUTH_LDAP_BIND_PASSWORD)
            current_users = {}
            for dn, attrs in ld.search_st(
                    settings.LDAP_USER_BASE,
                    ldap.SCOPE_SUBTREE,
                    filterstr="(!(objectClass=organizationalUnit))"
            ):
                current_users[attrs["uid"][0]] = (dn, attrs)

            bf = {s : bytes(self.cleaned_data[s], "utf-8") for s in ["email", "username", "first_name", "last_name"]}
            home = bytes("/home/{}".format(self.cleaned_data["username"]), "utf-8")
            dn = "uid={},{}".format(self.cleaned_data["username"], settings.LDAP_USER_BASE)
            next_uid_number = max([2000] + [int(x[1]["uidNumber"][0]) for x in current_users.values()]) + 1
            item = {
                "objectClass" : [b"inetOrgPerson", b"posixAccount", b"shadowAccount"],
                "mail" : [bf["email"]],
                "sn" : [bf["last_name"]],
                "givenName" : [bf["first_name"]],
                "uid" : [bf["username"]],
                "cn" : [bf["username"]],
                "uidNumber" : [bytes(str(next_uid_number), "utf-8")],
                "gidNumber" : [b"100"],
                "loginShell" : [b"/bin/bash"],
                "homeDirectory" : [home],
                "gecos" : [bf["username"]],
            }
            ld.add_s(dn, modlist.addModlist(item))
            ld.passwd_s(dn, None, self.data["password1"])
            for gdn in [settings.LDAP_WEB_GROUP_DN, settings.LDAP_WORKSTATION_GROUP_DN]:
                ld.modify_s(
                    gdn,
                    [
                        (ldap.MOD_ADD, 'memberUid', [bf["username"]]),
                    ],
                )

        user = super().save(*argv, **argd)
        user.save()
        assign_perm("ochre.view_user", get_anonymous_user(), user)
        assign_perm("ochre.change_user", user, user)
        
        # this second save seems necessary to prevent populating the password field in SQL?
        user.save()
        return user
