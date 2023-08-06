from PFRWebScraper.Position.Kicking.KickingRegularSeason import KickingRegularSeason
from PFRWebScraper.Position.Kicking.KickingPlayoffs import KickingPlayoffs

class KickingData():
    def __init__(self, logger=None, season_games=17):
        """Sets initial values for use within an object

        Args:
            logger (Logger): Python Default Logger Class
            season_games (int, optional): Number of games in an NFL season. Defaults to 17.
        """
        self.__logger = logger
            
        self.__generic_error_message = "An error has occurred please check the log for more information.\nError:"
        self.season_games = season_games
        
        self.__kicking_regular_season_stats = None
        self.__kicking_playoffs_stats = None
            
    def set_kicking_data_regular_season(self, kicking_data):
        """Sets the kicking data for the regular season in the object

        Args:
            kicking_data (dict): Kicking data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__kicking_regular_season_stats, KickingRegularSeason)):
            self.__kicking_regular_season_stats.parse_kicking_data(kicking_data)
        else:
            self.__kicking_regular_season_stats = KickingRegularSeason(self.__logger, self.season_games, self.__generic_error_message, kicking_data)
                
    def set_kicking_data_playoffs(self, kicking_data):
        """Sets the kicking data for the playoffs in the object

        Args:
            kicking_data (dict): Kicking data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__kicking_playoffs_stats, KickingPlayoffs)):
            self.__kicking_playoffs_stats.parse_kicking_data(kicking_data)
        else:
            self.__kicking_playoffs_stats = KickingPlayoffs(self.__logger, self.season_games, self.__generic_error_message, kicking_data)
            
    def get_kicking_data_regular_season(self):
        """Returns the object for kicking regular season stats

        Returns:
            KickingRegularSeason: Object containing kicking data for the regular season
        """
        return self.__kicking_regular_season_stats
    
    def get_kicking_data_playoffs(self):
        """Returns the object for kicking playoff stats

        Returns:
            KickingPlayoffs: Object containing kicking data for the playoffs
        """
        return self.__kicking_playoffs_stats
    
    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")