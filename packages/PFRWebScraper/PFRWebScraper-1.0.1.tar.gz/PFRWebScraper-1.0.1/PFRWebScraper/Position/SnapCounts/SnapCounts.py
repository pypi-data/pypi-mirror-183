from PFRWebScraper.Position.SnapCounts.SnapCountsRegularSeason import SnapCountsRegularSeason

class SnapCountsData():
    def __init__(self, logger=None, season_games=17):
        """Sets initial values for use within an object

        Args:
            logger (Logger): Python Default Logger Class
            season_games (int, optional): Number of games in an NFL season. Defaults to 17.
        """
        self.__logger = logger
            
        self.__generic_error_message = "An error has occurred please check the log for more information.\nError:"
        self.season_games = season_games
        
        self.__snap_counts_regular_season = None
        
    def set_snap_counts_regular_season(self, snap_counts_data):
        """Sets the snap counts data for the regular season in the object

        Args:
            snap_counts_data (dict): Snap Counts data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        if (isinstance(self.__snap_counts_regular_season, SnapCountsRegularSeason)):
            self.__snap_counts_regular_season.parse_snap_counts_data(snap_counts_data)
        else:
            self.__snap_counts_regular_season = SnapCountsRegularSeason(self.__logger, self.season_games, self.__generic_error_message, snap_counts_data)
            
    def get_snap_counts_data_regular_season(self):
        """Returns the object for snap counts regular season stats

        Returns:
            SnapCountsRegularSeason: Object containing snap counts data for the regular season
        """
        return self.__snap_counts_regular_season
    

if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")