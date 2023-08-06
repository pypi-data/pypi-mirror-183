from PFRWebScraper.Includes.Configuration import Configuration

from PFRWebScraper.Position.Scrapers.ScrapePassing import ScrapePassing
from PFRWebScraper.Position.Scrapers.ScrapeRushingReceiving import ScrapeRushingReceiving
from PFRWebScraper.Position.Scrapers.ScrapeScoring import ScrapeScoring
from PFRWebScraper.Position.Scrapers.ScrapeSnapCounts import ScrapeSnapCounts
from PFRWebScraper.Position.Scrapers.ScrapeDefenseAndFumbles import ScrapeDefenseAndFumbles
from PFRWebScraper.Position.Scrapers.ScrapeReturns import ScrapeReturns
from PFRWebScraper.Position.Scrapers.ScrapeKicking import ScrapeKicking

class ScrapePlayerData():
    def __init__(self, logger=None):
        """Initialization
        """
        self.nfl_positions = Configuration().import_config("Positions.config", section="ABBREVIATIONTOPOSITION")
        self.team_abbreviations = Configuration().import_config("TeamAbbreviations.config", section="ABBREVIATIONTOTEAM")
        self.__logger = logger
        
    def scrape_passing(self, player_url=None, sections=["passing", "advanced", "adjusted"]):
        """Scrapes player's page for passing data and returns an object with that passing data stored

        Args:
            player_url (str): Must be a player from the following website format https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm 
                            Defaults to None.
            sections (list): Receives a list of parameters that explain what data to scrape. 
                            The following values can be passed:
                            "all" - Scrapes all the data on a passer.
                            "passing" - Scrapes Regular Season and Playoff data on a passer.
                            "advanced" - Scrapes Air Yards, Accuracy, Pressure, and Play Type data on a passer.
                            "adjusted" - Scrapes Adjusted data on a passer.
                            Reference https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm to
                                see what data you may want to pull.
                            Defaults to ["all"].

        Returns:
            PassingData: An object containing the passing data for a player
        """
        if(player_url):
            return ScrapePassing(self.__logger).scrape_data(player_url, data_type=sections)
    
        return None
        
    def scrape_rushing_receiving(self, player_url=None):
        """Scrapes player's page for rushing and receiving data and returns an object with that rushing and receiving data stored

        Args:
            player_url (str): Must be a player from the following website format https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm 
                            Defaults to None.

        Returns:
            RushingReceivingData: An object containing the rushing and receiving data for a player
        """
        if(player_url):
            return ScrapeRushingReceiving(self.__logger).scrape_data(player_url)
        
        return None
        
    def scrape_scoring(self, player_url=None):
        """Scrapes player's page for scoring data and returns an object with that scoring data stored

        Args:
            player_url (str): Must be a player from the following website format https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm 
                            Defaults to None.

        Returns:
            ScoringData: An object containing the scoring data for a player
        """
        if(player_url):
            return ScrapeScoring(self.__logger).scrape_data(player_url)
        
        return None
        
    def scrape_snap_counts(self, player_url=None):
        """Scrapes player's page for snap counts data and returns an object with that snap counts data stored

        Args:
            player_url (str): Must be a player from the following website format https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm 
                            Defaults to None.

        Returns:
            SnapCountsData: An object containing the snap counts data for a player
        """
        if(player_url):
            return ScrapeSnapCounts(self.__logger).scrape_data(player_url)
        
        return None
    
    def scrape_defense_and_fumbles(self, player_url=None):
        """Scrapes player's page for defense and fumbles data and returns an object with that defense and fumbles data stored

        Args:
            player_url (str): Must be a player from the following website format https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm 
                            Defaults to None.

        Returns:
            DefenseAndFumblesData: An object containing the defense and fumbles data for a player
        """
        if(player_url):
            return ScrapeDefenseAndFumbles(self.__logger).scrape_data(player_url)
        
        return None
    
    def scrape_kick_and_punt_returns(self, player_url=None):
        """Scrapes player's page for kick and punt return data and returns an object with that kick and punt return data stored

        Args:
            player_url (str): Must be a player from the following website format https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm 
                            Defaults to None.

        Returns:
            ReturnsData: An object containing the kick and punt return data for a player
        """
        if(player_url):
            return ScrapeReturns(self.__logger).scrape_data(player_url)
        
        return None
    
    def scrape_kicking(self, player_url=None):
        """Scrapes player's page for kicking data and returns an object with that kicking data stored

        Args:
            player_url (str): Must be a player from the following website format https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm 
                            Defaults to None.

        Returns:
            KickingData: An object containing the kicking data for a player
        """
        if(player_url):
            return ScrapeKicking(self.__logger).scrape_data(player_url)
        
        return None
    
    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")