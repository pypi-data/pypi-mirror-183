from PFRWebScraper.Position.Passing.PassingRegularSeason import PassingRegularSeason
from PFRWebScraper.Position.Passing.PassingPlayoffs import PassingPlayoffs
from PFRWebScraper.Position.Passing.PassingAdvancedAirYards import PassingAdvancedAirYards
from PFRWebScraper.Position.Passing.PassingAdvancedAccuracy import PassingAdvancedAccuracy
from PFRWebScraper.Position.Passing.PassingAdvancedPressure import PassingAdvancedPressure
from PFRWebScraper.Position.Passing.PassingAdvancedPlayType import PassingAdvancedPlayType
from PFRWebScraper.Position.Passing.PassingAdjusted import PassingAdjusted

class PassingData():
    def __init__(self, logger=None, season_games=17):
        """Sets initial values for use within an object

        Args:
            logger (Logger): Python Default Logger Class
            season_games (int, optional): Number of games in an NFL season. Defaults to 17.
        """
        self.__logger = logger
            
        self.__generic_error_message = "An error has occurred please check the log for more information.\nError:"
        self.season_games = season_games
        
        self.__passing_regular_season_stats = None
        self.__passing_playoffs_stats = None
        self.__passing_advanced_air_yards = None
        self.__passing_advanced_accuracy = None
        self.__passing_advanced_pressure = None
        self.__passing_advanced_play_type = None
        self.__passing_adjusted = None
            
    def set_passing_data_regular_season(self, passing_data):
        """Sets the passing data for the regular season in the object

        Args:
            passing_data (dict): Passing data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__passing_regular_season_stats, PassingRegularSeason)):
            self.__passing_regular_season_stats.parse_passing_data(passing_data)
        else:
            self.__passing_regular_season_stats = PassingRegularSeason(self.__logger, self.season_games, self.__generic_error_message, passing_data)
                
    def set_passing_data_playoffs(self, passing_data):
        """Sets the passing data for the playoffs in the object

        Args:
            passing_data (dict): Passing data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__passing_playoffs_stats, PassingPlayoffs)):
            self.__passing_playoffs_stats.parse_passing_data(passing_data)
        else:
            self.__passing_playoffs_stats = PassingPlayoffs(self.__logger, self.season_games, self.__generic_error_message, passing_data)
            
    def set_passing_data_advanced_air_yards(self, passing_data):
        """Sets the advanced passing data for the player in the object

        Args:
            passing_data (dict): Passing data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__passing_advanced_air_yards, PassingAdvancedAirYards)):
            self.__passing_advanced_air_yards.parse_passing_data(passing_data)
        else:
            self.__passing_advanced_air_yards = PassingAdvancedAirYards(self.__logger, self.season_games, self.__generic_error_message, passing_data)
            
    def set_passing_data_advanced_accuracy(self, passing_data):
        """Sets the advanced passing data for the player in the object

        Args:
            passing_data (dict): Passing data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__passing_advanced_accuracy, PassingAdvancedAccuracy)):
            self.__passing_advanced_accuracy.parse_passing_data(passing_data)
        else:
            self.__passing_advanced_accuracy = PassingAdvancedAccuracy(self.__logger, self.season_games, self.__generic_error_message, passing_data)
            
    def set_passing_data_advanced_pressure(self, passing_data):
        """Sets the advanced passing data for the player in the object

        Args:
            passing_data (dict): Passing data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__passing_advanced_pressure, PassingAdvancedPressure)):
            self.__passing_advanced_pressure.parse_passing_data(passing_data)
        else:
            self.__passing_advanced_pressure = PassingAdvancedPressure(self.__logger, self.season_games, self.__generic_error_message, passing_data)
            
    def set_passing_data_advanced_play_type(self, passing_data):
        """Sets the advanced passing data for the player in the object

        Args:
            passing_data (dict): Passing data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__passing_advanced_play_type, PassingAdvancedPlayType)):
            self.__passing_advanced_play_type.parse_passing_data(passing_data)
        else:
            self.__passing_advanced_play_type = PassingAdvancedPlayType(self.__logger, self.season_games, self.__generic_error_message, passing_data)
            
    def set_passing_data_adjusted(self, passing_data):
        """Sets the adjusted passing data for the player in the object

        Args:
            passing_data (dict): Passing data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__passing_adjusted, PassingAdjusted)):
            self.__passing_adjusted.parse_passing_data(passing_data)
        else:
            self.__passing_adjusted = PassingAdjusted(self.__logger, self.season_games, self.__generic_error_message, passing_data)
            
    def get_passing_data_regular_season(self):
        """Returns the object for passing regular season stats

        Returns:
            PassingRegularSeason: Object containing passing data for the regular season
        """
        return self.__passing_regular_season_stats
    
    def get_passing_data_playoffs(self):
        """Returns the object for passing playoff stats

        Returns:
            PassingPlayoffs: Object containing passing data for the playoffs
        """
        return self.__passing_playoffs_stats
    
    def get_passing_data_advanced_air_yards(self):
        """Returns the object for passing advanced air yards

        Returns:
            PassingAdvancedAirYards: Object containing advanced air yards passing data
        """
        return self.__passing_advanced_air_yards
    
    def get_passing_data_advanced_accuracy(self):
        """Returns the object for passing advanced accuracy

        Returns:
            PassingAdvancedAccuracy: Object containing advanced accuracy passing data
        """
        return self.__passing_advanced_accuracy
    
    def get_passing_data_advanced_pressure(self):
        """Returns the object for passing advanced pressure

        Returns:
            PassingAdvancedPressure: Object containing advanced pressure passing data
        """
        return self.__passing_advanced_pressure
    
    def get_passing_data_advanced_play_type(self):
        """Returns the object for passing advanced play_type

        Returns:
            PassingAdvancedPlayType: Object containing advanced play_type passing data
        """
        return self.__passing_advanced_play_type
    
    def get_passing_data_adjusted(self):
        """Returns the object for passing adjusted

        Returns:
            PassingAdjusted: Object containing adjusted passing data
        """
        return self.__passing_adjusted


if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")