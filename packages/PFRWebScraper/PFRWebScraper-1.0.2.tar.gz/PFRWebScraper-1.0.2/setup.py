from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

VERSION = '1.0.2'
DESCRIPTION = 'Scrapes statistics from https://www.pro-football-reference.com/'

# Setting up
setup(
    name="PFRWebScraper",
    version=VERSION,
    author="Devon Connors",
    author_email="<dconns1@outlook.com>",
    license="MIT",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(exclude=('tests*', 'testing*', '*__pycache__*')),
    include_package_data=True,
    install_requires=['pandas', 'beautifulsoup4', 'random_user_agent', 'lxml'],
    keywords=['python', 'pro-football-reference', 'football', 'fantasy football', 'american football', 'pro football reference', 'web scraper', 'scraper'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)