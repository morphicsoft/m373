from os import path

from pip.req import parse_requirements
from setuptools import setup, find_packages

install_reqs = parse_requirements('requirements.txt', session='none')

here = path.abspath(path.dirname(__file__))

version = '0.0.1.dev0'

setup(
    name='m373',

    version=version,

    description='OU M373 Solutions',

    # The project's main homepage.
    url='https://github.com/morphicsoft/m373',

    # Author details
    author='Jon Bills',
    author_email='jon@morphicsoftware.co.uk',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6'
    ],

    # What does your project relate to?
    keywords=['Open University', 'M373', 'Optimization'],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[str(ir.req) for ir in install_reqs],
    zip_safe=False
)
