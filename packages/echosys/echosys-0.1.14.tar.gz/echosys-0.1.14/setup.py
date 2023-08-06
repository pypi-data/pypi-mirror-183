from setuptools import setup, find_packages

with open("ECHO/README.org", "r") as ldf:
    long_description = ldf.read()

print(find_packages())

setup(
    name='echosys',
    version='0.1.14',
    description='A python library for modeling and solving epistemic multi agents planning problems',
    long_description = long_description,
    long_description_content_type = '',
    url='https://github.com/DavideSolda/echosys',
    author='Davide Solda\'',
    author_email='davide.solda@tuwien.ac.at',
    license='GNU General Public License v3.0',
    packages=find_packages(),
    install_requires=['clingo'],
    classifiers=[]
    )
