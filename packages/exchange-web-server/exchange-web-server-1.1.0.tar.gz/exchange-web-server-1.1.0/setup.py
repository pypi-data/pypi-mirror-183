import os

from setuptools import setup, find_packages
from dotenv import load_dotenv

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
load_dotenv()

NAME = os.environ.get("COMPOSE_PROJECT_NAME")
VERSION = os.environ.get("LATEST_STABLE_VERSION")
DESCRIPTION = 'Send/Save Emails & Attachments via Outlook'
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
    name=NAME,
    version=VERSION,
    author="Valentin Baier",
    author_email="valentin_baier@gmx.de",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['exchangelib'],
    keywords=['python', 'email', 'outlook', 'send', 'send email', 'save', 'save email'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
