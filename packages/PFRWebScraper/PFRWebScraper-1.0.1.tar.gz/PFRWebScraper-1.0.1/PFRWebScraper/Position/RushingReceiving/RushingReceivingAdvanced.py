import pandas as pd
import os
import sys

passing_directory = os.path.dirname(__file__)
position_directory = os.path.dirname(passing_directory)
pfr_directory = os.path.dirname(position_directory)

sys.path.insert(0, pfr_directory)

from PFRWebScraper.Includes.PositionAbstract import PositionAbstract

class RushingReceivingAdvanced():
    def __init__(self, logger, season_games, generic_error_message, rushing_receiving_data):
        self.__logger = logger
            
        self.season_games = season_games
        self.__generic_error_message = generic_error_message
        self.__rushing_receiving_advanced_stats = pd.DataFrame()
        self.__year = 0
        
        self.parse_rushing_receiving_data(rushing_receiving_data)
        
    def parse_rushing_receiving_data(self, rushing_receiving_data):
        """Sets the rushing and receiving data for the regular season in the object

        Args:
            rushing_receiving_data (dict): Rushing and Receiving data for the regular season obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        self.__rushing_receiving_advanced_stats = PositionAbstract().set_or_update_dataframe(self.__rushing_receiving_advanced_stats, rushing_receiving_data)
        
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
        return list(self.__rushing_receiving_advanced_stats['year'].values)
    
    def get_dataframe_of_stats(self):
        """Returns a dataframe of all of the stats

        Returns:
            Dataframe: Dataframe containing all the stats
        """
        return self.__rushing_receiving_advanced_stats
    
    def get_dictionary_of_stats(self):
        """Converts the dataframe to a dictionary of dictionaries and returns it.
        Each row of data becomes its own dictionary within the dictionary.

        Returns:
            dict: Dictionary of dictionaries containing all the stats
        """
        return self.__rushing_receiving_advanced_stats.to_dict('index')
    
    def get_age(self):
        """Get method for age

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['age'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['age'].values[0])
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
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['team_abbreviation'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['team_abbreviation'].values[0])
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
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['position'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['position'].values[0])
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
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['uniform_number'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['uniform_number'].values[0])
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
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['games_played'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['games_played'].values[0])
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
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['games_started'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['games_started'].values[0])
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
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['targets'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['targets'].values[0])
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
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec'].values[0])
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
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_yds'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for yards obtained from receiving the ball.\nYear:{0}\n\nException:{1}".format(self.__year, e))
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
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_first_down'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_first_down'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for first downs obtained from receiving the ball.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
    
    def get_air_yards_for_reception(self):
        """Get method for total yards passes traveled in the air before being caught

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_air_yds'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_air_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for total yards passes traveled in the air before being caught.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_air_yards_per_reception(self):
        """Get method for yards before catch per reception

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_air_yds_per_rec'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_air_yds_per_rec'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for yards before catch per reception.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_yards_after_catch(self):
        """Get method for yards after catch

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_yac'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_yac'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for yards after catch.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_yards_after_catch_per_reception(self):
        """Get method for yards after catch per reception

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_yac_per_rec'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_yac_per_rec'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for yards after catch per reception.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_depth_of_target_when_targeted(self):
        """Get method for average depth of target when targeted, whether completed or not.

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_adot'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_adot'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average depth of target when targeted, whether completed or not.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_broken_tackles_after_reception(self):
        """Get method for broken tackles on receptions

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_broken_tackles'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_broken_tackles'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for broken tackles on receptions.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_receptions_per_broken_tackle(self):
        """Get method for receptions per broken tackle

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_broken_tackles_per_rec'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_broken_tackles_per_rec'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for receptions per broken tackle.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_dropped_passes(self):
        """Get method for dropped passes

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_drops'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_drops'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for dropped passes.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_dropped_passes_per_target(self):
        """Get method for percentage of dropped passes per target

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_drop_pct'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_drop_pct'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for dropped passes per target.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_interceptions_when_targeted(self):
        """Get method for interceptions on passes where targeted

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_target_int'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_target_int'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for interceptions on passes where targeted.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passer_rating_when_targeted(self):
        """Get method for passer rating on passes when targeted.

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_pass_rating'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rec_pass_rating'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passer rating on passes when targeted.\nYear:{0}\n\nException:{1}".format(self.__year, e))
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
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_att'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_att'].values[0])
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
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_yds'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_yds'].values[0])
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
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_td'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_td'].values[0])
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
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_first_down'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_first_down'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for first downs from rushing.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_yards_before_contact(self):
        """Get method for rushing yards before contact

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_yds_before_contact'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_yds_before_contact'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing yards before contact.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_yards_before_contact_per_attempt(self):
        """Get method for rushing yards before contact per rushing attempt

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_yds_bc_per_rush'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_yds_bc_per_rush'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing yards before contact per rushing attempt.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_yards_after_contact(self):
        """Get method for rushing yards after contact

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_yac'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_yac'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing yards after contact.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_yards_after_contact_per_attempt(self):
        """Get method for rushing yards after contact per rushing attempt

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_yac_per_rush'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_yac_per_rush'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing yards after contact per rushing attempt.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_broken_tackles(self):
        """Get method for broken tackles on rushes

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_broken_tackles'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_broken_tackles'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for broken tackles on rushes.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushes_per_broken_tackle(self):
        """Get method for rushes per broken tackle

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_broken_tackles_per_rush'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__rushing_receiving_advanced_stats[self.__rushing_receiving_advanced_stats['year'] == self.__year]['rush_broken_tackles_per_rush'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushes per broken tackle.\nYear:{0}\n\nException:{1}".format(self.__year, e))
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