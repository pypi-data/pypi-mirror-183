import os
import sys
from bs4 import Comment

scrapers_directory = os.path.dirname(__file__)
url_directory = os.path.dirname(scrapers_directory)
pfr_directory = os.path.dirname(url_directory)
sys.path.insert(0, pfr_directory)
sys.path.insert(1, url_directory)

from PFRWebScraper.Includes.ScrapeDataAbstract import ScrapeDataAbstract
from PFRWebScraper.URL.TeamURLs.TeamURLs import TeamURLData

class ScrapeTeamURLs():
    def __init__(self, logger=None, base_url=None):
        """Initialize

        Args:
            logger (Python Logger): A logger created from the Python Logger Class. Defaults to None.
        """
        self.__base_url = base_url
        self.__team_url_instance = TeamURLData(logger=logger)
        
        
    def scrape_urls(self, url):
        """Scrapes player's urls from a teams's page

        Args:
            url (string): URL for NFL team from www.pro-football-reference.com
            
        Returns:
            TeamURLData: Object with the url, position, and player names stored
        """
        scraper = ScrapeDataAbstract().create_scraper(url)
        
        self.__scrape_team_passing_url(scraper)
        self.__scrape_team_rushing_and_receiving_url(scraper)
        self.__scrape_team_kicking_url(scraper)
        
        return self.__team_url_instance
    
    def __scrape_team_passing_url(self, scraper):
        """Scrapes all players with the position 'QB' with passing data on the team data page

        Args:
            scraper (BeautifulSoup): Beautifulsoup instance of the team's data page
        """
        for all_passing in scraper.find_all(id="all_passing"):
            # Scrapes the comment and then loads the HTML into a parser 
            #   to continue scraping information
            for comment in all_passing.find_all(text=lambda text:isinstance(text, Comment)):
                comment_soup = ScrapeDataAbstract().scrape_comment(comment)
                for div_passing in comment_soup.find_all(id="div_passing"):
                    for table in div_passing.find_all("table"):
                        for tbody in table.find_all("tbody"):
                            for tr in tbody.find_all("tr"):
                                self.__team_url_instance.set_team_urls(self.__obtain_player_urls(tr.find_all("td"), ["QB"]))
                                
    def __scrape_team_rushing_and_receiving_url(self, scraper):
        """Scrapes all players with the position 'RB', 'WR', 'TE', 'FB' with rushing and/or receiving data on the team data page

        Args:
            scraper (BeautifulSoup): Beautifulsoup instance of the team's data page
        """
        for all_rushing_and_receiving in scraper.find_all(id="all_rushing_and_receiving"):
            # Scrapes the comment and then loads the HTML into a parser 
            #   to continue scraping information
            for comment in all_rushing_and_receiving.find_all(text=lambda text:isinstance(text, Comment)):
                comment_soup = ScrapeDataAbstract().scrape_comment(comment)
                for div_rushing_and_receiving in comment_soup.find_all(id="div_rushing_and_receiving"):
                    for table in div_rushing_and_receiving.find_all("table"):
                        for tbody in table.find_all("tbody"):
                            for tr in tbody.find_all("tr"):
                                self.__team_url_instance.set_team_urls(self.__obtain_player_urls(tr.find_all("td"), ["RB", "WR", "TE", "FB"]))
    
    def __scrape_team_kicking_url(self, scraper):
        """Scrapes all players with the position 'K' with kicking data on the team data page

        Args:
            scraper (BeautifulSoup): Beautifulsoup instance of the team's data page
        """
        for all_kicking in scraper.find_all(id="all_kicking"):
            # Scrapes the comment and then loads the HTML into a parser 
            #   to continue scraping information
            for comment in all_kicking.find_all(text=lambda text:isinstance(text, Comment)):
                comment_soup = ScrapeDataAbstract().scrape_comment(comment)
                for div_kicking in comment_soup.find_all(id="div_kicking"):
                    for table in div_kicking.find_all("table"):
                        for tbody in table.find_all("tbody"):
                            for tr in tbody.find_all("tr"):
                                self.__team_url_instance.set_team_urls(self.__obtain_player_urls(tr.find_all("td"), ["K"]))
                                
    def __obtain_player_urls(self, section_data, position):
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
            if (data['data-stat'] == 'pos' and data.text in position):
                return [player_name, player_url, data.text.strip()]
                
        return None
                    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")