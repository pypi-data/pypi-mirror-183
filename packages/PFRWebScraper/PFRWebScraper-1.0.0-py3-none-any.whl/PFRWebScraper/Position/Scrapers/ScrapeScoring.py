import os
import sys

scrapers_directory = os.path.dirname(__file__)
position_directory = os.path.dirname(scrapers_directory)
pfr_directory = os.path.dirname(position_directory)
sys.path.insert(0, pfr_directory)
sys.path.insert(1, position_directory)

from PFRWebScraper.Includes.ScrapeDataAbstract import ScrapeDataAbstract
from PFRWebScraper.Position.Scoring.Scoring import ScoringData

class ScrapeScoring():
    
    def __init__(self, logger=None):
        """Initialize

        Args:
            logger (Python Logger): A logger created from the Python Logger Class. Defaults to None.
        """
        self.__scoring_data_instance = ScoringData(logger=logger)
        
    def scrape_data(self, url):
        """Scrapes scoring data from a player's page

        Args:
            url (string): URL for NFL player from www.pro-football-reference.com
        """
        scraper = ScrapeDataAbstract().create_scraper(url)
        
        self.__scrape_scoring_data(scraper)
        
        return self.__scoring_data_instance
    
    def __scrape_scoring_data(self, scraper):
        """Method for scraping scoring data
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        next_tag = ""
        
        for all_scoring in scraper.find_all(id="all_scoring"):
            if(all_scoring.find_all(id="switcher_scoring")):
                next_tag = all_scoring.find_all(id="switcher_scoring")[0]
            else:
                next_tag = all_scoring
            
            self.__scoring_regular_season(next_tag)
            self.__scoring_playoffs(next_tag)
            
    def __scoring_regular_season(self, scraper):
        """Method for scraping scoring for regular season
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        for identifier in scraper.find_all(id="div_scoring"):
            for table in identifier.find_all("table"):
                for tbody in table.find_all("tbody"):
                    for tr in tbody.find_all("tr"):
                        for th in tr.find_all("th"):
                            for a in th.find_all("a"):
                                current_year = int(a.text)
                        self.__scoring_data_instance.set_scoring_data_regular_season(self.__obtain_scoring_data(current_year, tr.find_all("td")))

    def __scoring_playoffs(self, scraper):
        """Method for scraping scoring data for playoffs
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        for identifier in scraper.find_all(id="div_scoring_playoffs"):
            for table in identifier.find_all("table"):
                for tbody in table.find_all("tbody"):
                    for tr in tbody.find_all("tr"):
                        for th in tr.find_all("th"):
                            for a in th.find_all("a"):
                                current_year = int(a.text)
                        self.__scoring_data_instance.set_scoring_data_playoffs(self.__obtain_scoring_data(current_year, tr.find_all("td")))

    
    def __obtain_scoring_data(self, year, section_data):
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
            elif (stat['data-stat'] == 'rushtd'):
                if stat.text == "":
                    stats['rushtd'] = [0]
                else:
                    stats['rushtd'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rectd'):
                if stat.text == "":
                    stats['rectd'] = [0]
                else:
                    stats['rectd'] = [int(stat.text)]
            elif (stat['data-stat'] == 'prtd'):
                if stat.text == "":
                    stats['prtd'] = [0]
                else:
                    stats['prtd'] = [int(stat.text)]
            elif (stat['data-stat'] == 'krtd'):
                if stat.text == "":
                    stats['krtd'] = [0]
                else:
                    stats['krtd'] = [int(stat.text)]
            elif (stat['data-stat'] == 'frtd'):
                if stat.text == "":
                    stats['frtd'] = [0]
                else:
                    stats['frtd'] = [int(stat.text)]
            elif (stat['data-stat'] == 'ditd'):
                if stat.text == "":
                    stats['ditd'] = [0]
                else:
                    stats['ditd'] = [int(stat.text)]
            elif (stat['data-stat'] == 'otd'):
                if stat.text == "":
                    stats['otd'] = [0]
                else:
                    stats['otd'] = [int(stat.text)]
            elif (stat['data-stat'] == 'alltd'):
                if stat.text == "":
                    stats['alltd'] = [0]
                else:
                    stats['alltd'] = [int(stat.text)]
            elif (stat['data-stat'] == 'two_pt_md'):
                if stat.text == "":
                    stats['two_pt_md'] = [0]
                else:
                    stats['two_pt_md'] = [int(stat.text)]
            elif (stat['data-stat'] == 'two_pt_att'):
                if stat.text == "":
                    stats['two_pt_att'] = [0]
                else:
                    stats['two_pt_att'] = [int(stat.text)]
            elif (stat['data-stat'] == 'def_two_pt'):
                if stat.text == "":
                    stats['def_two_pt'] = [0]
                else:
                    stats['def_two_pt'] = [int(stat.text)]
            elif (stat['data-stat'] == 'xpm'):
                if stat.text == "":
                    stats['xpm'] = [0]
                else:
                    stats['xpm'] = [int(stat.text)]
            elif (stat['data-stat'] == 'xpa'):
                if stat.text == "":
                    stats['xpa'] = [0]
                else:
                    stats['xpa'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fgm'):
                if stat.text == "":
                    stats['fgm'] = [0]
                else:
                    stats['fgm'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fga'):
                if stat.text == "":
                    stats['fga'] = [0]
                else:
                    stats['fga'] = [int(stat.text)]
            elif (stat['data-stat'] == 'safety_md'):
                if stat.text == "":
                    stats['safety_md'] = [0]
                else:
                    stats['safety_md'] = [int(stat.text)]
            elif (stat['data-stat'] == 'scoring'):
                if stat.text == "":
                    stats['scoring'] = [0]
                else:
                    stats['scoring'] = [int(stat.text)]
            elif (stat['data-stat'] == 'points_per_g'):
                if stat.text == "":
                    stats['points_per_g'] = [0.0]
                else:
                    stats['points_per_g'] = [float(stat.text)]
        return stats
    
    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")
    