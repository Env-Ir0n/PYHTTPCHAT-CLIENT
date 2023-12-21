from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = 'pyhttpchat-client',
    version = 'ALPHA 0.1',
    packages = find_packages(),
    install_requires = requirements,
    author = 'EnvIr0n',
    author_email = 'envir0n@proton.me',
    url='https://github.com/Env-Ir0n/PYHTTPCHAT-CLIENT.git',
    


)