import pandas as pd

class TeamDefenseData():
    def __init__(self, logger=None, season_games=17):
        """Initialize

        Args:
            logger (logger): Logger passed by class. Defaults to None.
            season_games (int): The number of games played in an NFL season. Defaults to 17.
        """
        self.__logger = logger
        self.__generic_error_message = "An error has occurred please check the log for more information.\nError:"
        self.season_games = season_games
        
        self.__year = int()
        self.__defense_stats = pd.DataFrame()
        self.__defense_ranks = pd.DataFrame()
        
    def parse_defense_data(self, defense_data):
        """Main method to load data into object

        Args:
            defense_data (list): Defense data and rankings from the web scraper
        """
        if(defense_data and isinstance(defense_data, list) and len(defense_data) == 2):
            if(not self.__defense_stats.empty):
                self.__defense_stats = self.__defense_stats.append(self.__parse_defense_stats(defense_data[0]), ignore_index=True)
            else:
                self.__defense_stats = self.__parse_defense_stats(defense_data[0])
                
            if(not self.__defense_ranks.empty):
                self.__defense_ranks = self.__defense_ranks.append(self.__parse_defense_rankings(defense_data[1]), ignore_index=True)
            else:
                self.__defense_ranks = self.__parse_defense_rankings(defense_data[1])
        
    def __parse_defense_stats(self, defense_stats):
        """Parses the dictionary's defensive stats and places them in their relevant references

        Args:
            defense_stats (dict): Defensive Data
            
        Return:
            defense_data (Dataframe): Defensive Data
        """
        
        defensive_stats = pd.DataFrame.from_dict(defense_stats)
        defensive_stats['year'] = defensive_stats['year'].astype(int)
        return defensive_stats
        
    def __parse_defense_rankings(self, defensive_rankings):
        """Parses the dictionary's defensive rankings and puts them in their relevant references

        Args:
            defensive_rankings (dict): Defensive Rankings
            
        Return:
            defensive_rank (DataFrame): Defensive Rankings
        """
        
        defensive_rank = pd.DataFrame.from_dict(defensive_rankings)
        defensive_rank['year'] = defensive_rank['year'].astype(int)
        return defensive_rank
        
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
        return list(self.__defense_stats['year'].values)
    
    def get_dataframe_of_stats(self):
        """Returns a dataframe of all of the stats

        Returns:
            Dataframe: Dataframe containing all the stats
        """
        return self.__defense_stats
    
    def get_dictionary_of_stats(self):
        """Converts the dataframe to a dictionary of dictionaries and returns it.
        Each row of data becomes its own dictionary within the dictionary.

        Returns:
            dict: Dictionary of dictionaries containing all the stats
        """
        return self.__defense_stats.to_dict('index')
    
    def get_points_allowed(self):
        """Get method for points allowed by defense

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['points'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for points.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
        
    def get_total_yards_allowed(self):
        """Get method for total yards allowed by defense

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['total_yards'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for total yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
    
    def get_opponents_offensive_plays(self):
        """Get method for the number of offensive plays the opponents had against the defense

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['plays_offense'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for offensive plays.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_yards_per_play_allowed(self):
        """Get method for the number of yards the defense would allow per play

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__defense_stats[self.__defense_stats['year'] == self.__year]['yds_per_play_offense'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for yards per play.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_turnovers(self):
        """Get method for the turnovers the defense caused

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['turnovers'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for turnovers.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_forced_fumbles(self):
        """Get method for the number of fumbles the defense recovered

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['fumbles_lost'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for forced fumbles.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_first_downs_allowed(self):
        """Get method for the number of first downs the defense allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['first_down'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for first down.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_completed_passes_allowed(self):
        """Get method for the number of completed passes the defense allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['pass_cmp'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for completed passes.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_opponents_attempted_passes(self):
        """Get method for the number of passes attempted the defense allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['pass_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for attempted passes.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_yards_allowed(self):
        """Get method for the number of passing yards the defense allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['pass_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_touchdowns_allowed(self):
        """Get method for the number of passing touchdowns the defense allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['pass_td'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_interceptions(self):
        """Get method for the number of times the defense intercepted the opposing team

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['pass_int'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for interceptions.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_yards_per_attempt_allowed(self):
        """Get method for the number of passing yards the defense allowed per attempt

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__defense_stats[self.__defense_stats['year'] == self.__year]['pass_net_yds_per_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing yards per attempt.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_first_downs_allowed(self):
        """Get method for the number of passing first downs the defense allowed per attempt

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['pass_fd'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing first downs.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_opponents_attempted_rushes(self):
        """Get method for the number of times the opponent attempted rushes on the defense

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['rush_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing attempts.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_yards_allowed(self):
        """Get method for the rushing yards the defense allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['rush_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_touchdowns_allowed(self):
        """Get method for the rushing touchdowns the defense allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['rush_td'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_yards_per_attempt_allowed(self):
        """Get method for the rushing yards per attempt the defense allowed

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__defense_stats[self.__defense_stats['year'] == self.__year]['rush_yds_per_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing yards per attempt.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_first_downs_allowed(self):
        """Get method for the rushing first downs the defense allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['rush_fd'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing first downs.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_penalties(self):
        """Get method for the number of penalties the opponent committed and the defense accepted

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['penalties'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for penalties.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_yards_from_penalties(self):
        """Get method for the number of penalty yards the defense's opponents accrued

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['penalties_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for yards from penalties.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_first_downs_from_penalties(self):
        """Get method for the number of first downs the defense's opponents received due to penalties

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['pen_fd'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for first downs from penalties.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_drives_allowed(self):
        """Get method for the number of drives the defense's opponents attempted

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['drives'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for drives.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_of_drives_ending_in_score(self):
        """Get method for the percentage of drives the defense allowed a score

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__defense_stats[self.__defense_stats['year'] == self.__year]['score_pct'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for percentage of drives ending in a score.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_of_drives_ending_in_turnovers(self):
        """Get method for the percentage of drives ended by the defense getting a turnover

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__defense_stats[self.__defense_stats['year'] == self.__year]['turnover_pct'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for percentage of drives ending in a turnover.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_starting_field_position_allowed(self):
        """Get method for the average starting field position of the defense's opponents

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_stats[self.__defense_stats['year'] == self.__year]['start_avg'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average starting field position.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_time_per_drive_allowed(self):
        """Get method for the average time the defense's opponent's drives lasted

        Returns:
            timedelta64: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return self.__defense_stats[self.__defense_stats['year'] == self.__year]['time_avg'].values[0]
        except ValueError as e:
            error_message = ("Invalid value for average time drives lasted.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_plays_per_drive_allowed(self):
        """Get method for the average number of plays the defense's opponent attempted per drive

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__defense_stats[self.__defense_stats['year'] == self.__year]['plays_per_drive'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for number of plays per drive.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_yards_per_drive_allowed(self):
        """Get method for the average number of yards the defense's opponent received per drive

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__defense_stats[self.__defense_stats['year'] == self.__year]['yds_per_drive'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average yards per drive.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_points_per_drive_allowed(self):
        """Get method for the average number of points the defense allowed per drive

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__defense_stats[self.__defense_stats['year'] == self.__year]['points_avg'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average points per drive.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_points_allowed_ranking(self):
        """Get method for the defense's ranking for points allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['points'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for points ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_total_yards_allowed_ranking(self):
        """Get method for the defense's ranking for total yards allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['total_yards'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for total yards ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_turnovers_ranking(self):
        """Get method for the defense's ranking for turnovers

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['turnovers'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for turnovers ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_fumbles_recovered_ranking(self):
        """Get method for the defense's ranking for fumbles recovered

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['fumbles_lost'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for fumbles recovered ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_first_downs_allowed_ranking(self):
        """Get method for the defense's ranking for first downs they allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['first_down'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for first down ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_opponents_attempted_passes_ranking(self):
        """Get method for the defense's ranking for the number of passes an opponent would attempt on them

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['pass_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for attempted passes ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_yards_allowed_ranking(self):
        """Get method for the defense's ranking for the passing yards they allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['pass_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing yards ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_touchdowns_allowed_ranking(self):
        """Get method for the defense's ranking for the passing touchdowns they allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['pass_td'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing touchdown ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_interceptions_ranking(self):
        """Get method for the defense's ranking for the number of interceptions they got

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['pass_int'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for intercepted passes ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_yards_per_attempt_allowed_ranking(self):
        """Get method for the defense's ranking for the number of passing yards allowed per attempt

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['pass_net_yds_per_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing yards per attempt ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_opponents_attempted_rushes_ranking(self):
        """Get method for the defense's ranking for the number of times an opponent attempted to run on them

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['rush_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing attempts ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_yards_allowed_ranking(self):
        """Get method for the defense's ranking for the number rushing yards they allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['rush_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing yards ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_touchdowns_allowed_ranking(self):
        """Get method for the defense's ranking for the number rushing touchdowns they allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['rush_td'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing touchdowns ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_yards_per_attempt_allowed_ranking(self):
        """Get method for the defense's ranking for the number rushing yards per attempt they allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['rush_yds_per_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing yards per attempt ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_of_drives_ending_in_score_ranking(self):
        """Get method for the defense's ranking of the percentage of drives they allowed the opponent to score

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['score_pct'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for percentage of drives ending in a score ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_of_drives_ending_in_turnover_ranking(self):
        """Get method for the defense's ranking of the percentage of drives they ended a drive in a turnover

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['turnover_pct'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for percentage of drives ending in a turnover ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_starting_field_position_allowed_ranking(self):
        """Get method for the defense's ranking of the average field position the opponent starts with

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['start_avg'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average starting field position ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_time_per_drive_allowed_ranking(self):
        """Get method for the defense's ranking of the average time it took to end their opponent's drive

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['time_avg'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average time of possession per drive ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_plays_per_drive_allowed_ranking(self):
        """Get method for the defense's ranking of the average number of plays the opponent had per drive

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['plays_per_drive'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average plays per drive ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_yards_per_drive_allowed_ranking(self):
        """Get method for the defense's ranking of the average number of yards the opponent had per drive

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['yds_per_drive'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average yards per drive ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_points_per_drive_allowed_ranking(self):
        """Get method for the defense's ranking of the average number of points the opponent had per drive

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__defense_ranks[self.__defense_ranks['year'] == self.__year]['points_avg'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average points per drive ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
    
    def get_average_points_allowed_per_game(self):
        """GET the average numbers of points allowed per game

        Returns:
            float: Divides the points allowed by the number of games in a season
        """
        return float(self.get_points_allowed() / self.season_games)
    
    def get_average_yards_allowed_per_game(self):
        """GET the average number of yards allowed per game

        Returns:
            float: Divides the total yards allowed by the number of games in a season
        """
        return float(self.get_total_yards_allowed() / self.season_games)
    
    def get_average_offensive_plays_attempted_per_game(self):
        """GET the average number of offensive plays an opponent attempts on the defense

        Returns:
            float: Divdes the all the opponents offensive plays by the number of games in a season
        """
        return float(self.get_opponents_offensive_plays() / self.season_games)
    
    def get_average_turnovers_per_game(self):
        """GET the average number of takeaways the defense had per game

        Returns:
            float: Divides the opponents turnovers by the number of games in a season
        """
        return float(self.get_turnovers() / self.season_games)
    
    def get_average_forced_fumbles_per_game(self):
        """GET the average number of fumbles forced by the defense per game

        Returns:
            float: Divides the fumbles forced by the total number of games in a season
        """
        return float(self.get_forced_fumbles() / self.season_games)
    
    def get_average_first_downs_per_game(self):
        """GET the average number of first downs the defense allowed per game

        Returns:
            float: Divides the number of first downs allowed by the number of games in a season
        """
        return float(self.get_first_downs_allowed() / self.season_games)
    
    def get_opponents_completion_percentage(self):
        """GET the percentage of passes completed against the defense

        Returns:
            float: Divides the number of completed passes by the number of passes attempted and multiplies that value by 100
        """
        return (float(self.get_completed_passes_allowed() / self.get_opponents_attempted_passes()) * 100)
    
    def get_average_number_of_completed_passes_allowed_per_game(self):
        """GET the average number of completed passes the defense would allow per game

        Returns:
            float: Divides the completed passes allowed by the number of games in a season
        """
        return float(self.get_completed_passes_allowed() / self.season_games)
    
    def get_average_number_of_passes_attempted_per_game(self):
        """GET the average number of times the opponent would attempt to pass the ball against the defense

        Returns:
            float: Divides the number of passes the opponent attempted by the number of games in a season
        """
        return float(self.get_opponents_attempted_passes() / self.season_games)
    
    def get_average_passing_yards_per_game(self):
        """GET the average number of passing yards the defense allowed per game

        Returns:
            float: Divides the number of passing yards allowed by the number of games in a season
        """
        return float(self.get_passing_yards_allowed() / self.season_games)
    
    def get_average_passing_touchdowns_per_game(self):
        """GET the average number of passing touchdowns the defense allowed per game

        Returns:
            float: Divides the number of passing touchdowns by the number of games in a season
        """
        return float(self.get_passing_touchdowns_allowed() / self.season_games)
    
    def get_average_interceptions_per_game(self):
        """GET the average number of interceptions the defense has per game

        Returns:
            float: Divides the number of interceptions by the number of games in a season
        """
        return float(self.get_interceptions() / self.season_games)
    
    def get_average_passing_first_downs_per_game(self):
        """GET the average number of passing first downs the defense allowed per game

        Returns:
            float: Divides the passing first downs allowed by the number of games in a season
        """
        return float(self.get_passing_first_downs_allowed() / self.season_games)
    
    def get_average_number_of_rushing_attempts_per_game(self):
        """GET the average number of times the opponent attempted to rush against the defense per game

        Returns:
            float: Divides the number of times the opponent attempted to rush by the number of games in a season
        """
        return float(self.get_opponents_attempted_rushes() / self.season_games)
    
    def get_average_rushing_yards_allowed_per_game(self):
        """GET the average number of yards the the defense would allow per game

        Returns:
            float: Divides the rushing yards allowed by the number of games in a season
        """
        return float(self.get_rushing_yards_allowed() / self.season_games)
    
    def get_average_rushing_touchdowns_per_game(self):
        """GET the average number of rushing touchdowns the defense would allow per game

        Returns:
            float: Divides the rushing touchdowns allowed by the number of games in a season
        """
        return float(self.get_rushing_touchdowns_allowed() / self.season_games)
    
    def get_average_rushing_first_downs_per_game(self):
        """GET the average number of rushing first downs the defense would allow per game

        Returns:
            float: Divides the rushing first downs allowed by the number of games in a season
        """
        return float(self.get_rushing_first_downs_allowed() / self.season_games)
    
    def __logging(self, message):
        """Checks to see if there is a logger and if there is logs the message to the error log
        
        Args:
            message (str): Error message
        """
        if (self.__logger):
            self.__logger.error(message)


if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")
