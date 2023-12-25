from setuptools import setup, find_packages

with open('requirements.txt','r') as f:
    reqs = f.read()

setup(
    name = 'PyHTTPChat-Client',
    version = '0.0.1',
    packages = find_packages(),
    author = 'EnvIr0n',
    author_email = 'envir0n@proton.me',
    url='https://github.com/Env-Ir0n/PYHTTPCHAT-CLIENT',
    scripts= ['src.pychatclient.py'],
    requires=reqs

)