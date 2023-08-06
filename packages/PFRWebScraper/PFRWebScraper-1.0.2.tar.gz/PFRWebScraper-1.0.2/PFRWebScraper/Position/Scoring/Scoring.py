from PFRWebScraper.Position.Scoring.ScoringRegularSeason import ScoringRegularSeason
from PFRWebScraper.Position.Scoring.ScoringPlayoffs import ScoringPlayoffs

class ScoringData():
    def __init__(self, logger=None, season_games=17):
        """Sets initial values for use within an object

        Args:
            logger (Logger): Python Default Logger Class
            season_games (int, optional): Number of games in an NFL season. Defaults to 17.
        """
        self.__logger = logger
            
        self.__generic_error_message = "An error has occurred please check the log for more information.\nError:"
        self.season_games = season_games
        
        self.__scoring_regular_season_stats = None
        self.__scoring_playoffs_stats = None
            
    def set_scoring_data_regular_season(self, scoring_data):
        """Sets the scoring data for the regular season in the object

        Args:
            scoring_data (dict): Scoring data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__scoring_regular_season_stats, ScoringRegularSeason)):
            self.__scoring_regular_season_stats.parse_scoring_data(scoring_data)
        else:
            self.__scoring_regular_season_stats = ScoringRegularSeason(self.__logger, self.season_games, self.__generic_error_message, scoring_data)
                
    def set_scoring_data_playoffs(self, scoring_data):
        """Sets the scoring data for the playoffs in the object

        Args:
            scoring_data (dict): Scoring data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__scoring_playoffs_stats, ScoringPlayoffs)):
            self.__scoring_playoffs_stats.parse_scoring_data(scoring_data)
        else:
            self.__scoring_playoffs_stats = ScoringPlayoffs(self.__logger, self.season_games, self.__generic_error_message, scoring_data)
            
    def get_scoring_data_regular_season(self):
        """Returns the object for scoring regular season stats

        Returns:
            ScoringRegularSeason: Object containing scoring data for the regular season
        """
        return self.__scoring_regular_season_stats
    
    def get_scoring_data_playoffs(self):
        """Returns the object for scoring playoff stats

        Returns:
            ScoringPlayoffs: Object containing scoring data for the playoffs
        """
        return self.__scoring_playoffs_stats
    
    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")