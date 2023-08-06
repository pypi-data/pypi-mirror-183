import pandas as pd
import os
import sys

passing_directory = os.path.dirname(__file__)
position_directory = os.path.dirname(passing_directory)
pfr_directory = os.path.dirname(position_directory)

sys.path.insert(0, pfr_directory)

from PFRWebScraper.Includes.PositionAbstract import PositionAbstract

class DefenseAndFumblesPlayoffs():
    def __init__(self, logger, season_games, generic_error_message, defense_and_fumbles_data):
        self.__logger = logger
            
        self.season_games = season_games
        self.__generic_error_message = generic_error_message
        self.__defense_and_fumbles_playoffs_stats = pd.DataFrame()
        self.__year = 0
        
        self.parse_defense_and_fumbles_data(defense_and_fumbles_data)
        
    def parse_defense_and_fumbles_data(self, defense_and_fumbles_data):
        """Sets the defense and fumbles data for the playoffs in the object

        Args:
            defense_and_fumbles_data (dict): Defense and fumbles data for the playoffs obtained from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        """
        
        self.__defense_and_fumbles_playoffs_stats = PositionAbstract().set_or_update_dataframe(self.__defense_and_fumbles_playoffs_stats, defense_and_fumbles_data)
        
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
        return list(self.__defense_and_fumbles_playoffs_stats['year'].values)
    
    def get_dataframe_of_stats(self):
        """Returns a dataframe of all of the stats

        Returns:
            Dataframe: Dataframe containing all the stats
        """
        return self.__defense_and_fumbles_playoffs_stats
    
    def get_dictionary_of_stats(self):
        """Converts the dataframe to a dictionary of dictionaries and returns it.
        Each row of data becomes its own dictionary within the dictionary.

        Returns:
            dict: Dictionary of dictionaries containing all the stats
        """
        return self.__defense_and_fumbles_playoffs_stats.to_dict('index')
    
    def get_age(self):
        """Get method for age 

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['age'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['age'].values[0])
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
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['team_abbreviation'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['team_abbreviation'].values[0])
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
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['position'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return str(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['position'].values[0])
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
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['games_played'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['games_played'].values[0])
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
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['games_started'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['games_started'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for games started.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_interceptions(self):
        """Get method for passes intercepted on defense

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['def_int'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['def_int'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passes intercepted on defense.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_interception_yards(self):
        """Get method for return yards from interceptions

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['def_int_yds'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['def_int_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for return yards from interceptions.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_interception_touchdowns(self):
        """Get method for return touchdowns from interceptions

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['def_int_td'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['def_int_td'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for return touchdowns from interceptions.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_longest_interception(self):
        """Get method for longest interception return

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['def_int_long'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['def_int_long'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for longest interception return.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passes_defended(self):
        """Get method for passes defended

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['pass_defended'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['pass_defended'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passes defended.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_forced_fumbles(self):
        """Get method for fumbles forced and recovered by either team

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['fumbles_forced'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['fumbles_forced'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for fumbles forced.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_all_fumbles(self):
        """Get method for Number of times fumbled both lost and recovered by own team. These represent ALL fumbles by the player on offense, defense, and special teams

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['fumbles'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['fumbles'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for all fumbles.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))

    def get_fumbles_recovered(self):
        """Get method for Fumbles recovered by a Player or Team. Original fumble by either team

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['fumbles_rec'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['fumbles_rec'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for fumbles recovered.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_yards_from_fumbles_recovered(self):
        """Get method for Yards recovered fumbles were returned

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['fumbles_rec_yds'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['fumbles_rec_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for Yards recovered fumbles were returned.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_touchdowns_from_fumbles_recovered(self):
        """Get method for Touchdowns recovered fumbles were returned

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['fumbles_rec_td'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['fumbles_rec_td'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for touchdowns recovered fumbles were returned.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_sacks(self):
        """Get method for sacks

        Returns:
            array/float: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['sacks'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return float(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['sacks'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for sacks.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
    
    def get_combined_tackles(self):
        """Get method for combined tackles. Combined solo + assisted tackles

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['tackles_combined'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['tackles_combined'].values[0])
        except ValueError as e:
            error_message = ("Invalid value combined tackles.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_solo_tackles(self):
        """Get method for solo tackles

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['tackles_solo'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['tackles_solo'].values[0])
        except ValueError as e:
            error_message = ("Invalid value solo tackles.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_assists_on_tackles(self):
        """Get method for assists on tackles

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['tackles_assists'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['tackles_assists'].values[0])
        except ValueError as e:
            error_message = ("Invalid value assists on tackles.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_tackles_for_loss(self):
        """Get method for tackles for loss

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['tackles_loss'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['tackles_loss'].values[0])
        except ValueError as e:
            error_message = ("Invalid value tackles for loss.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_quarterback_hits(self):
        """Get method for quarterback hits

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['qb_hits'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['qb_hits'].values[0])
        except ValueError as e:
            error_message = ("Invalid value quarterback hits.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_safeties_scored(self):
        """Get method for safeties scored

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['safety_md'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['safety_md'].values[0])
        except ValueError as e:
            error_message = ("Invalid value safeties scored.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_approximate_value(self):
        """Get method for approximate value

        Returns:
            array/int: The correlating value(s) from https://www.pro-football-reference.com/players/{initial}/{player_identifier}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return_value = self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['approximate_value'].values
            if(len(return_value) > 1):
                return return_value
            else:
                return int(self.__defense_and_fumbles_playoffs_stats[self.__defense_and_fumbles_playoffs_stats['year'] == self.__year]['approximate_value'].values[0])
        except ValueError as e:
            error_message = ("Invalid value approximate value.\nYear:{0}\n\nException:{1}".format(self.__year, e))
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