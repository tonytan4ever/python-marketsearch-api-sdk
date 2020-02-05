from setuptools import setup
setup(
    name='python-marketcheck-api',
    version='0.0.1',
    description='My custom package tested with tox',
    long_description='A long description of my custom package tested with tox',
    install_requires=[
        'requests>=2.20.0',
        'marshmallow==3.3.0',
        'flake8==3.7.9'
    ],
    classifiers=[
        'Programming Language :: Python',
    ],
)
