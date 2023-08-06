from setuptools import setup
import io

with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pythonfofa',
    version='1.0.6',
    packages=['pythonfofa'],
    url='https://github.com/Moxin1044/pythonfofa',
    license='MIT License',
    author='Moxin',
    author_email='1044631097@qq.com',
    description='FOFA.info Python SDK'
)
