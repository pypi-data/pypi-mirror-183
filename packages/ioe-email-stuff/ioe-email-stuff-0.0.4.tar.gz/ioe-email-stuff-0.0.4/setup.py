from setuptools import setup

VERSION = '0.0.4'
DESCRIPTION = 'Email sending functionality package'
LONG_DESCRIPTION = 'A package that allows to send emails via a number of different methods from within a python application.'

with open("README.md", "r") as fh:
    long_description = fh.read()

# Setting up
setup(
    name="ioe-email-stuff",
    url="https://github.com/george-oconnor/ioe-email-stuff",
    version=VERSION,
    author="george-oconnor (George O' Connor)",
    author_email="<george@georgestools.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["ioe_email_stuff"],
    package_dir={'': 'src'},
    install_requires=['pywin32>=305'],
    keywords=['python', 'email', 'outlook', 'send email', 'email attachments', 'mail'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License"
    ]
)