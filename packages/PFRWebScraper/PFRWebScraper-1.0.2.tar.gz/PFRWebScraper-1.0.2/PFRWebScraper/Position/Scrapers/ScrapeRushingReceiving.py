import os
import sys
from bs4 import Comment

scrapers_directory = os.path.dirname(__file__)
position_directory = os.path.dirname(scrapers_directory)
pfr_directory = os.path.dirname(position_directory)
sys.path.insert(0, pfr_directory)
sys.path.insert(1, position_directory)

from PFRWebScraper.Includes.ScrapeDataAbstract import ScrapeDataAbstract
from PFRWebScraper.Position.RushingReceiving.RushingReceiving import RushingReceivingData

class ScrapeRushingReceiving():
    
    def __init__(self, logger=None):
        """Initialize

        Args:
            logger (Python Logger): A logger created from the Python Logger Class. Defaults to None.
        """
        self.__rushing_receiving_data_instance = RushingReceivingData(logger=logger)
        
    def scrape_data(self, url):
        """Scrapes rushing and receiving data from a player's page

        Args:
            url (string): URL for NFL player from www.pro-football-reference.com
        """
        scraper = ScrapeDataAbstract().create_scraper(url)
        
        self.__rushing_receiving_data(scraper)
        self.__advanced_rushing_receiving(scraper)
        
        return self.__rushing_receiving_data_instance
    
    def __rushing_receiving_data(self, scraper):
        """Top level method for scraping passing data for regular season and playoffs

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        next_step = ""
        first_tag = "all_receiving_and_rushing"
        second_tag = "switcher_receiving_and_rushing"
        regular_season_tag = "div_receiving_and_rushing"
        playoffs_tag = "div_receiving_and_rushing_playoffs"
        
        if(scraper.find_all(id="all_rushing_and_receiving")):
            first_tag = "all_rushing_and_receiving"
            second_tag = "switcher_rushing_and_receiving"
            regular_season_tag = "div_rushing_and_receiving"
            playoffs_tag = "div_rushing_and_receiving_playoffs"
        
        for all_data in scraper.find_all(id=first_tag):
            if(all_data.find_all(id=second_tag)):
                next_tag = all_data.find_all(id=second_tag)[0]
            else:
                next_tag = all_data
            self.__rushing_receiving_regular_season(next_tag, regular_season_tag)
            self.__rushing_receiving_playoffs(next_tag, playoffs_tag)
                                
    def __rushing_receiving_regular_season(self, scraper, identifier):
        """Method for scraping rushing and receiving data for regular season
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        for identifier in scraper.find_all(id=identifier):
            for table in identifier.find_all("table"):
                for tbody in table.find_all("tbody"):
                    for tr in tbody.find_all("tr"):
                        for th in tr.find_all("th"):
                            for a in th.find_all("a"):
                                current_year = int(a.text)
                        self.__rushing_receiving_data_instance.set_rushing_receiving_data_regular_season(self.__obtain_rushing_receiving_data(current_year, tr.find_all("td")))
    
    def __rushing_receiving_playoffs(self, scraper, identifier):
        """Method for scraping rushing and receiving data for playoffs
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        for identifier in scraper.find_all(id=identifier):
            for table in identifier.find_all("table"):
                for tbody in table.find_all("tbody"):
                    for tr in tbody.find_all("tr"):
                        for th in tr.find_all("th"):
                            for a in th.find_all("a"):
                                current_year = int(a.text)
                        self.__rushing_receiving_data_instance.set_rushing_receiving_data_playoffs(self.__obtain_rushing_receiving_data(current_year, tr.find_all("td")))
    
    def __advanced_rushing_receiving(self, scraper):
        """Method for scraping advanced rushing and receiving data
        Passes relevant data to correlating object for storage
        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        first_tag = "all_detailed_receiving_and_rushing"
        identifier = "div_detailed_receiving_and_rushing"
        
        if(scraper.find_all(id="all_detailed_rushing_and_receiving")):
            first_tag = "all_detailed_rushing_and_receiving"
            identifier = "div_detailed_rushing_and_receiving"
            
        for parent_div in scraper.find_all(id=first_tag):
            # Scrapes the comment and then loads the HTML into a parser 
            #   to continue scraping information
            for comment in parent_div.find_all(text=lambda text:isinstance(text, Comment)):
                comment_soup = ScrapeDataAbstract().scrape_comment(comment)
                for child_div in comment_soup.find_all(id=identifier):
                    for table in child_div.find_all("table"):
                        for tbody in table.find_all("tbody"):
                            for tr in tbody.find_all("tr"):
                                for th in tr.find_all("th"):
                                    for a in th.find_all("a"):
                                        current_year = int(a.text)
                                self.__rushing_receiving_data_instance.set_rushing_receiving_data_advanced(self.__obtain_rushing_receiving_data(current_year, tr.find_all("td")))
    
    def __obtain_rushing_receiving_data(self, year, section_data):
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
            elif (stat['data-stat'] == 'rush_att'):
                if stat.text == "":
                    stats['rush_att'] = [0]
                else:
                    stats['rush_att'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rush_yds'):
                if stat.text == "":
                    stats['rush_yds'] = [0]
                else:
                    stats['rush_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rush_td'):
                if stat.text == "":
                    stats['rush_td'] = [0]
                else:
                    stats['rush_td'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rush_first_down'):
                if stat.text == "":
                    stats['rush_first_down'] = [0]
                else:
                    stats['rush_first_down'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rush_long'):
                if stat.text == "":
                    stats['rush_long'] = [0]
                else:
                    stats['rush_long'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rush_yds_per_att'):
                if stat.text == "":
                    stats['rush_yds_per_att'] = [0.0]
                else:
                    stats['rush_yds_per_att'] = [float(stat.text)]
            elif (stat['data-stat'] == 'rush_yds_per_g'):
                if stat.text == "":
                    stats['rush_yds_per_g'] = [0.0]
                else:
                    stats['rush_yds_per_g'] = [float(stat.text)]
            elif (stat['data-stat'] == 'rush_att_per_g'):
                if stat.text == "":
                    stats['rush_att_per_g'] = [0.0]
                else:
                    stats['rush_att_per_g'] = [float(stat.text)]
            elif (stat['data-stat'] == 'targets'):
                if stat.text == "":
                    stats['targets'] = [0]
                else:
                    stats['targets'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rec'):
                if stat.text == "":
                    stats['rec'] = [0]
                else:
                    stats['rec'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rec_yds'):
                if stat.text == "":
                    stats['rec_yds'] = [0]
                else:
                    stats['rec_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rec_yds_per_rec'):
                if stat.text == "":
                    stats['rec_yds_per_rec'] = [0.0]
                else:
                    stats['rec_yds_per_rec'] = [float(stat.text)]
            elif (stat['data-stat'] == 'rec_td'):
                if stat.text == "":
                    stats['rec_td'] = [0]
                else:
                    stats['rec_td'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rec_first_down'):
                if stat.text == "":
                    stats['rec_first_down'] = [0]
                else:
                    stats['rec_first_down'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rec_long'):
                if stat.text == "":
                    stats['rec_long'] = [0]
                else:
                    stats['rec_long'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rec_per_g'):
                if stat.text == "":
                    stats['rec_per_g'] = [0.0]
                else:
                    stats['rec_per_g'] = [float(stat.text)]
            elif (stat['data-stat'] == 'rec_yds_per_g'):
                if stat.text == "":
                    stats['rec_yds_per_g'] = [0.0]
                else:
                    stats['rec_yds_per_g'] = [float(stat.text)]
            elif (stat['data-stat'] == 'catch_pct'):
                if stat.text == "":
                    stats['catch_pct'] = [0.0]
                else:
                    stats['catch_pct'] = [float(stat.text.replace("%", ""))]
            elif (stat['data-stat'] == 'rec_yds_per_tgt'):
                if stat.text == "":
                    stats['rec_yds_per_tgt'] = [0.0]
                else:
                    stats['rec_yds_per_tgt'] = [float(stat.text)]
            elif (stat['data-stat'] == 'touches'):
                if stat.text == "":
                    stats['touches'] = [0]
                else:
                    stats['touches'] = [int(stat.text)]
            elif (stat['data-stat'] == 'yds_per_touch'):
                if stat.text == "":
                    stats['yds_per_touch'] = [0.0]
                else:
                    stats['yds_per_touch'] = [float(stat.text)]
            elif (stat['data-stat'] == 'yds_from_scrimmage'):
                if stat.text == "":
                    stats['yds_from_scrimmage'] = [0]
                else:
                    stats['yds_from_scrimmage'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rush_receive_td'):
                if stat.text == "":
                    stats['rush_receive_td'] = [0]
                else:
                    stats['rush_receive_td'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fumbles'):
                if stat.text == "":
                    stats['fumbles'] = [0]
                else:
                    stats['fumbles'] = [int(stat.text)]
            elif (stat['data-stat'] == 'av'):
                if stat.text == "":
                    stats['approximate_value'] = [0]
                else:
                    stats['approximate_value'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rush_yds_before_contact'):
                if stat.text == "":
                    stats['rush_yds_before_contact'] = [0]
                else:
                    stats['rush_yds_before_contact'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rush_yds_bc_per_rush'):
                if stat.text == "":
                    stats['rush_yds_bc_per_rush'] = [0.0]
                else:
                    stats['rush_yds_bc_per_rush'] = [float(stat.text)]
            elif (stat['data-stat'] == 'rush_yac'):
                if stat.text == "":
                    stats['rush_yac'] = [0]
                else:
                    stats['rush_yac'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rush_yac_per_rush'):
                if stat.text == "":
                    stats['rush_yac_per_rush'] = [0.0]
                else:
                    stats['rush_yac_per_rush'] = [float(stat.text)]
            elif (stat['data-stat'] == 'rush_broken_tackles'):
                if stat.text == "":
                    stats['rush_broken_tackles'] = [0]
                else:
                    stats['rush_broken_tackles'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rush_broken_tackles_per_rush'):
                if stat.text == "":
                    stats['rush_broken_tackles_per_rush'] = [0.0]
                else:
                    stats['rush_broken_tackles_per_rush'] = [float(stat.text)]
            elif (stat['data-stat'] == 'rec_air_yds'):
                if stat.text == "":
                    stats['rec_air_yds'] = [0]
                else:
                    stats['rec_air_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rec_air_yds_per_rec'):
                if stat.text == "":
                    stats['rec_air_yds_per_rec'] = [0.0]
                else:
                    stats['rec_air_yds_per_rec'] = [float(stat.text)]
            elif (stat['data-stat'] == 'rec_yac'):
                if stat.text == "":
                    stats['rec_yac'] = [0]
                else:
                    stats['rec_yac'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rec_yac_per_rec'):
                if stat.text == "":
                    stats['rec_yac_per_rec'] = [0.0]
                else:
                    stats['rec_yac_per_rec'] = [float(stat.text)]
            elif (stat['data-stat'] == 'rec_adot'):
                if stat.text == "":
                    stats['rec_adot'] = [0.0]
                else:
                    stats['rec_adot'] = [float(stat.text)]
            elif (stat['data-stat'] == 'rec_broken_tackles'):
                if stat.text == "":
                    stats['rec_broken_tackles'] = [0]
                else:
                    stats['rec_broken_tackles'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rec_broken_tackles_per_rec'):
                if stat.text == "":
                    stats['rec_broken_tackles_per_rec'] = [0.0]
                else:
                    stats['rec_broken_tackles_per_rec'] = [float(stat.text)]
            elif (stat['data-stat'] == 'rec_drops'):
                if stat.text == "":
                    stats['rec_drops'] = [0]
                else:
                    stats['rec_drops'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rec_drop_pct'):
                if stat.text == "":
                    stats['rec_drop_pct'] = [0.0]
                else:
                    stats['rec_drop_pct'] = [float(stat.text)]
            elif (stat['data-stat'] == 'rec_target_int'):
                if stat.text == "":
                    stats['rec_target_int'] = [0]
                else:
                    stats['rec_target_int'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rec_pass_rating'):
                if stat.text == "":
                    stats['rec_pass_rating'] = [0.0]
                else:
                    stats['rec_pass_rating'] = [float(stat.text)]
                    
        return stats
    
    def __logging(self, message):
        """Checks to see if there is a logger and if there is logs the message to the error log
        
        Args:
            message (str): Error message
        """
        if (self.__logger):
            self.__logger.error(message)

    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")
    