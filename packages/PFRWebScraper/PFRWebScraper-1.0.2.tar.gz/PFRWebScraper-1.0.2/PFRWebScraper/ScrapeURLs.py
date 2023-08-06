from PFRWebScraper.Includes.Configuration import Configuration
from datetime import datetime

from PFRWebScraper.URL.Scrapers.ScrapeTeamURLs import ScrapeTeamURLs
from PFRWebScraper.URL.Scrapers.ScrapeStatTypeURLs import ScrapeStatTypeURLs

class ScrapeURLs():
    def __init__(self, logger=None):
        """Initialization
        """
        self.__config_parameters = Configuration().import_config("ScrapeData.config")
        self.nfl_positions = Configuration().import_config("Positions.config", section="POSITIONTOABBREVATION")
        self.__team_abbreviations = Configuration().import_config("TeamAbbreviations.config", section="TEAMTOABBREVIATION")
        self.__logger = logger
        
    def scrape_team_for_player_urls(self, team_name=None, year=datetime.now().year):
        """Scrapes team's page for the URLs of all their players

        Args:
            team_name (str): The name of the team you would like to scrape for URLs
                             URL Format: https://www.pro-football-reference.com/teams/{team_abbreviation}/{year}.htm
            year (int): The year you would like team URLs from. Defaults to current year.

        Returns:
            TeamURLData: An object containing the list of URLs
        """
        try:
            if(team_name):
                team_abbreviation = self.__team_abbreviations[team_name.title()]
                url_year = "/" + str(year) + ".htm"
                team_url = self.__config_parameters['baseURLTeam'] + team_abbreviation + url_year
                return ScrapeTeamURLs(self.__logger, self.__config_parameters['baseURL']).scrape_urls(team_url)
            
            return None
        except KeyError:
            raise KeyError("{0} was not a valid team name.".format(team_name))
        
    def scrape_stat_type_for_player_urls(self, stat_type=None, year=datetime.now().year):
        """Scrapes stat type's page for the URLs of all the players

        Args:
            stat_type (str): The name of the position you would like to scrape for URLs
                Stat Types: Passing, Rushing, Receiving, Kicking, Returns, Scoring 
                URL Format: https://www.pro-football-reference.com/years/{year}/{stat_type}.htm
            year (int): The year you would like team URLs from. Defaults to current year.

        Returns:
            PositionURLData: An object containing the list of URLs
        """
        stat_types = [
            'passing',
            'rushing',
            'receiving',
            'kicking',
            'returns',
            'scoring'
        ]
        if (stat_type and stat_type.lower() in stat_types):
            stat_url = "/" + stat_type.lower() + ".htm"
            url_year = "/" + str(year)
            stat_url = self.__config_parameters['baseURLYears'] + url_year + stat_url 
            return ScrapeStatTypeURLs(self.__logger, self.__config_parameters['baseURL']).scrape_urls(stat_url, stat_type.lower())
        
        return None
    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")