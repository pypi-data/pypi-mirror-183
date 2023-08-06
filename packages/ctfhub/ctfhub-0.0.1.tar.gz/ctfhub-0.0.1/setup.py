from setuptools import setup
import io

with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ctfhub',
    version='0.0.1',
    packages=['ctfhub'],
    url='https://github.com/Moxin1044/ctf-python',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    license='MIT License',
    author='Moxin',
    author_email='1044631097@qq.com',
    description='CTF-Python'
)
