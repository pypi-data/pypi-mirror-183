from setuptools import setup, find_packages

setup(
    name='echosys',
    version='0.1.6',
    description='A python library for modeling and solving epistemic multi agents planning problems',
    url='https://github.com/DavideSolda/ECHO',
    author='Davide Solda\'',
    author_email='davide.solda@tuwien.ac.at',
    license='GNU General Public License v3.0',
    packages=['ECHO'],
    install_requires=['clingo'],
    classifiers=[]
    )
