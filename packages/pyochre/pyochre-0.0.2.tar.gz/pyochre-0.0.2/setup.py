from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='pyochre',
    version='0.0.2',
    description='Library for the Open Computational Humanities Research Ecosystem (OCHRE).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Tom Lippincott',
    author_email='tom.lippincott@jhu.edu',
    url='https://github.com/comp-int-hum/ochre-python',
    packages=["pyochre"],
    install_requires=[
        "captum",
        "django",
        "djangorestframework",
        "django-cors-headers",
        "django-debug-toolbar",
        "django-environ",
        "django-extensions",
        "django-guardian",
        "django-mptt",
        "django-registration",
        "django-sekizai",
        "drf-nested-routers",
        "gensim",
        "jsonpath-python",
        "pairtree",
        "python-dotenv",
        "rdflib",
        "requests",
        "rest-framework-nested",
        "spacy",
        "torch",
        "torchvision",
        "torch-model-archiver",
        "transformers",
        "wiki",
        "wikidata",
    ],
    extras_require={
        "LDAP" : [
            "django-auth-ldap",
            "python-ldap"
        ],
        "POSTGRES" : [
            "psycopg2"
        ],
        "CELERY" : [
            "celery"
        ],
        "TORCHSERVE" : [
            "torchserve"
        ]
    }
)
