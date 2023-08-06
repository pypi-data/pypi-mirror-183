from setuptools import setup

setup(
    name='a8logging',
    version='1.0.0',
    description='A utility for logging events in Python projects',
    long_description='A utility for logging events in Python projects with multiple output options such as logging to a file or pushing the logs to Elasticsearch',
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