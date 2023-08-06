import pandas as pd
import os
import sys

passing_directory = os.path.dirname(__file__)
position_directory = os.path.dirname(passing_directory)
pfr_directory = os.path.dirname(position_directory)

sys.path.insert(0, pfr_directory)

from PFRWebScraper.Includes.PositionAbstract import PositionAbstract

class RushingReceivingRegularSeason():
    def __init__(self, logger, season_games, generic_error_message, rushing_receiving_data):
        self.__logger = logger
            
        self.season_games = season_games
        self.__generic_error_message = generic_error_message
        self.__rushing_receiving_regular_season_stats = pd.DataFrame()
        self.__year = 0
        
        self.parse_rushing_receiving_data(rushing_receiving_data)
        
    def parse_rushing_receiving_data(self, rushing_receiving_data):
        """Sets the rushing and receiving data for the regular season in the object

        Args:
            rushing_receiving_data (dict): Rushing and Receiving data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        self.__rushing_receiving_regular_season_stats = PositionAbstract().set_or_update_dataframe(self.__rushing_receiving_regular_season_stats, rushing_receiving_data)
        
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
        return list(self.__rushing_receiving_regular_season_stats['year'].values)
    
    def get_dataframe_of_stats(self):
        """Returns a dataframe of all of the stats

        Returns:
            Dataframe: Dataframe containing all the stats
        """
        return self.__rushing_receiving_regular_season_stats
    
    def get_dictionary_of_stats(self):
        """Converts the dataframe to a dictionary of dictionaries and returns it.
        Each row of data becomes its own dictionary within the dictionary.

        Returns:
            dict: Dictionary of dictionaries containing all the stats
        """
        return self.__rushing_receiving_regular_season_stats.to_dict('index')
    
    def get_age(self):
        """Get method for age 

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['age'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['age'].values[0])
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
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['team_abbreviation'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['team_abbreviation'].values[0])
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
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['position'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['position'].values[0])
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
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['uniform_number'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['uniform_number'].values[0])
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
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['games_played'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['games_played'].values[0])
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
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['games_started'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['games_started'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for games started.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_pass_targets(self):
        """Get method for number of times the receiver was targeted by the passer

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['targets'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['targets'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for times the receiver was targeted by the passer.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
    
    def get_receptions(self):
        """Get method for number of receptions

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for number of receptions.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_yards_from_receptions(self):
        """Get method for yards obtained from receiving the ball

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_yds'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for yards obtained from receiving the ball.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_yards_per_receptions(self):
        """Get method for yards obtained per reception

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_yds_per_rec'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_yds_per_rec'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for yards obtained per reception.\nYear:{0}\n\nException:{1}".format(self.__year, e))
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
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_td'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_td'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for receiving touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_first_downs_from_receptions(self):
        """Get method for first downs obtained from receiving the ball

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_first_down'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_first_down'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for first downs obtained from receiving the ball.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_longest_reception(self):
        """Get method for longest reception

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_long'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_long'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for longest reception.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
    
    def get_receptions_per_game(self):
        """Get method for receptions per game

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_per_g'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_per_g'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for receptions per game.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_reception_yards_per_game(self):
        """Get method for reception yards per game

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_yds_per_g'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_yds_per_g'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for receptions yards per game.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_catch_percentage(self):
        """Get method for catch percentage.  Receptions divided by targets.

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['catch_pct'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['catch_pct'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for catch percentage.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_reception_yards_per_target(self):
        """Get method for reception yards per target

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_yds_per_tgt'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rec_yds_per_tgt'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for receptions yards per target.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_attempts(self):
        """Get method for rushing attempts

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_att'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing attempts.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_yards(self):
        """Get method for rushing yards gained

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_yds'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing yards gained.\nYear:{0}\n\nException:{1}".format(self.__year, e))
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
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_td'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_td'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_first_downs_from_rushing(self):
        """Get method for first downs from rushing

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_first_down'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_first_down'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for first downs from rushing.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_longest_rush(self):
        """Get method for longest rush

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_long'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_long'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for longest rush.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_yards_per_attempt(self):
        """Get method for rushing yards per attempt

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_yds_per_att'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_yds_per_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing yards per attempt.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_yards_per_game(self):
        """Get method for rushing yards per game

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_yds_per_g'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_yds_per_g'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing yards per game.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_attempts_per_game(self):
        """Get method for rushing attempts per game

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_att_per_g'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_att_per_g'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing attempts per game.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_touches(self):
        """Get method for touches.  Rushing attempts + Receiving attempts

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['touches'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['touches'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for touches.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_yards_per_touch(self):
        """Get method for yards per touch

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['yds_per_touch'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['yds_per_touch'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for yards per touch.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_yards_from_scrimmage(self):
        """Get method for yards from scrimmage

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['yds_from_scrimmage'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['yds_from_scrimmage'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for yards from scrimmage.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_total_touchdowns(self):
        """Get method for total touchdowns. Rushing touchdowns + Receiving touchdowns

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_receive_td'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['rush_receive_td'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for total touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_number_of_times_fumbled(self):
        """Get method for number of times fumbled. Total fumbles both lost and recovered

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['fumbles'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['fumbles'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for number of times fumbled.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_approximate_value(self):
        """Get method for approximate value. This is pro football references attempt to assign a single number to every player

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['approximate_value'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_regular_season_stats[self.__rushing_receiving_regular_season_stats['year'] == self.__year]['approximate_value'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for approximate value.\nYear:{0}\n\nException:{1}".format(self.__year, e))
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