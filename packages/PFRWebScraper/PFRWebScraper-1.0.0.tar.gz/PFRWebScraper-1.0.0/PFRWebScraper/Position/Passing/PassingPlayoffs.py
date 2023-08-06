import pandas as pd
import os
import sys

passing_directory = os.path.dirname(__file__)
position_directory = os.path.dirname(passing_directory)
pfr_directory = os.path.dirname(position_directory)

sys.path.insert(0, pfr_directory)

from PFRWebScraper.Includes.PositionAbstract import PositionAbstract

class PassingPlayoffs():
    def __init__(self, logger, season_games, generic_error_message, passing_data):
        self.__logger = logger
            
        self.season_games = season_games
        self.__generic_error_message = generic_error_message
        self.__passing_playoffs_stats = pd.DataFrame()
        self.__year = 0
        
        self.parse_passing_data(passing_data)
    
    def parse_passing_data(self, passing_data):
        """Sets the passing data for the regular season in the object

        Args:
            passing_data (dict): Passing data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        self.__passing_playoffs_stats = PositionAbstract().set_or_update_dataframe(self.__passing_playoffs_stats, passing_data)
        
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
        return list(self.__passing_playoffs_stats['year'].values)
    
    def get_dataframe_of_stats(self):
        """Returns a dataframe of all of the stats

        Returns:
            Dataframe: Dataframe containing all the stats
        """
        return self.__passing_playoffs_stats
    
    def get_dictionary_of_stats(self):
        """Converts the dataframe to a dictionary of dictionaries and returns it.
        Each row of data becomes its own dictionary within the dictionary.

        Returns:
            dict: Dictionary of dictionaries containing all the stats
        """
        return self.__passing_playoffs_stats.to_dict('index')
    
    def get_age(self):
        """Get method for age

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['age'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['age'].values[0])
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
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['team_abbreviation'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['team_abbreviation'].values[0])
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
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['position'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['position'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for position.\nYear:{0}\n\nException:{1}".format(self.__year, e))
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
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['games_played'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['games_played'].values[0])
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
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['games_started'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['games_started'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for games started.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_wins(self):
        """Get method for games won

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['wins'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['wins'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for games won.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_losses(self):
        """Get method for games lost

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['losses'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['losses'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for games lost.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_ties(self):
        """Get method for games tied

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['ties'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['ties'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for games tied.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_pass_completions(self):
        """Get method for passes completed

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_cmp'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_cmp'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passes completed.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_pass_attempts(self):
        """Get method for passes attempted

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_att'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passes attempted.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_pass_completion_percentage(self):
        """Get method for percentage of passes completed

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_cmp_perc'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_cmp_perc'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for percentage of passes completed.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_yards(self):
        """Get method for yards gained by passing

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_yds'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for yards gained by passing.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_touchdowns(self):
        """Get method for passing towndowns

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_td'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_td'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_touchdown_percentage(self):
        """Get method for Percentage of Touchdowns Thrown when Attempting to Pass

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_td_perc'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_td_perc'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for Percentage of Touchdowns Thrown when Attempting to Pass.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_interceptions_thrown(self):
        """Get method for Interceptions thrown

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_int'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_int'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for interceptions thrown.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_of_interceptions_thrown(self):
        """Get method for Percentage of Times Intercepted when Attempting to Pass

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_int_perc'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_int_perc'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for Times Intercepted when Attempting to Pass.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_first_downs(self):
        """Get method for first downs passing

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_first_down'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_first_down'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for first downs passing.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_longest_pass(self):
        """Get method for longest pass

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_long'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_long'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for longest pass.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_yards_per_attempt(self):
        """Get method for Yards gained per pass attempt

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_yds_per_att'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_yds_per_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for Yards gained per pass attempt.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_adjusted_passing_yards_per_attempt(self):
        """Get method for Adjusted Yards gained per pass attempt. (Passing Yards + 20 * Passing TD - 45 * Interceptions) / (Passes Attempted)

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_adj_yds_per_att'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_adj_yds_per_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for Adjusted Yards gained per pass attempt.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_yards_per_completion(self):
        """Get method for Yards gained per pass completion. (Passing Yards) / (Passes Completed)

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_yds_per_cmp'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_yds_per_cmp'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for Yards gained per pass completion.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_yards_per_game(self):
        """Get method for Yards gained per game played

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_yds_per_g'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_yds_per_g'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for Yards gained per game played.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passer_rating(self):
        """Get method for Quarterback Rating

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_rating'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_rating'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for Quarterback Rating.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passer_sacked(self):
        """Get method for times sacked

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_sacked'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_sacked'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for times sacked.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_yards_lost_from_sacks(self):
        """Get method for Yards lost due to sacks

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_sacked_yds'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_sacked_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for Yards lost due to sacks.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_of_plays_sacked(self):
        """Get method for Percentage of Time Sacked when Attempting to Pass: Times Sacked / (Passes Attempted + Times Sacked)

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_sacked_perc'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_sacked_perc'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for Percentage of Time Sacked when Attempting to Pass.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_net_passing_yards_per_attempt(self):
        """Get method for Net Yards gained per pass attempt: (Passing Yards - Sack Yards) / (Passes Attempted + Times Sacked)

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_net_yds_per_att'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_net_yds_per_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for Net Yards gained per pass attempt.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_adjusted_net_passing_yards_per_attempt(self):
        """Get method for Adjusted Net Yards per Pass Attempt: (Passing Yards - Sack Yards + (20 * Passing TD) - (45 * Interceptions)) / (Passes Attempted + Times Sacked)

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_adj_net_yds_per_att'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['pass_adj_net_yds_per_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for Adjusted Net Yards per Pass Attempt.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_fourth_quarter_comebacks(self):
        """Get method for Comebacks led by quarterback. Must be an offensive scoring drive in the 4th quarter, with the team trailing by one score, though not necessarily a drive to take the lead. Only games ending in a win or tie are included.

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['4Q_comebacks'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['4Q_comebacks'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for Comebacks led by quarterback.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_game_winning_drives(self):
        """Get method for Game-winning drives led by quarterback. Must be an offensive scoring drive in the 4th quarter or overtime that puts the winning team ahead for the last time.

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['game_winning_drives'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_playoffs_stats[self.__passing_playoffs_stats['year'] == self.__year]['game_winning_drives'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for game winning drives.\nYear:{0}\n\nException:{1}".format(self.__year, e))
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