import pandas as pd
import os
import sys

passing_directory = os.path.dirname(__file__)
position_directory = os.path.dirname(passing_directory)
pfr_directory = os.path.dirname(position_directory)

sys.path.insert(0, pfr_directory)

from PFRWebScraper.Includes.PositionAbstract import PositionAbstract

class SnapCountsRegularSeason():
    def __init__(self, logger, season_games, generic_error_message, snap_counts_data):
        self.__logger = logger
            
        self.season_games = season_games
        self.__generic_error_message = generic_error_message
        self.__snap_counts_regular_season_stats = pd.DataFrame()
        self.__year = 0
        
        self.parse_snap_counts_data(snap_counts_data)
        
    def parse_snap_counts_data(self, snap_counts_data):
        """Sets the snap counts data for the regular season in the object

        Args:
            snap_counts_data (dict): Snap Counts data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        self.__snap_counts_regular_season_stats = PositionAbstract().set_or_update_dataframe(self.__snap_counts_regular_season_stats, snap_counts_data)
        
    def set_reference_year(self, value):
        """Sets the year as a point of reference for the object

        Args:
            value (int/str): The value is passes as either a string or int.
        
        Raises:
            ValueError: Value cannot be cast
        """
        if(isinstance(value, int)):
            self.__year = value
        else:
            try:
                self.__year = int(value)
            except ValueError as e:
                self.__logging("Invalid value for year.\nValue:{0}\nError:{1}".format(value, e))
                raise ValueError("{0}{1}".format(self.__generic_error_message, e))
            
    def get_list_of_years(self):
        """Returns a list of the years that data is present for

        Returns:
            list: List of years with the integer data type
        """
        return list(self.__snap_counts_regular_season_stats['year'].values)
    
    def get_dataframe_of_stats(self):
        """Returns a dataframe of all of the stats

        Returns:
            Dataframe: Dataframe containing all the stats
        """
        return self.__snap_counts_regular_season_stats
    
    def get_dictionary_of_stats(self):
        """Converts the dataframe to a dictionary of dictionaries and returns it.
        Each row of data becomes its own dictionary within the dictionary.

        Returns:
            dict: Dictionary of dictionaries containing all the stats
        """
        return self.__snap_counts_regular_season_stats.to_dict('index')
    
    def get_age(self):
        """Get method for age 

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['age'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['age'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for age.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_team_abbreviation(self):
        """Get method for team's abbreviation 

        Returns:
            array/str: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['team_abbreviation'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['team_abbreviation'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for team's abbreviation.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_position(self):
        """Get method for position 

        Returns:
            array/str: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['position'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['position'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for position.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_uniform_number(self):
        """Get method for uniform number 

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['uniform_number'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['uniform_number'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for uniform number.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_games_played(self):
        """Get method for games played

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['games_played'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['games_played'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for games played.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_games_started(self):
        """Get method for games started

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['games_started'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['games_started'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for games started.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_offensive_snaps(self):
        """Get method for the number of offensive snaps

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['offense'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['offense'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for the number of offensive snaps.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_offensive_snaps(self):
        """Get method for the percentage of offensive snaps

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['off_pct'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['off_pct'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for the percentage of offensive snaps.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_defensive_snaps(self):
        """Get method for the number of defensive snaps

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['defense'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['defense'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for the number of defensive snaps.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_defensive_snaps(self):
        """Get method for the percentage of defensive snaps

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['def_pct'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['def_pct'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for the percentage of defensive snaps.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_special_teams_snaps(self):
        """Get method for the number of special teams snaps

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['special_teams'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['special_teams'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for the number of special teams snaps.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_special_teams_snaps(self):
        """Get method for the percentage of special teams snaps

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['st_pct'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__snap_counts_regular_season_stats[self.__snap_counts_regular_season_stats['year'] == self.__year]['st_pct'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for the percentage of special teams snaps.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def __logging(self, message):
        """Checks to see if there is a logger and if there is logs the message to the error log
        
        Args:
            message (str): Error message
        """
        if (self.__logger):
            self.__logger.error(message)


if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")