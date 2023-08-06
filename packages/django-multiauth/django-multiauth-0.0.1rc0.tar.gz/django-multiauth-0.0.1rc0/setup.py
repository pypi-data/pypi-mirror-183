import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django-multiauth',
    version='0.0.1.pre',
    packages=['multiauth'],
    description='A django package for allowing your user to manage multiple sources of authentication',
    long_description=README,
    author='Riley Mathews',
    author_email='dev@rileymathews.com',
    url='https://github.com/rileymathews/django-multiauth/',
    license='MIT',
    install_requires=[
        'Django>=4.0',
    ]
)
