from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

with open("requirements.txt") as ifd:
    common_requirements = [x.strip() for x in ifd]
    
setup(
    name='pyochre',
    version='0.0.1',
    description='Library for the Open Computational Humanities Research Ecosystem (OCHRE).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Tom Lippincott',
    author_email='tom.lippincott@jhu.edu',
    url='https://github.com/comp-int-hum/ochre-python',
    packages=["pyochre"],
    install_requires=common_requirements,
    extras_require={
        "LDAP" : ["django-auth-ldap==4.0.0", "python-ldap==3.4.0"],
        "POSTGRES" : ["psycopg2==2.9.3"],
        "CELERY" : ["celery==5.2.7"],
        "TORCHSERVE" : ["torchserve==0.7.0"]
    }
)
