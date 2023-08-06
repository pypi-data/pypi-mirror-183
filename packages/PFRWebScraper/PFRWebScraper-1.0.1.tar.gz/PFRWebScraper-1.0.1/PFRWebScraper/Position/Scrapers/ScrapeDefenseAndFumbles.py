import os
import sys

scrapers_directory = os.path.dirname(__file__)
position_directory = os.path.dirname(scrapers_directory)
pfr_directory = os.path.dirname(position_directory)
sys.path.insert(0, pfr_directory)
sys.path.insert(1, position_directory)

from PFRWebScraper.Includes.ScrapeDataAbstract import ScrapeDataAbstract
from PFRWebScraper.Position.DefenseAndFumbles.DefenseAndFumbles import DefenseAndFumblesData

class ScrapeDefenseAndFumbles():
    
    def __init__(self, logger=None):
        """Initialize

        Args:
            logger (Python Logger): A logger created from the Python Logger Class. Defaults to None.
        """
        self.__defense_and_fumbles_data_instance = DefenseAndFumblesData(logger=logger)
        
    def scrape_data(self, url):
        """Scrapes defense and fumbles data from a player's page

        Args:
            url (string): URL for NFL player from www.pro-football-reference.com
        """
        scraper = ScrapeDataAbstract().create_scraper(url)
        
        self.__scrape_defense_and_fumbles_data(scraper)
        
        return self.__defense_and_fumbles_data_instance
    
    def __scrape_defense_and_fumbles_data(self, scraper):
        """Method for scraping defense and fumbles data
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        next_tag = ""
        
        for all_defense in scraper.find_all(id="all_defense"):
            if(all_defense.find_all(id="switcher_defense")):
                next_tag = all_defense.find_all(id="switcher_defense")[0]
            else:
                next_tag = all_defense
            
            self.__defense_and_fumbles_regular_season(next_tag)
            self.__defense_and_fumbles_playoffs(next_tag)
            
    def __defense_and_fumbles_regular_season(self, scraper):
        """Method for scraping defense and fumbles for regular season
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        for identifier in scraper.find_all(id="div_defense"):
            for table in identifier.find_all("table"):
                for tbody in table.find_all("tbody"):
                    for tr in tbody.find_all("tr"):
                        for th in tr.find_all("th"):
                            for a in th.find_all("a"):
                                current_year = int(a.text)
                        self.__defense_and_fumbles_data_instance.set_defense_and_fumbles_data_regular_season(self.__obtain_defense_and_fumbles_data(current_year, tr.find_all("td")))

    def __defense_and_fumbles_playoffs(self, scraper):
        """Method for scraping defense and fumbles data for playoffs
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        for identifier in scraper.find_all(id="div_defense_playoffs"):
            for table in identifier.find_all("table"):
                for tbody in table.find_all("tbody"):
                    for tr in tbody.find_all("tr"):
                        for th in tr.find_all("th"):
                            for a in th.find_all("a"):
                                current_year = int(a.text)
                        self.__defense_and_fumbles_data_instance.set_defense_and_fumbles_data_playoffs(self.__obtain_defense_and_fumbles_data(current_year, tr.find_all("td")))

    
    def __obtain_defense_and_fumbles_data(self, year, section_data):
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
            elif (stat['data-stat'] == 'def_int'):
                if stat.text == "":
                    stats['def_int'] = [0]
                else:
                    stats['def_int'] = [int(stat.text)]
            elif (stat['data-stat'] == 'def_int_yds'):
                if stat.text == "":
                    stats['def_int_yds'] = [0]
                else:
                    stats['def_int_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'def_int_td'):
                if stat.text == "":
                    stats['def_int_td'] = [0]
                else:
                    stats['def_int_td'] = [int(stat.text)]
            elif (stat['data-stat'] == 'def_int_long'):
                if stat.text == "":
                    stats['def_int_long'] = [0]
                else:
                    stats['def_int_long'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_defended'):
                if stat.text == "":
                    stats['pass_defended'] = [0]
                else:
                    stats['pass_defended'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fumbles_forced'):
                if stat.text == "":
                    stats['fumbles_forced'] = [0]
                else:
                    stats['fumbles_forced'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fumbles'):
                if stat.text == "":
                    stats['fumbles'] = [0]
                else:
                    stats['fumbles'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fumbles_rec'):
                if stat.text == "":
                    stats['fumbles_rec'] = [0]
                else:
                    stats['fumbles_rec'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fumbles_rec_yds'):
                if stat.text == "":
                    stats['fumbles_rec_yds'] = [0]
                else:
                    stats['fumbles_rec_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fumbles_rec_td'):
                if stat.text == "":
                    stats['fumbles_rec_td'] = [0]
                else:
                    stats['fumbles_rec_td'] = [int(stat.text)]
            elif (stat['data-stat'] == 'sacks'):
                if stat.text == "":
                    stats['sacks'] = [0.0]
                else:
                    stats['sacks'] = [float(stat.text)]
            elif (stat['data-stat'] == 'tackles_combined'):
                if stat.text == "":
                    stats['tackles_combined'] = [0]
                else:
                    stats['tackles_combined'] = [int(stat.text)]
            elif (stat['data-stat'] == 'tackles_solo'):
                if stat.text == "":
                    stats['tackles_solo'] = [0]
                else:
                    stats['tackles_solo'] = [int(stat.text)]
            elif (stat['data-stat'] == 'tackles_assists'):
                if stat.text == "":
                    stats['tackles_assists'] = [0]
                else:
                    stats['tackles_assists'] = [int(stat.text)]
            elif (stat['data-stat'] == 'tackles_loss'):
                if stat.text == "":
                    stats['tackles_loss'] = [0]
                else:
                    stats['tackles_loss'] = [int(stat.text)]
            elif (stat['data-stat'] == 'qb_hits'):
                if stat.text == "":
                    stats['qb_hits'] = [0]
                else:
                    stats['qb_hits'] = [int(stat.text)]
            elif (stat['data-stat'] == 'safety_md'):
                if stat.text == "":
                    stats['safety_md'] = [0]
                else:
                    stats['safety_md'] = [int(stat.text)]
            elif (stat['data-stat'] == 'av'):
                if stat.text == "":
                    stats['approximate_value'] = [0]
                else:
                    stats['approximate_value'] = [int(stat.text)]

        return stats
    
    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")