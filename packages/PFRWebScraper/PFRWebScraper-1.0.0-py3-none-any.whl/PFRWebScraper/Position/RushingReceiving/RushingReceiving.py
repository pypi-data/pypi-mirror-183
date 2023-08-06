from PFRWebScraper.Position.RushingReceiving.RushingReceivingRegularSeason import RushingReceivingRegularSeason
from PFRWebScraper.Position.RushingReceiving.RushingReceivingPlayoffs import RushingReceivingPlayoffs
from PFRWebScraper.Position.RushingReceiving.RushingReceivingAdvanced import RushingReceivingAdvanced

class RushingReceivingData():
    def __init__(self, logger=None, season_games=17):
        """Sets initial values for use within an object

        Args:
            logger (Logger): Python Default Logger Class
            season_games (int, optional): Number of games in an NFL season. Defaults to 17.
        """
        self.__logger = logger
            
        self.__generic_error_message = "An error has occurred please check the log for more information.\nError:"
        self.season_games = season_games
        
        self.__rushing_receiving_regular_season = None
        self.__rushing_receiving_playoffs = None
        self.__rushing_receiving_advanced = None
        
    def set_rushing_receiving_data_regular_season(self, rushing_receiving_data):
        """Sets the rushing and receiving data for the regular season in the object

        Args:
            rushing_receiving_data (dict): rushing and receiving data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__rushing_receiving_regular_season, RushingReceivingRegularSeason)):
            self.__rushing_receiving_regular_season.parse_rushing_receiving_data(rushing_receiving_data)
        else:
            self.__rushing_receiving_regular_season = RushingReceivingRegularSeason(self.__logger, self.season_games, self.__generic_error_message, rushing_receiving_data)
            
    def set_rushing_receiving_data_playoffs(self, rushing_receiving_data):
        """Sets the rushing and receiving data for the regular season in the object

        Args:
            rushing_receiving_data (dict): rushing and receiving data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__rushing_receiving_playoffs, RushingReceivingPlayoffs)):
            self.__rushing_receiving_playoffs.parse_rushing_receiving_data(rushing_receiving_data)
        else:
            self.__rushing_receiving_playoffs = RushingReceivingPlayoffs(self.__logger, self.season_games, self.__generic_error_message, rushing_receiving_data)
            
    def set_rushing_receiving_data_advanced(self, rushing_receiving_data):
        """Sets the rushing and receiving data for the regular season in the object

        Args:
            rushing_receiving_data (dict): rushing and receiving data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__rushing_receiving_advanced, RushingReceivingAdvanced)):
            self.__rushing_receiving_advanced.parse_rushing_receiving_data(rushing_receiving_data)
        else:
            self.__rushing_receiving_advanced = RushingReceivingAdvanced(self.__logger, self.season_games, self.__generic_error_message, rushing_receiving_data)
            
    def get_rushing_receiving_data_regular_season(self):
        """Returns the object for passing regular season stats

        Returns:
            RushingReceivingRegularSeason: Object containing passing data for the regular season
        """
        return self.__rushing_receiving_regular_season
    
    def get_rushing_receiving_data_playoffs(self):
        """Returns the object for passing regular season stats

        Returns:
            RushingReceivingPlayoffs: Object containing passing data for the regular season
        """
        return self.__rushing_receiving_playoffs
    
    def get_rushing_receiving_data_advanced(self):
        """Returns the object for passing regular season stats

        Returns:
            RushingReceivingAdvanced: Object containing passing data for the regular season
        """
        return self.__rushing_receiving_advanced


if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")