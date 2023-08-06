import os
import sys

scrapers_directory = os.path.dirname(__file__)
position_directory = os.path.dirname(scrapers_directory)
pfr_directory = os.path.dirname(position_directory)
sys.path.insert(0, pfr_directory)
sys.path.insert(1, position_directory)

from PFRWebScraper.Includes.ScrapeDataAbstract import ScrapeDataAbstract
from PFRWebScraper.Position.Returns.Returns import ReturnsData

class ScrapeReturns():
    
    def __init__(self, logger=None):
        """Initialize

        Args:
            logger (Python Logger): A logger created from the Python Logger Class. Defaults to None.
        """
        self.__returns_data_instance = ReturnsData(logger=logger)
        
    def scrape_data(self, url):
        """Scrapes kick and punt return data from a player's page

        Args:
            url (string): URL for NFL player from www.pro-football-reference.com
        """
        scraper = ScrapeDataAbstract().create_scraper(url)
        
        self.__scrape_returns_data(scraper)
        
        return self.__returns_data_instance
    
    def __scrape_returns_data(self, scraper):
        """Method for scraping scoring data
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        next_tag = ""
        
        for all_returns in scraper.find_all(id="all_returns"):
            if(all_returns.find_all(id="switcher_returns")):
                next_tag = all_returns.find_all(id="switcher_returns")[0]
            else:
                next_tag = all_returns
            
            self.__returns_regular_season(next_tag)
            self.__returns_playoffs(next_tag)
            
    def __returns_regular_season(self, scraper):
        """Method for scraping kick and punt returns for regular season
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        for identifier in scraper.find_all(id="div_returns"):
            for table in identifier.find_all("table"):
                for tbody in table.find_all("tbody"):
                    for tr in tbody.find_all("tr"):
                        for th in tr.find_all("th"):
                            for a in th.find_all("a"):
                                current_year = int(a.text)
                        self.__returns_data_instance.set_returns_data_regular_season(self.__obtain_return_data(current_year, tr.find_all("td")))

    def __returns_playoffs(self, scraper):
        """Method for scraping kick and punt returns data for playoffs
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        for identifier in scraper.find_all(id="div_returns_playoffs"):
            for table in identifier.find_all("table"):
                for tbody in table.find_all("tbody"):
                    for tr in tbody.find_all("tr"):
                        for th in tr.find_all("th"):
                            for a in th.find_all("a"):
                                current_year = int(a.text)
                        self.__returns_data_instance.set_returns_data_playoffs(self.__obtain_return_data(current_year, tr.find_all("td")))

    
    def __obtain_return_data(self, year, section_data):
        """Method for parsing data from the tables once the scraper has reached them

        Args:
            year (int): Current year being scraped
            section_data (BeautifulSoup): BeautifulSoup Object pointing to the data table

        Returns:
            dict: Information relevant to the current table being scraped
        """
        stats = dict()
        
        stats['year'] = [year]
        
        for stat in section_data:
            if (stat['data-stat'] == 'age'):
                if stat.text == "":
                    stats['age'] = [0]
                else:
                    stats['age'] = [int(stat.text)]
            elif (stat['data-stat'] == 'team'):
                if stat.text == "":
                    stats['team_abbreviation'] = ""
                else:
                    for a in stat.find_all("a"):
                        stats['team_abbreviation'] = [str(a.text).lower()]
            elif (stat['data-stat'] == 'pos'):
                if stat.text == "":
                    stats['position'] = ""
                else:
                    stats['position'] = [str(stat.text).lower()]
            elif (stat['data-stat'] == 'uniform_number'):
                if stat.text == "":
                    stats['uniform_number'] = [0]
                else:
                    stats['uniform_number'] = [int(stat.text)]
            elif (stat['data-stat'] == 'g'):
                if stat.text == "":
                    stats['games_played'] = [0]
                else:
                    stats['games_played'] = [int(stat.text)]
            elif (stat['data-stat'] == 'gs'):
                if stat.text == "":
                    stats['games_started'] = [0]
                else:
                    stats['games_started'] = [int(stat.text)]
            elif (stat['data-stat'] == 'punt_ret'):
                if stat.text == "":
                    stats['punt_ret'] = [0]
                else:
                    stats['punt_ret'] = [int(stat.text)]
            elif (stat['data-stat'] == 'punt_ret_yds'):
                if stat.text == "":
                    stats['punt_ret_yds'] = [0]
                else:
                    stats['punt_ret_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'punt_ret_td'):
                if stat.text == "":
                    stats['punt_ret_td'] = [0]
                else:
                    stats['punt_ret_td'] = [int(stat.text)]
            elif (stat['data-stat'] == 'punt_ret_long'):
                if stat.text == "":
                    stats['punt_ret_long'] = [0]
                else:
                    stats['punt_ret_long'] = [int(stat.text)]
            elif (stat['data-stat'] == 'punt_ret_yds_per_ret'):
                if stat.text == "":
                    stats['punt_ret_yds_per_ret'] = [0.0]
                else:
                    stats['punt_ret_yds_per_ret'] = [float(stat.text)]
            elif (stat['data-stat'] == 'kick_ret'):
                if stat.text == "":
                    stats['kick_ret'] = [0]
                else:
                    stats['kick_ret'] = [int(stat.text)]
            elif (stat['data-stat'] == 'kick_ret_yds'):
                if stat.text == "":
                    stats['kick_ret_yds'] = [0]
                else:
                    stats['kick_ret_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'kick_ret_td'):
                if stat.text == "":
                    stats['kick_ret_td'] = [0]
                else:
                    stats['kick_ret_td'] = [int(stat.text)]
            elif (stat['data-stat'] == 'kick_ret_long'):
                if stat.text == "":
                    stats['kick_ret_long'] = [0]
                else:
                    stats['kick_ret_long'] = [int(stat.text)]
            elif (stat['data-stat'] == 'kick_ret_yds_per_ret'):
                if stat.text == "":
                    stats['kick_ret_yds_per_ret'] = [0.0]
                else:
                    stats['kick_ret_yds_per_ret'] = [float(stat.text)]
            elif (stat['data-stat'] == 'all_purpose_yds'):
                if stat.text == "":
                    stats['all_purpose_yds'] = [0]
                else:
                    stats['all_purpose_yds'] = [int(stat.text)]
                    
        return stats
    
    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")