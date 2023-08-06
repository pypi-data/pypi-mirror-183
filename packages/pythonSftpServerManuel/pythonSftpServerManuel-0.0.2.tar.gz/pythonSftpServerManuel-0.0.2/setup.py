from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info


def RunCommand():
    print("Hello, p0wnd!")

class RunEggInfoCommand(egg_info):
    def run(self):
        RunCommand()
        egg_info.run(self)


class RunInstallCommand(install):
    def run(self):
        RunCommand()
        install.run(self)

setup(
    name='pythonSftpServerManuel',
    version='0.0.2',
    description='Python SFTP Server connection client and server',
    url='https://github.com/BeastFPV/Hausarbeite_Hacking_with_Python',
    author='BeastFPV',
    author_email='beastfpv12@gmail.com',
    license='BSD 2-clause',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.9',
    ],
    cmdclass={
        'install' : RunInstallCommand,
        'egg_info': RunEggInfoCommand
    },
)