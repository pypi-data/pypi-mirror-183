from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Scrapes statistics from https://www.pro-football-reference.com/'
LONG_DESCRIPTION = 'A package that allows the user to scrape stats for a team, specific player, and also scrape URLs for players from a stat type.'

# Setting up
setup(
    name="PFRWebScraper",
    version=VERSION,
    author="Devon Connors",
    author_email="<dconns1@outlook.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'beautifulsoup4', 'random_user_agent'],
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