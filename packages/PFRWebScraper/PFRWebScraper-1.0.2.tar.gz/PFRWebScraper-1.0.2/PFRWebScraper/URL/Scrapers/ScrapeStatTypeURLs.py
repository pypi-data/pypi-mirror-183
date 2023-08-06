import os
import sys
from bs4 import Comment

scrapers_directory = os.path.dirname(__file__)
url_directory = os.path.dirname(scrapers_directory)
pfr_directory = os.path.dirname(url_directory)
sys.path.insert(0, pfr_directory)
sys.path.insert(1, url_directory)

from PFRWebScraper.Includes.ScrapeDataAbstract import ScrapeDataAbstract
from PFRWebScraper.URL.StatTypeURLs.StatTypeURLs import StatTypeURLData

class ScrapeStatTypeURLs():
    def __init__(self, logger=None, base_url=None):
        """Initialize

        Args:
            logger (Python Logger): A logger created from the Python Logger Class. Defaults to None.
        """
        self.__base_url = base_url
        self.__stat_type_url_instance = StatTypeURLData(logger=logger)
        
        
    def scrape_urls(self, url, stat_type):
        """Scrapes player's urls from a teams's page

        Args:
            url (string): URL for NFL team from www.pro-football-reference.com
            
        Returns:
            StatTypeURLs: Object with the url, position, and player names stored
        """
        scraper = ScrapeDataAbstract().create_scraper(url)
        
        if (stat_type == 'passing'):
            self.__scrape_passing_stats(scraper)
        elif (stat_type == 'rushing'):
            self.__scrape_rushing_stats(scraper)
        elif (stat_type == 'receiving'):
            self.__scrape_receiving_stats(scraper)
        elif (stat_type == 'kicking'):
            self.__scrape_kicking_stats(scraper)
        elif (stat_type == 'returns'):
            self.__scrape_returning_stats(scraper)
        elif (stat_type == 'scoring'):
            self.__scrape_scoring_stats(scraper)

        
        return self.__stat_type_url_instance
    
    def __scrape_passing_stats(self, scraper):
        """Scrapes all players from the list of passing stats

        Args:
            scraper (BeautifulSoup): Beautifulsoup instance of the team's data page
        """
        for all_passing in scraper.find_all(id="all_passing"):
            for div_passing in all_passing.find_all(id="div_passing"):
                for table in div_passing.find_all("table"):
                    for tbody in table.find_all("tbody"):
                        for tr in tbody.find_all("tr"):
                            self.__stat_type_url_instance.set_stat_type_urls(self.__obtain_player_urls(tr.find_all("td")))
                            
    def __scrape_rushing_stats(self, scraper):
        """Scrapes all players from the list of rushing stats

        Args:
            scraper (BeautifulSoup): Beautifulsoup instance of the team's data page
        """
        for all_rushing in scraper.find_all(id="all_rushing"):
            for div_rushing in all_rushing.find_all(id="div_rushing"):
                for table in div_rushing.find_all("table"):
                    for tbody in table.find_all("tbody"):
                        for tr in tbody.find_all("tr"):
                            self.__stat_type_url_instance.set_stat_type_urls(self.__obtain_player_urls(tr.find_all("td")))
                            
    def __scrape_receiving_stats(self, scraper):
        """Scrapes all players from the list of receiving stats

        Args:
            scraper (BeautifulSoup): Beautifulsoup instance of the team's data page
        """
        for all_receiving in scraper.find_all(id="all_receiving"):
            for div_receiving in all_receiving.find_all(id="div_receiving"):
                for table in div_receiving.find_all("table"):
                    for tbody in table.find_all("tbody"):
                        for tr in tbody.find_all("tr"):
                            self.__stat_type_url_instance.set_stat_type_urls(self.__obtain_player_urls(tr.find_all("td")))
                            
    def __scrape_kicking_stats(self, scraper):
        """Scrapes all players from the list of kicking stats

        Args:
            scraper (BeautifulSoup): Beautifulsoup instance of the team's data page
        """
        for all_kicking in scraper.find_all(id="all_kicking"):
            for div_kicking in all_kicking.find_all(id="div_kicking"):
                for table in div_kicking.find_all("table"):
                    for tbody in table.find_all("tbody"):
                        for tr in tbody.find_all("tr"):
                            self.__stat_type_url_instance.set_stat_type_urls(self.__obtain_player_urls(tr.find_all("td")))
                            
    def __scrape_returning_stats(self, scraper):
        """Scrapes all players from the list of returning stats

        Args:
            scraper (BeautifulSoup): Beautifulsoup instance of the team's data page
        """
        for all_returns in scraper.find_all(id="all_returns"):
            for div_returns in all_returns.find_all(id="div_returns"):
                for table in div_returns.find_all("table"):
                    for tbody in table.find_all("tbody"):
                        for tr in tbody.find_all("tr"):
                            self.__stat_type_url_instance.set_stat_type_urls(self.__obtain_player_urls(tr.find_all("td")))
                            
    def __scrape_scoring_stats(self, scraper):
        """Scrapes all players from the list of scoring stats

        Args:
            scraper (BeautifulSoup): Beautifulsoup instance of the team's data page
        """
        for all_scoring in scraper.find_all(id="all_scoring"):
            for div_scoring in all_scoring.find_all(id="div_scoring"):
                for table in div_scoring.find_all("table"):
                    for tbody in table.find_all("tbody"):
                        for tr in tbody.find_all("tr"):
                            self.__stat_type_url_instance.set_stat_type_urls(self.__obtain_player_urls(tr.find_all("td")))
                                
    def __obtain_player_urls(self, section_data):
        """Method for parsing urls from the tables once the scraper has reached them

        Args:
            section_data (BeautifulSoup): BeautifulSoup Object pointing to the data table

        Returns:
            list: Information relevant to the current table being scraped
        """
        player_url = ""
        player_name = ""
        
        for data in section_data:
            if (data['data-stat'] == 'player'):
                for a in data.find_all("a"):
                    if a.text == "" or a['href'] == "":
                        return None
                    else:
                        player_name = a.text.lower().strip()
                        player_url = self.__base_url + a['href']
                        print([player_name, player_url])
                        return [player_name, player_url]
                
        return None
                    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")