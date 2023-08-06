import pandas as pd
import os
import sys

passing_directory = os.path.dirname(__file__)
position_directory = os.path.dirname(passing_directory)
pfr_directory = os.path.dirname(position_directory)

sys.path.insert(0, pfr_directory)

from PFRWebScraper.Includes.PositionAbstract import PositionAbstract

class ScoringRegularSeason():
    def __init__(self, logger, season_games, generic_error_message, scoring_data):
        self.__logger = logger
            
        self.season_games = season_games
        self.__generic_error_message = generic_error_message
        self.__scoring_regular_season_stats = pd.DataFrame()
        self.__year = 0
        
        self.parse_scoring_data(scoring_data)
        
    def parse_scoring_data(self, scoring_data):
        """Sets the scoring data for the regular season in the object

        Args:
            scoring_data (dict): Scoring data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        self.__scoring_regular_season_stats = PositionAbstract().set_or_update_dataframe(self.__scoring_regular_season_stats, scoring_data)
        
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
        return list(self.__scoring_regular_season_stats['year'].values)
    
    def get_dataframe_of_stats(self):
        """Returns a dataframe of all of the stats

        Returns:
            Dataframe: Dataframe containing all the stats
        """
        return self.__scoring_regular_season_stats
    
    def get_dictionary_of_stats(self):
        """Converts the dataframe to a dictionary of dictionaries and returns it.
        Each row of data becomes its own dictionary within the dictionary.

        Returns:
            dict: Dictionary of dictionaries containing all the stats
        """
        return self.__scoring_regular_season_stats.to_dict('index')
    
    def get_age(self):
        """Get method for age 

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['age'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['age'].values[0])
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
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['team_abbreviation'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['team_abbreviation'].values[0])
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
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['position'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['position'].values[0])
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
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['uniform_number'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['uniform_number'].values[0])
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
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['games_played'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['games_played'].values[0])
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
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['games_started'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['games_started'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for games started.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_touchdowns(self):
        """Get method for rushing touchdowns

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['rushtd'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['rushtd'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_receiving_touchdowns(self):
        """Get method for receiving touchdowns

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['rectd'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['rectd'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for receiving touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_punt_return_touchdowns(self):
        """Get method for punt return touchdowns

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['prtd'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['prtd'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for punt return touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_kick_return_touchdowns(self):
        """Get method for kick return touchdowns

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['krtd'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['krtd'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for kick return touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_fumble_recovery_touchdowns(self):
        """Get method for fumble recovery touchdowns

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['frtd'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['frtd'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for fumble recovery touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_interception_touchdowns(self):
        """Get method for interception touchdowns

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['ditd'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['ditd'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for interception touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_miscellaneous_touchdowns(self):
        """Get method for miscellaneous touchdowns.  Blocked Kicks or Missed Field Goal Attempts

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['otd'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['otd'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for miscellaneous touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_total_touchdowns(self):
        """Get method for total touchdowns

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['alltd'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['alltd'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for miscellaneous touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_two_point_conversions_made(self):
        """Get method for two point conversions made

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['two_pt_md'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['two_pt_md'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for two point conversions made.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_two_point_conversions_attempted(self):
        """Get method for two point conversions attempted

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['two_pt_att'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['two_pt_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for two point conversions attempted.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_defensive_two_point_conversions(self):
        """Get method for defensive two point conversions

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['def_two_pt'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['def_two_pt'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for defensive two point conversions.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_extra_points_made(self):
        """Get method for extra points made

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['xpm'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['xpm'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for extra points made.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_extra_points_attempted(self):
        """Get method for extra points attempted

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['xpa'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['xpa'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for extra points attempted.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_field_goals_made(self):
        """Get method for field goals made

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['fgm'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['fgm'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for field goals made.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_field_goals_attempted(self):
        """Get method for field goals attempted

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['fga'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['fga'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for field goals attempted.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_safeties_scored(self):
        """Get method for safeties scored by player or team

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['safety_md'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['safety_md'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for safeties scored by player or team.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_total_points_scored(self):
        """Get method for total points scored

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['scoring'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['scoring'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for total points scored.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_points_per_game(self):
        """Get method for points per game

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['points_per_g'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__scoring_regular_season_stats[self.__scoring_regular_season_stats['year'] == self.__year]['points_per_g'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for points per game.\nYear:{0}\n\nException:{1}".format(self.__year, e))
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