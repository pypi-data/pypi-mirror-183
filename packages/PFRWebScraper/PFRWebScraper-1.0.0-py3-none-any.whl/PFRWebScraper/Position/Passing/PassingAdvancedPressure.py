import pandas as pd
import os
import sys

passing_directory = os.path.dirname(__file__)
position_directory = os.path.dirname(passing_directory)
pfr_directory = os.path.dirname(position_directory)

sys.path.insert(0, pfr_directory)

from PFRWebScraper.Includes.PositionAbstract import PositionAbstract

class PassingAdvancedPressure():
    def __init__(self, logger, season_games, generic_error_message, passing_data):
        self.__logger = logger
            
        self.season_games = season_games
        self.__generic_error_message = generic_error_message
        self.__passing_stats = pd.DataFrame()
        self.__year = 0
        
        self.parse_passing_data(passing_data)
    
    def parse_passing_data(self, passing_data):
        """Sets the advanced passing data in the object

        Args:
            passing_data (dict): Passing data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        self.__passing_stats = PositionAbstract().set_or_update_dataframe(self.__passing_stats, passing_data)
        
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
        return list(self.__passing_stats['year'].values)
    
    def get_dataframe_of_stats(self):
        """Returns a dataframe of all of the stats

        Returns:
            Dataframe: Dataframe containing all the stats
        """
        return self.__passing_stats
    
    def get_dictionary_of_stats(self):
        """Converts the dataframe to a dictionary of dictionaries and returns it.
        Each row of data becomes its own dictionary within the dictionary.

        Returns:
            dict: Dictionary of dictionaries containing all the stats
        """
        return self.__passing_stats.to_dict('index')
    
    def get_age(self):
        """Get method for age

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['age'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_stats[self.__passing_stats['year'] == self.__year]['age'].values[0])
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
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['team_abbreviation'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__passing_stats[self.__passing_stats['year'] == self.__year]['team_abbreviation'].values[0])
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
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['position'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__passing_stats[self.__passing_stats['year'] == self.__year]['position'].values[0])
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
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['uniform_number'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_stats[self.__passing_stats['year'] == self.__year]['uniform_number'].values[0])
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
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['games_played'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_stats[self.__passing_stats['year'] == self.__year]['games_played'].values[0])
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
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['games_started'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_stats[self.__passing_stats['year'] == self.__year]['games_started'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for games started.\nYear:{0}\n\nException:{1}".format(self.__year, e))
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
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_cmp'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_cmp'].values[0])
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
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_att'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passes attempted.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_yards(self):
        """Get method for Yards Gained by Passing

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_yds'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passer_sacked(self):
        """Get method for the number of times the passer was sacked

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_sacked'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_sacked'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for the number of times the passer was sacked.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_time_in_pocket(self):
        """Get method for Average time the QB had in the pocket between the snap and throwing the ball or pressure collapses the pocket, in seconds

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['pocket_time'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__passing_stats[self.__passing_stats['year'] == self.__year]['pocket_time'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for the average_time_in_pocket.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_times_blitzed(self):
        """Get method for times blitzed

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_blitzed'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_blitzed'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for times blitzed.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_times_hurried(self):
        """Get method for times hurried

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_hurried'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_hurried'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for times hurried.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_times_hit_while_passing(self):
        """Get method for Times hit as a QB while passing

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_hits'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_hits'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for Times hit as a QB while passing.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_times_passer_was_pressured(self):
        """Get method for Times the QB was pressured (hurries + hits+ times sacked)

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_pressured'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_pressured'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for times the QB was pressured.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_of_times_passer_was_pressured(self):
        """Get method for percentage of Times pressured per dropback

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_pressured_pct'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__passing_stats[self.__passing_stats['year'] == self.__year]['pass_pressured_pct'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for percentage of times pressured per dropback.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_times_passer_scrambled(self):
        """Get method for Scrambles (rushes on plays designed as passes)

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['rush_scrambles'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__passing_stats[self.__passing_stats['year'] == self.__year]['rush_scrambles'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for scrambles.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_yards_per_scramble_attempt(self):
        """Get method for yards per scramble attempt

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__passing_stats[self.__passing_stats['year'] == self.__year]['rush_scrambles_yds_per_att'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__passing_stats[self.__passing_stats['year'] == self.__year]['rush_scrambles_yds_per_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for yards per scramble attempt.\nYear:{0}\n\nException:{1}".format(self.__year, e))
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