import os
import sys

scrapers_directory = os.path.dirname(__file__)
position_directory = os.path.dirname(scrapers_directory)
pfr_directory = os.path.dirname(position_directory)
sys.path.insert(0, pfr_directory)
sys.path.insert(1, position_directory)

from PFRWebScraper.Includes.ScrapeDataAbstract import ScrapeDataAbstract
from PFRWebScraper.Position.Passing.Passing import PassingData

class ScrapePassing():
    
    def __init__(self, logger=None):
        """Initialize

        Args:
            logger (Python Logger): A logger created from the Python Logger Class. Defaults to None.
        """
        self.__passing_data_instance = PassingData(logger=logger)
    
    def scrape_data(self, url, data_type=["passing", "advanced", "adjusted"]):
        """Scrapes passing data from players page.

        Args:
            url (str): Must be a player from the following website format https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
            data_type (list): Receives a list of parameters that explain what data to scrape. 
                            The following values can be passed:
                            "all" - Scrapes all the data on a passer.
                            "passing" - Scrapes Regular Season and Playoff data on a passer.
                            "advanced" - Scrapes Air Yards, Accuracy, Pressure, and Play Type data on a passer.
                            "adjusted" - Scrapes Adjusted data on a passer.
                            Reference https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm to
                                see what data you may want to pull.
                            Defaults to ["all"].

        Returns:
            PassingData: A Object that allows you to obtain other objects around more specified data depending on the 
                        data_type you specified.  If you did not specify a data type all objects will be available.
                        Other Objects:
                            PassingRegularSeason
                            PassingPlayoffs
                            PassingAdvancedAirYards
                            PassingAdvancedAccuracy
                            PassingAdvancedPressure
                            PassingAdvancedPlayType
                            PassingAdjusted
        """
        scraper = ScrapeDataAbstract().create_scraper(url)
        
        if("passing" in data_type):
            self.__passing_data(scraper)
        if("advanced" in data_type):
            self.__advanced_passing(scraper)
        if("adjusted" in data_type):
            self.__adjusted_passing(scraper)
        
        return self.__passing_data_instance
        
    def __passing_data(self, scraper):
        """Top level method for scraping passing data for regular season and playoffs

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        next_tag = ""
        
        for all_stats in scraper.find_all(id="all_passing"):
            if(all_stats.find_all(id="switcher_passing")):
                next_tag = all_stats.find_all(id="switcher_passing")[0]
            else:
                next_tag = all_stats
            self.__passing_data_regular_season(next_tag)
            self.__passing_data_playoffs(next_tag)
                
                                
    def __passing_data_regular_season(self, scraper):
        """Method for scraping passing data for regular season
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        current_year = None
        
        for div_passing in scraper.find_all(id="div_passing"):
            for table in div_passing.find_all("table"):
                for tbody in table.find_all("tbody"):
                    for tr in tbody.find_all("tr"):
                        for th in tr.find_all("th"):
                            for a in th.find_all("a"):
                                current_year = int(a.text)
                        self.__passing_data_instance.set_passing_data_regular_season(self.__obtain_passing_data(current_year, tr.find_all("td")))
                        
    def __passing_data_playoffs(self, scraper):
        """Method for scraping passing data for playoffs
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        current_year = None
        
        for div_passing in scraper.find_all(id="div_passing_playoffs"):
            for table in div_passing.find_all("table"):
                for tbody in table.find_all("tbody"):
                    for tr in tbody.find_all("tr"):
                        for th in tr.find_all("th"):
                            for a in th.find_all("a"):
                                current_year = int(a.text)
                        self.__passing_data_instance.set_passing_data_playoffs(self.__obtain_passing_data(current_year, tr.find_all("td")))
    
    def __advanced_passing(self, scraper):
        """Top level method for scraping advanced passing data

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        for all_passing_detailed in scraper.find_all(id="all_passing_detailed"):
            for switcher_passing_detailed in all_passing_detailed.find_all(id="switcher_passing_detailed"):
                self.__advanced_passing_air_yards(switcher_passing_detailed)
                self.__advanced_passing_accuracy(switcher_passing_detailed)
                self.__advanced_passing_pressure(switcher_passing_detailed)
                self.__advanced_passing_play_type(switcher_passing_detailed)
    
    def __advanced_passing_air_yards(self, scraper):
        """Method for scraping advanced passing data air yards
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        current_year = None
        
        for div_advanced_air_yards in scraper.find_all(id="div_advanced_air_yards"):
            for table in div_advanced_air_yards.find_all("table"):
                for tbody in table.find_all("tbody"):
                    for tr in tbody.find_all("tr"):
                        for th in tr.find_all("th"):
                            for a in th.find_all("a"):
                                current_year = int(a.text)
                        self.__passing_data_instance.set_passing_data_advanced_air_yards(self.__obtain_passing_data(current_year, tr.find_all("td")))
    
    def __advanced_passing_accuracy(self, scraper):
        """Method for scraping advanced passing data accuracy
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        current_year = None
        
        for div_advanced_accuracy in scraper.find_all(id="div_advanced_accuracy"):
                for table in div_advanced_accuracy.find_all("table"):
                    for tbody in table.find_all("tbody"):
                        for tr in tbody.find_all("tr"):
                            for th in tr.find_all("th"):
                                for a in th.find_all("a"):
                                    current_year = int(a.text)
                            self.__passing_data_instance.set_passing_data_advanced_accuracy(self.__obtain_passing_data(current_year, tr.find_all("td")))
    
    
    def __advanced_passing_pressure(self, scraper):
        """Method for scraping advanced passing data pressure
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        current_year = None
        
        for div_advanced_pressure in scraper.find_all(id="div_advanced_pressure"):
                for table in div_advanced_pressure.find_all("table"):
                    for tbody in table.find_all("tbody"):
                        for tr in tbody.find_all("tr"):
                            for th in tr.find_all("th"):
                                for a in th.find_all("a"):
                                    current_year = int(a.text)
                            self.__passing_data_instance.set_passing_data_advanced_pressure(self.__obtain_passing_data(current_year, tr.find_all("td")))
    
    def __advanced_passing_play_type(self, scraper):
        """Method for scraping advanced passing data play type
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        current_year = None
        
        for div_advanced_play_type in scraper.find_all(id="div_advanced_play_type"):
                for table in div_advanced_play_type.find_all("table"):
                    for tbody in table.find_all("tbody"):
                        for tr in tbody.find_all("tr"):
                            for th in tr.find_all("th"):
                                for a in th.find_all("a"):
                                    current_year = int(a.text)
                            self.__passing_data_instance.set_passing_data_advanced_play_type(self.__obtain_passing_data(current_year, tr.find_all("td")))
    
    def __adjusted_passing(self, scraper):
        """Method for scraping adjusted passing data
        Passes relevant data to correlating object for storage

        Args:
            scraper (BeautifulSoup): A beautifulsoup object for parsing
        """
        current_year = None
        
        for all_passing_advanced in scraper.find_all(id="all_passing_advanced"):
            for div_passing_advanced in all_passing_advanced.find_all(id="div_passing_advanced"):
                for table in div_passing_advanced.find_all("table"):
                    for tbody in table.find_all("tbody"):
                        for tr in tbody.find_all("tr"):
                            for th in tr.find_all("th"):
                                for a in th.find_all("a"):
                                    current_year = int(a.text)
                            self.__passing_data_instance.set_passing_data_adjusted(self.__obtain_passing_data(current_year, tr.find_all("td")))
                            
    def __obtain_passing_data(self, year, section_data):
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
            elif (stat['data-stat'] == 'qb_rec'):
                try:
                    stats['wins'] = [int(str(stat.text).split("-")[0])]
                except IndexError:
                    stats['wins'] = [0]
                try:
                    stats['losses'] = [int(str(stat.text).split("-")[1])]
                except IndexError:
                    stats['losses'] = [0]
                try:
                    stats['ties'] = [int(str(stat.text).split("-")[2])]
                except IndexError:
                    stats['ties'] = [0]
            elif (stat['data-stat'] == 'pass_cmp'):
                if stat.text == "":
                    stats['pass_cmp'] = [0]
                else:
                    stats['pass_cmp'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_att'):
                if stat.text == "":
                    stats['pass_att'] = [0]
                else:
                    stats['pass_att'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_cmp_perc'):
                if stat.text == "":
                    stats['pass_cmp_perc'] = [0.0]
                else:
                    stats['pass_cmp_perc'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_yds'):
                if stat.text == "":
                    stats['pass_yds'] = [0]
                else:
                    stats['pass_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_td'):
                if stat.text == "":
                    stats['pass_td'] = [0]
                else:
                    stats['pass_td'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_td_perc'):
                if stat.text == "":
                    stats['pass_td_perc'] = [0.0]
                else:
                    stats['pass_td_perc'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_int'):
                if stat.text == "":
                    stats['pass_int'] = [0]
                else:
                    stats['pass_int'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_int_perc'):
                if stat.text == "":
                    stats['pass_int_perc'] = [0.0]
                else:
                    stats['pass_int_perc'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_first_down'):
                if stat.text == "":
                    stats['pass_first_down'] = [0]
                else:
                    stats['pass_first_down'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_long'):
                if stat.text == "":
                    stats['pass_long'] = [0]
                else:
                    stats['pass_long'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_yds_per_att'):
                if stat.text == "":
                    stats['pass_yds_per_att'] = [0.0]
                else:
                    stats['pass_yds_per_att'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_adj_yds_per_att'):
                if stat.text == "":
                    stats['pass_adj_yds_per_att'] = [0.0]
                else:
                    stats['pass_adj_yds_per_att'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_yds_per_cmp'):
                if stat.text == "":
                    stats['pass_yds_per_cmp'] = [0.0]
                else:
                    stats['pass_yds_per_cmp'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_yds_per_g'):
                if stat.text == "":
                    stats['pass_yds_per_g'] = [0.0]
                else:
                    stats['pass_yds_per_g'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_rating'):
                if stat.text == "":
                    stats['pass_rating'] = [0.0]
                else:
                    stats['pass_rating'] = [float(stat.text)]
            elif (stat['data-stat'] == 'qbr'):
                if stat.text == "":
                    stats['qbr'] = [0.0]
                else:
                    stats['qbr'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_sacked'):
                if stat.text == "":
                    stats['pass_sacked'] = [0]
                else:
                    stats['pass_sacked'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_sacked_yds'):
                if stat.text == "":
                    stats['pass_sacked_yds'] = [0]
                else:
                    stats['pass_sacked_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_sacked_perc'):
                if stat.text == "":
                    stats['pass_sacked_perc'] = [0.0]
                else:
                    stats['pass_sacked_perc'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_net_yds_per_att'):
                if stat.text == "":
                    stats['pass_net_yds_per_att'] = [0.0]
                else:
                    stats['pass_net_yds_per_att'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_adj_net_yds_per_att'):
                if stat.text == "":
                    stats['pass_adj_net_yds_per_att'] = [0.0]
                else:
                    stats['pass_adj_net_yds_per_att'] = [float(stat.text)]
            elif (stat['data-stat'] == 'comebacks'):
                if stat.text == "":
                    stats['4Q_comebacks'] = [0]
                else:
                    stats['4Q_comebacks'] = [int(stat.text)]
            elif (stat['data-stat'] == 'gwd'):
                if stat.text == "":
                    stats['game_winning_drives'] = [0]
                else:
                    stats['game_winning_drives'] = [int(stat.text)]
            elif (stat['data-stat'] == 'av'):
                if stat.text == "":
                    stats['approximate_value'] = [0]
                else:
                    stats['approximate_value'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_yds_per_att_index'):
                if stat.text == "":
                    stats['pass_yds_per_att_index'] = [0]
                else:
                    stats['pass_yds_per_att_index'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_net_yds_per_att_index'):
                if stat.text == "":
                    stats['pass_net_yds_per_att_index'] = [0]
                else:
                    stats['pass_net_yds_per_att_index'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_adj_yds_per_att_index'):
                if stat.text == "":
                    stats['pass_adj_yds_per_att_index'] = [0]
                else:
                    stats['pass_adj_yds_per_att_index'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_adj_net_yds_per_att_index'):
                if stat.text == "":
                    stats['pass_adj_net_yds_per_att_index'] = [0]
                else:
                    stats['pass_adj_net_yds_per_att_index'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_cmp_perc_index'):
                if stat.text == "":
                    stats['pass_cmp_perc_index'] = [0]
                else:
                    stats['pass_cmp_perc_index'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_td_perc_index'):
                if stat.text == "":
                    stats['pass_td_perc_index'] = [0]
                else:
                    stats['pass_td_perc_index'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_int_perc_index'):
                if stat.text == "":
                    stats['pass_int_perc_index'] = [0]
                else:
                    stats['pass_int_perc_index'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_sacked_perc_index'):
                if stat.text == "":
                    stats['pass_sacked_perc_index'] = [0]
                else:
                    stats['pass_sacked_perc_index'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_rating_index'):
                if stat.text == "":
                    stats['pass_rating_index'] = [0]
                else:
                    stats['pass_rating_index'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_target_yds'):
                if stat.text == "":
                    stats['pass_target_yds'] = [0]
                else:
                    stats['pass_target_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_tgt_yds_per_att'):
                if stat.text == "":
                    stats['pass_tgt_yds_per_att'] = [0.0]
                else:
                    stats['pass_tgt_yds_per_att'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_air_yds'):
                if stat.text == "":
                    stats['pass_air_yds'] = [0]
                else:
                    stats['pass_air_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_air_yds_per_cmp'):
                if stat.text == "":
                    stats['pass_air_yds_per_cmp'] = [0.0]
                else:
                    stats['pass_air_yds_per_cmp'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_air_yds_per_att'):
                if stat.text == "":
                    stats['pass_air_yds_per_att'] = [0.0]
                else:
                    stats['pass_air_yds_per_att'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_yac'):
                if stat.text == "":
                    stats['pass_yac'] = [0]
                else:
                    stats['pass_yac'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_yac_per_cmp'):
                if stat.text == "":
                    stats['pass_yac_per_cmp'] = [0.0]
                else:
                    stats['pass_yac_per_cmp'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_batted_passes'):
                if stat.text == "":
                    stats['pass_batted_passes'] = [0]
                else:
                    stats['pass_batted_passes'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_throwaways'):
                if stat.text == "":
                    stats['pass_throwaways'] = [0]
                else:
                    stats['pass_throwaways'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_spikes'):
                if stat.text == "":
                    stats['pass_spikes'] = [0]
                else:
                    stats['pass_spikes'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_drops'):
                if stat.text == "":
                    stats['pass_drops'] = [0]
                else:
                    stats['pass_drops'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_drop_pct'):
                if stat.text == "":
                    stats['pass_drop_pct'] = [0.0]
                else:
                    stats['pass_drop_pct'] = [float(stat.text.replace("%",""))]
            elif (stat['data-stat'] == 'pass_poor_throws'):
                if stat.text == "":
                    stats['pass_poor_throws'] = [0]
                else:
                    stats['pass_poor_throws'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_poor_throw_pct'):
                if stat.text == "":
                    stats['pass_poor_throw_pct'] = [0.0]
                else:
                    stats['pass_poor_throw_pct'] = [float(stat.text.replace("%",""))]
            elif (stat['data-stat'] == 'pass_on_target'):
                if stat.text == "":
                    stats['pass_on_target'] = [0]
                else:
                    stats['pass_on_target'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_on_target_pct'):
                if stat.text == "":
                    stats['pass_on_target_pct'] = [0.0]
                else:
                    stats['pass_on_target_pct'] = [float(stat.text.replace("%",""))]
            elif (stat['data-stat'] == 'pocket_time'):
                if stat.text == "":
                    stats['pocket_time'] = [0.0]
                else:
                    stats['pocket_time'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_blitzed'):
                if stat.text == "":
                    stats['pass_blitzed'] = [0]
                else:
                    stats['pass_blitzed'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_hurried'):
                if stat.text == "":
                    stats['pass_hurried'] = [0]
                else:
                    stats['pass_hurried'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_hits'):
                if stat.text == "":
                    stats['pass_hits'] = [0]
                else:
                    stats['pass_hits'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_pressured'):
                if stat.text == "":
                    stats['pass_pressured'] = [0]
                else:
                    stats['pass_pressured'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_pressured_pct'):
                if stat.text == "":
                    stats['pass_pressured_pct'] = [0.0]
                else:
                    stats['pass_pressured_pct'] = [float(stat.text.replace("%",""))]
            elif (stat['data-stat'] == 'rush_scrambles'):
                if stat.text == "":
                    stats['rush_scrambles'] = [0]
                else:
                    stats['rush_scrambles'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rush_scrambles_yds_per_att'):
                if stat.text == "":
                    stats['rush_scrambles_yds_per_att'] = [0.0]
                else:
                    stats['rush_scrambles_yds_per_att'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_rpo'):
                if stat.text == "":
                    stats['pass_rpo'] = [0]
                else:
                    stats['pass_rpo'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_rpo_yds'):
                if stat.text == "":
                    stats['pass_rpo_yds'] = [0]
                else:
                    stats['pass_rpo_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_rpo_pass_att'):
                if stat.text == "":
                    stats['pass_rpo_pass_att'] = [0]
                else:
                    stats['pass_rpo_pass_att'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_rpo_pass_yds'):
                if stat.text == "":
                    stats['pass_rpo_pass_yds'] = [0]
                else:
                    stats['pass_rpo_pass_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_rpo_rush_att'):
                if stat.text == "":
                    stats['pass_rpo_rush_att'] = [0]
                else:
                    stats['pass_rpo_rush_att'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_rpo_rush_yds'):
                if stat.text == "":
                    stats['pass_rpo_rush_yds'] = [0]
                else:
                    stats['pass_rpo_rush_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_play_action'):
                if stat.text == "":
                    stats['pass_play_action'] = [0]
                else:
                    stats['pass_play_action'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_play_action_pass_yds'):
                if stat.text == "":
                    stats['pass_play_action_pass_yds'] = [0]
                else:
                    stats['pass_play_action_pass_yds'] = [int(stat.text)]
                    
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
    