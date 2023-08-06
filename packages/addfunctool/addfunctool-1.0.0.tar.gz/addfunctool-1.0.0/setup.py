from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='addfunctool',
    version='1.0.0',
    description='Add Operator',
    long_description=long_description,
    author='chenweikai',
    author_email='1765026991@qq.com',
    license='BSD License',
    packages=find_packages(),
    platforms=['all'],
)
