from PFRWebScraper.Position.DefenseAndFumbles.DefenseAndFumblesRegularSeason import DefenseAndFumblesRegularSeason
from PFRWebScraper.Position.DefenseAndFumbles.DefenseAndFumblesPlayoffs import DefenseAndFumblesPlayoffs

class DefenseAndFumblesData():
    def __init__(self, logger=None, season_games=17):
        """Sets initial values for use within an object

        Args:
            logger (Logger): Python Default Logger Class
            season_games (int, optional): Number of games in an NFL season. Defaults to 17.
        """
        self.__logger = logger
            
        self.__generic_error_message = "An error has occurred please check the log for more information.\nError:"
        self.season_games = season_games
        
        self.__defense_and_fumbles_regular_season_stats = None
        self.__defense_and_fumbles_playoffs_stats = None
            
    def set_defense_and_fumbles_data_regular_season(self, defense_and_fumbles_data):
        """Sets the defense and fumbles data for the regular season in the object

        Args:
            defense_and_fumbles_data (dict): Defense and fumbles data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__defense_and_fumbles_regular_season_stats, DefenseAndFumblesRegularSeason)):
            self.__defense_and_fumbles_regular_season_stats.parse_defense_and_fumbles_data(defense_and_fumbles_data)
        else:
            self.__defense_and_fumbles_regular_season_stats = DefenseAndFumblesRegularSeason(self.__logger, self.season_games, self.__generic_error_message, defense_and_fumbles_data)
                
    def set_defense_and_fumbles_data_playoffs(self, defense_and_fumbles_data):
        """Sets the defense and fumbles data for the playoffs in the object

        Args:
            defense_and_fumbles_data (dict): Defense and fumbles data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__defense_and_fumbles_playoffs_stats, DefenseAndFumblesPlayoffs)):
            self.__defense_and_fumbles_playoffs_stats.parse_defense_and_fumbles_data(defense_and_fumbles_data)
        else:
            self.__defense_and_fumbles_playoffs_stats = DefenseAndFumblesPlayoffs(self.__logger, self.season_games, self.__generic_error_message, defense_and_fumbles_data)
            
    def get_defense_and_fumbles_data_regular_season(self):
        """Returns the object for defense and fumbles regular season stats

        Returns:
            DefenseAndFumblesRegularSeason: Object containing defense and fumbles data for the regular season
        """
        return self.__defense_and_fumbles_regular_season_stats
    
    def get_defense_and_fumbles_data_playoffs(self):
        """Returns the object for defense and fumbles playoff stats

        Returns:
            DefenseAndFumblesPlayoffs: Object containing defense and fumbles data for the playoffs
        """
        return self.__defense_and_fumbles_playoffs_stats
    
    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")