import os
import sys

scrapers_directory = os.path.dirname(__file__)
position_directory = os.path.dirname(scrapers_directory)
pfr_directory = os.path.dirname(position_directory)
sys.path.insert(0, pfr_directory)
sys.path.insert(1, position_directory)

from PFRWebScraper.Includes.ScrapeDataAbstract import ScrapeDataAbstract
from PFRWebScraper.Position.SnapCounts.SnapCounts import SnapCountsData

class ScrapeSnapCounts():
    
    def __init__(self, logger=None):
        """Initialize

        Args:
            logger (Python Logger): A logger created from the Python Logger Class. Defaults to None.
        """
        self.__snap_counts_data_instance = SnapCountsData(logger=logger)
        
    def scrape_data(self, url):
        """Scrapes Snap Count data from a player's page

        Args:
            url (string): URL for NFL player from www.pro-football-reference.com
        """
        scraper = ScrapeDataAbstract().create_scraper(url)
        
        self.__scrape_snap_counts_data(scraper)
        
        return self.__snap_counts_data_instance
    
    def __scrape_snap_counts_data(self, scraper):
        """Method for scraping snap counts data
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        next_tag = ""
        
        for all_snap_counts in scraper.find_all(id="all_snap_counts"):
            if(all_snap_counts.find_all(id="switcher_snap_counts")):
                next_tag = all_snap_counts.find_all(id="switcher_snap_counts")[0]
            else:
                next_tag = all_snap_counts
            
            self.__snap_counts_regular_season(next_tag)
            
    def __snap_counts_regular_season(self, scraper):
        """Method for scraping snap counts for regular season
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        for identifier in scraper.find_all(id="div_snap_counts"):
            for table in identifier.find_all("table"):
                for tbody in table.find_all("tbody"):
                    for tr in tbody.find_all("tr"):
                        for th in tr.find_all("th"):
                            for a in th.find_all("a"):
                                current_year = int(a.text)
                        self.__snap_counts_data_instance.set_snap_counts_regular_season(self.__obtain_snap_counts_data(current_year, tr.find_all("td")))
                        
    def __obtain_snap_counts_data(self, year, section_data):
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
            elif (stat['data-stat'] == 'offense'):
                if stat.text == "":
                    stats['offense'] = [0]
                else:
                    stats['offense'] = [int(stat.text)]
            elif (stat['data-stat'] == 'off_pct'):
                if stat.text == "":
                    stats['off_pct'] = [0.0]
                else:
                    stats['off_pct'] = [float(stat.text.replace("%", ""))]
            elif (stat['data-stat'] == 'defense'):
                if stat.text == "":
                    stats['defense'] = [0]
                else:
                    stats['defense'] = [int(stat.text)]
            elif (stat['data-stat'] == 'def_pct'):
                if stat.text == "":
                    stats['def_pct'] = [0.0]
                else:
                    stats['def_pct'] = [float(stat.text.replace("%", ""))]
            elif (stat['data-stat'] == 'special_teams'):
                if stat.text == "":
                    stats['special_teams'] = [0]
                else:
                    stats['special_teams'] = [int(stat.text)]
            elif (stat['data-stat'] == 'st_pct'):
                if stat.text == "":
                    stats['st_pct'] = [0.0]
                else:
                    stats['st_pct'] = [float(stat.text.replace("%", ""))]
        
        return stats
    
    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")

