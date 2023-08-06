import pypandoc
from setuptools import setup

with open('README.md', 'r') as f:
    readme = f.read()

long_description = pypandoc.convert_text(readme, 'rst', format='md')

setup(
    name='a8logging',
    version='1.0.1',
    description='A utility for logging events in Python projects',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/devdp/python-logging.git',
    author='Bramhesh Kumar Srivastava',
    author_email='brahmesh1996@gmail.com',
    license='MIT',
    packages=['a8logging'],
    install_requires=['logging', 'traceback', 'uuid', 'elasticsearch'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)