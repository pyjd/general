from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='general',
    version='0.0.1',
    description='A general project to practice python programming',
    long_description=readme,
    author='Javad Alipanah',
    author_email='javadalipanah@gmail.com',
    url='https://github.com/pyjd/general',
    license=license,
    packages=find_packages(exclude=('tests'))
)
