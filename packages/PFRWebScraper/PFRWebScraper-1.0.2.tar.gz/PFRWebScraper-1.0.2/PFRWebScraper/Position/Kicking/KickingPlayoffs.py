import pandas as pd
import os
import sys

passing_directory = os.path.dirname(__file__)
position_directory = os.path.dirname(passing_directory)
pfr_directory = os.path.dirname(position_directory)

sys.path.insert(0, pfr_directory)

from PFRWebScraper.Includes.PositionAbstract import PositionAbstract

class KickingPlayoffs():
    def __init__(self, logger, season_games, generic_error_message, kicking_data):
        self.__logger = logger
            
        self.season_games = season_games
        self.__generic_error_message = generic_error_message
        self.__kicking_playoff_stats = pd.DataFrame()
        self.__year = 0
        
        self.parse_kicking_data(kicking_data)
        
    def parse_kicking_data(self, kicking_data):
        """Sets the kicking data for the playoffs in the object

        Args:
            kicking_data (dict): Kicking data for the playoffs obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        self.__kicking_playoff_stats = PositionAbstract().set_or_update_dataframe(self.__kicking_playoff_stats, kicking_data)
        
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
        return list(self.__kicking_playoff_stats['year'].values)
    
    def get_dataframe_of_stats(self):
        """Returns a dataframe of all of the stats

        Returns:
            Dataframe: Dataframe containing all the stats
        """
        return self.__kicking_playoff_stats
    
    def get_dictionary_of_stats(self):
        """Converts the dataframe to a dictionary of dictionaries and returns it.
        Each row of data becomes its own dictionary within the dictionary.

        Returns:
            dict: Dictionary of dictionaries containing all the stats
        """
        return self.__kicking_playoff_stats.to_dict('index')
    
    def get_age(self):
        """Get method for age 

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['age'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['age'].values[0])
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
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['team_abbreviation'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['team_abbreviation'].values[0])
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
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['position'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['position'].values[0])
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
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['games_played'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['games_played'].values[0])
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
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['games_started'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['games_started'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for games started.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_field_goals_attempted_0_19(self):
        """Get method for field goals attempted from 0 - 19 yards

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fga1'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fga1'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for field goals attempted from 0 - 19 yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_field_goals_made_0_19(self):
        """Get method for field goals made from 0 - 19 yards

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fgm1'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fgm1'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for field goals made from 0 - 19 yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_field_goals_attempted_20_29(self):
        """Get method for field goals attempted from 20 - 29 yards

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fga2'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fga2'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for field goals attempted from 20 - 29 yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_field_goals_made_20_29(self):
        """Get method for field goals made from 20 - 29 yards

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fgm2'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fgm2'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for field goals made from 20 - 29 yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_field_goals_attempted_30_39(self):
        """Get method for field goals attempted from 30 - 39 yards

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fga3'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fga3'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for field goals attempted from 30 - 39 yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_field_goals_made_30_39(self):
        """Get method for field goals made from 30 - 39 yards

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fgm3'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fgm3'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for field goals made from 30 - 39 yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_field_goals_attempted_40_49(self):
        """Get method for field goals attempted from 40 - 49 yards

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fga4'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fga4'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for field goals attempted from 40 - 49 yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_field_goals_made_40_49(self):
        """Get method for field goals made from 40 - 49 yards

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fgm4'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fgm4'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for field goals made from 40 - 49 yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
    
    def get_field_goals_attempted_50_or_more(self):
        """Get method for field goals attempted from 50 or more yards

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fga5'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fga5'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for field goals attempted from 50 or more yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_field_goals_made_50_or_more(self):
        """Get method for field goals made from 50 or more yards

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fgm5'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fgm5'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for field goals made from 50 or more yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_all_field_goals_attempted(self):
        """Get method for all field goals attempted from anywhere

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fga'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fga'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for all field goals attempted from anywhere.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_all_field_goals_made(self):
        """Get method for all field goals made from anywhere

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fgm'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fgm'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for all field goals made from anywhere.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))

    def get_percentage_of_field_goal_made(self):
        """Get method for percentage of field goals made

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fg_perc'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['fg_perc'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for percentage of field goals made.\nYear:{0}\n\nException:{1}".format(self.__year, e))
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
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['xpa'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['xpa'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for extra points attempted.\nYear:{0}\n\nException:{1}".format(self.__year, e))
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
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['xpm'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['xpm'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for extra points made.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_of_extra_points_made(self):
        """Get method for percentage of extra points made

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['xp_perc'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['xp_perc'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for percentage of extra points made.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_kickoffs(self):
        """Get method for kickoff count

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['kickoff'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['kickoff'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for kickoff count.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_kickoff_yards(self):
        """Get method for kickoff yards

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['kickoff_yds'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['kickoff_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for kickoff yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_kickoff_touchbacks(self):
        """Get method for kickoff touchbacks

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['kickoff_tb'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['kickoff_tb'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for kickoff touchbacks.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_of_kickoff_touchbacks(self):
        """Get method for percentage of kickoff touchbacks

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['kickoff_tb_pct'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['kickoff_tb_pct'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for percentage of kickoff touchbacks.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_kickoff_average_yardage(self):
        """Get method for percentage of kickoff average yardage

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['kickoff_yds_avg'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__kicking_playoff_stats[self.__kicking_playoff_stats['year'] == self.__year]['kickoff_yds_avg'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for percentage of kickoff average yardage.\nYear:{0}\n\nException:{1}".format(self.__year, e))
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