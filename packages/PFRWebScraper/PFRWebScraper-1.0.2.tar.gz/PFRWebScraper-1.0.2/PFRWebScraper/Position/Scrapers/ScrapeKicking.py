import os
import sys

scrapers_directory = os.path.dirname(__file__)
position_directory = os.path.dirname(scrapers_directory)
pfr_directory = os.path.dirname(position_directory)
sys.path.insert(0, pfr_directory)
sys.path.insert(1, position_directory)

from PFRWebScraper.Includes.ScrapeDataAbstract import ScrapeDataAbstract
from PFRWebScraper.Position.Kicking.Kicking import KickingData

class ScrapeKicking():
    
    def __init__(self, logger=None):
        """Initialize

        Args:
            logger (Python Logger): A logger created from the Python Logger Class. Defaults to None.
        """
        self.__kicking_data_instance = KickingData(logger=logger)
        
    def scrape_data(self, url):
        """Scrapes kicking data from a player's page

        Args:
            url (string): URL for NFL player from www.pro-football-reference.com
        """
        scraper = ScrapeDataAbstract().create_scraper(url)
        
        self.__scrape_kicking_data(scraper)
        
        return self.__kicking_data_instance
    
    def __scrape_kicking_data(self, scraper):
        """Method for scraping scoring data
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        next_tag = ""
        
        for all_kicking in scraper.find_all(id="all_kicking"):
            if(all_kicking.find_all(id="switcher_kicking")):
                next_tag = all_kicking.find_all(id="switcher_kicking")[0]
            else:
                next_tag = all_kicking
            
            self.__kicking_regular_season(next_tag)
            self.__kicking_playoffs(next_tag)
            
    def __kicking_regular_season(self, scraper):
        """Method for scraping kicking for regular season
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        for identifier in scraper.find_all(id="div_kicking"):
            for table in identifier.find_all("table"):
                for tbody in table.find_all("tbody"):
                    for tr in tbody.find_all("tr"):
                        for th in tr.find_all("th"):
                            for a in th.find_all("a"):
                                current_year = int(a.text)
                        self.__kicking_data_instance.set_kicking_data_regular_season(self.__obtain_kicking_data(current_year, tr.find_all("td")))

    def __kicking_playoffs(self, scraper):
        """Method for scraping kicking data for playoffs
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        for identifier in scraper.find_all(id="div_kicking_playoffs"):
            for table in identifier.find_all("table"):
                for tbody in table.find_all("tbody"):
                    for tr in tbody.find_all("tr"):
                        for th in tr.find_all("th"):
                            for a in th.find_all("a"):
                                current_year = int(a.text)
                        self.__kicking_data_instance.set_kicking_data_playoffs(self.__obtain_kicking_data(current_year, tr.find_all("td")))

    
    def __obtain_kicking_data(self, year, section_data):
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
            elif (stat['data-stat'] == 'fga1'):
                if stat.text == "":
                    stats['fga1'] = [0]
                else:
                    stats['fga1'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fgm1'):
                if stat.text == "":
                    stats['fgm1'] = [0]
                else:
                    stats['fgm1'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fga2'):
                if stat.text == "":
                    stats['fga2'] = [0]
                else:
                    stats['fga2'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fgm2'):
                if stat.text == "":
                    stats['fgm2'] = [0]
                else:
                    stats['fgm2'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fga3'):
                if stat.text == "":
                    stats['fga3'] = [0]
                else:
                    stats['fga3'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fgm3'):
                if stat.text == "":
                    stats['fgm3'] = [0]
                else:
                    stats['fgm3'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fga4'):
                if stat.text == "":
                    stats['fga4'] = [0]
                else:
                    stats['fga4'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fgm4'):
                if stat.text == "":
                    stats['fgm4'] = [0]
                else:
                    stats['fgm4'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fga5'):
                if stat.text == "":
                    stats['fga5'] = [0]
                else:
                    stats['fga5'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fgm5'):
                if stat.text == "":
                    stats['fgm5'] = [0]
                else:
                    stats['fgm5'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fga'):
                if stat.text == "":
                    stats['fga'] = [0]
                else:
                    stats['fga'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fgm'):
                if stat.text == "":
                    stats['fgm'] = [0]
                else:
                    stats['fgm'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fg_long'):
                if stat.text == "":
                    stats['fg_long'] = [0]
                else:
                    stats['fg_long'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fg_perc'):
                if stat.text == "":
                    stats['fg_perc'] = [0.0]
                else:
                    stats['fg_perc'] = [float(stat.text.replace("%", ""))]
            elif (stat['data-stat'] == 'xpa'):
                if stat.text == "":
                    stats['xpa'] = [0]
                else:
                    stats['xpa'] = [int(stat.text)]
            elif (stat['data-stat'] == 'xpm'):
                if stat.text == "":
                    stats['xpm'] = [0]
                else:
                    stats['xpm'] = [int(stat.text)]
            elif (stat['data-stat'] == 'xp_perc'):
                if stat.text == "":
                    stats['xp_perc'] = [0.0]
                else:
                    stats['xp_perc'] = [float(stat.text.replace("%", ""))]
            elif (stat['data-stat'] == 'kickoff'):
                if stat.text == "":
                    stats['kickoff'] = [0]
                else:
                    stats['kickoff'] = [int(stat.text)]
            elif (stat['data-stat'] == 'kickoff_yds'):
                if stat.text == "":
                    stats['kickoff_yds'] = [0]
                else:
                    stats['kickoff_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'kickoff_tb'):
                if stat.text == "":
                    stats['kickoff_tb'] = [0]
                else:
                    stats['kickoff_tb'] = [int(stat.text)]
            elif (stat['data-stat'] == 'kickoff_tb_pct'):
                if stat.text == "":
                    stats['kickoff_tb_pct'] = [0.0]
                else:
                    stats['kickoff_tb_pct'] = [float(stat.text.replace("%", ""))]
            elif (stat['data-stat'] == 'kickoff_yds_avg'):
                if stat.text == "":
                    stats['kickoff_yds_avg'] = [0.0]
                else:
                    stats['kickoff_yds_avg'] = [float(stat.text)]
            elif (stat['data-stat'] == 'av'):
                if stat.text == "":
                    stats['approximate_value'] = [0]
                else:
                    stats['approximate_value'] = [int(stat.text)]
        return stats
    
    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")