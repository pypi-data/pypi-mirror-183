import pathlib
from setuptools import find_packages, setup

Here = pathlib.Path(__file__).parent

README = (Here / "README.md").read_text()

setup(
    name='a8mailer',
    version='0.1',
    description='A package for sending emails using Outlook and SMTP',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/devdp/python-mailer.git',
    author='Bramhesh Kumar Srivastava',
    author_email='brahmesh1996@gmail.com',
    license='MIT',
    packages=['a8mailer'],
    install_requires=['smtplib', 'email'],
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)