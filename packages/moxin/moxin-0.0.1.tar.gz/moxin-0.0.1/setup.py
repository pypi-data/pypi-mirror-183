from setuptools import setup
import io

with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='moxin',
    version='0.0.1',
    packages=['moxin'],
    url='',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    license='MIT License',
    author='',
    author_email='',
    description=''
)
