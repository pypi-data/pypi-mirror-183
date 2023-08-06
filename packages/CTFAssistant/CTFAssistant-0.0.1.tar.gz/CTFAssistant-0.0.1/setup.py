from setuptools import setup
import io

with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='CTFAssistant',
    version='0.0.1',
    packages=['CTFAssistant'],
    url='https://github.com/Moxin1044/qsnctf-python',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    license='MIT License',
    author='Moxin',
    author_email='1044631097@qq.com',
    description='青少年CTF的Python库模块'
)
