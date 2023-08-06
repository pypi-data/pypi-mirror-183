from PFRWebScraper.Includes.MyOpener import MyOpener
from bs4 import BeautifulSoup
import time
import random

class ScrapeDataAbstract():    
    def create_scraper(self, url):
        """Creates the instance for scraping the data

        Args:
            url (string): The url that data will be scraped from

        Returns:
            BeautifulSoup: BeautifulSoup instance for scraping the site
        """
        opener = MyOpener()
        opener.version = opener.create_user_agent()
        
        try:
            with opener.open(url) as request:
                agent_opener = request.read()
                soup = BeautifulSoup(agent_opener, "lxml")
        except ValueError:
            raise ValueError("Wait {0} seconds before trying again.  The server has flagged you for making too many requests.".format(opener.open(url).headers['Retry-After']))
        
        # Sleeps between 5 and 10 seconds per request out of respect for the website owner
        time.sleep(random.uniform(5, 10))
        
        return soup
    
    def scrape_comment(self, comment):
        """Scrapes a comment when the data is dynamically loaded

        Args:
            comment (str): Comment string found within div

        Returns:
            BeautifulSoup: BeautifulSoup instance for scraping the comment
        """
        return BeautifulSoup(comment, 'html.parser')
    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")