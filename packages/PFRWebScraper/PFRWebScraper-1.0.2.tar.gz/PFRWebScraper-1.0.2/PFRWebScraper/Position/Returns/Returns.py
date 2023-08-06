from PFRWebScraper.Position.Returns.ReturnsRegularSeason import ReturnsRegularSeason
from PFRWebScraper.Position.Returns.ReturnsPlayoffs import ReturnsPlayoffs

class ReturnsData():
    def __init__(self, logger=None, season_games=17):
        """Sets initial values for use within an object

        Args:
            logger (Logger): Python Default Logger Class
            season_games (int, optional): Number of games in an NFL season. Defaults to 17.
        """
        self.__logger = logger
            
        self.__generic_error_message = "An error has occurred please check the log for more information.\nError:"
        self.season_games = season_games
        
        self.__returns_regular_season_stats = None
        self.__returns_playoffs_stats = None
            
    def set_returns_data_regular_season(self, returns_data):
        """Sets the kick and punt returns data for the regular season in the object

        Args:
            returns_data (dict): Returns data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__returns_regular_season_stats, ReturnsRegularSeason)):
            self.__returns_regular_season_stats.parse_returns_data(returns_data)
        else:
            self.__returns_regular_season_stats = ReturnsRegularSeason(self.__logger, self.season_games, self.__generic_error_message, returns_data)
                
    def set_returns_data_playoffs(self, returns_data):
        """Sets the kick and punt returns data for the playoffs in the object

        Args:
            returns_data (dict): Returns data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__returns_playoffs_stats, ReturnsPlayoffs)):
            self.__returns_playoffs_stats.parse_returns_data(returns_data)
        else:
            self.__returns_playoffs_stats = ReturnsPlayoffs(self.__logger, self.season_games, self.__generic_error_message, returns_data)
            
    def get_returns_data_regular_season(self):
        """Returns the object for kick and punt returns regular season stats

        Returns:
            ReturnsRegularSeason: Object containing returns data for the regular season
        """
        return self.__returns_regular_season_stats
    
    def get_returns_data_playoffs(self):
        """Returns the object for kick and punt returns playoff stats

        Returns:
            ReturnsPlayoffs: Object containing returns data for the playoffs
        """
        return self.__returns_playoffs_stats
    
    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")