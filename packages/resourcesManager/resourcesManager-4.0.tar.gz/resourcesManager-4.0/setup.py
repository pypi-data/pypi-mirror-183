from setuptools import setup

from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='resourcesManager',
    version='4.0',
    license='MIT License',
    author='Luan Soares',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='piitszkdev@outlook.com',
    keywords='fivem',
    description=u'Criação de resources mais rápida',
    packages=['piitszk'],
    install_requires=[],)