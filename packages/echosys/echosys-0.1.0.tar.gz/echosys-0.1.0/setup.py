from setuptools import setup

setup(
    name='echosys',
    version='0.1.0',
    description='A python library for modeling and solving epistemic multi agents planning problems',
    url='https://github.com/DavideSolda/ECHO',
    author='Davide Solda\'',
    author_email='davide.solda@tuwien.ac.at',
    license='GNU General Public License v3.0',
    packages=['ECHO'],
    install_requires=['clingo'],
    classifiers=[]
    )
