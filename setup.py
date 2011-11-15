from setuptools import setup, find_packages

setup(
    install_requires=[
        'setuptools',
    ],
    name='collective.js.extjs',
    namespace_packages=[
        'collective',
        'collective.js'
    ],
    version='0.1.0',
    packages=find_packages(),
)
