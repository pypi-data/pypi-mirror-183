from setuptools import setup
import io

with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ChinaIDCard',
    version='0.0.1',
    packages=['ChinaIDCard'],
    url='https://github.com/Moxin1044/eShenfenKu',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT License',
    author='Moxin',
    author_email='Moxin1044@gmail.com',
    description='中国身份证效验'
)
