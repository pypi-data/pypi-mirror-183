import pandas as pd

class TeamOffenseData():
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
        self.__offense_stats = pd.DataFrame()
        self.__offense_ranks = pd.DataFrame()
        
    def parse_offense_data(self, offense_data):
        """Main method to load data into object

        Args:
            offense_data (list): Offense data and rankings from the web scraper
        """
        if(offense_data and isinstance(offense_data, list) and len(offense_data) == 2):
            if(not self.__offense_stats.empty):
                self.__offense_stats = self.__offense_stats.append(self.__parse_offense_stats(offense_data[0]), ignore_index=True)
            else:
                self.__offense_stats = self.__parse_offense_stats(offense_data[0])
                
            if(not self.__offense_ranks.empty):
                self.__offense_ranks = self.__offense_ranks.append(self.__parse_offense_rankings(offense_data[1]), ignore_index=True)
            else:
                self.__offense_ranks = self.__parse_offense_rankings(offense_data[1])
        
    def __parse_offense_stats(self, offense_stats):
        """Parses the dictionary's offensive stats and places them in their relevant references

        Args:
            offense_stats (dict): Offensive Data
            
        Return:
            offensive_stats (DataFrame): Offensive Data
        """
        offensive_stats = pd.DataFrame.from_dict(offense_stats)
        offensive_stats['year'] = offensive_stats['year'].astype(int)
        return offensive_stats
        
    def __parse_offense_rankings(self, offensive_rankings):
        """Parses the dictionary's offensive rankings and puts them in their relevant references

        Args:
            offensive_rankings (dict): Offensive Rankings
            
        Return:
            offensive_rank (DataFrame): Offensive Rankings
        """
        offensive_rank = pd.DataFrame.from_dict(offensive_rankings)
        offensive_rank['year'] = offensive_rank['year'].astype(int)
        return offensive_rank
        
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
        return list(self.__offense_stats['year'].values)
    
    def get_dataframe_of_stats(self):
        """Returns a dataframe of all of the stats

        Returns:
            Dataframe: Dataframe containing all the stats
        """
        return self.__offense_stats
    
    def get_dictionary_of_stats(self):
        """Converts the dataframe to a dictionary of dictionaries and returns it.
        Each row of data becomes its own dictionary within the dictionary.

        Returns:
            dict: Dictionary of dictionaries containing all the stats
        """
        return self.__offense_stats.to_dict('index')
    
    def get_points(self):
        """Get method for points scored

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['points'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for points.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_total_yards(self):
        """Get method for total yards scored by offense

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['total_yards'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for total yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
    
    def get_offensive_plays(self):
        """Get method for the number of offensive plays the team attempted

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['plays_offense'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for offensive plays.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_yards_per_play(self):
        """Get method for the number of yards the team got per play

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__offense_stats[self.__offense_stats['year'] == self.__year]['yds_per_play_offense'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for yards per play.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_turnovers(self):
        """Get method for the turnovers

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['turnovers'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for turnovers.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_fumble_lost(self):
        """Get method for the number of fumbles lost

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['fumbles_lost'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for fumbles lost.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_first_downs(self):
        """Get method for the number of first downs obtained

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['first_down'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for first down.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_completed_passes(self):
        """Get method for the number of completed passes

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['pass_cmp'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for completed passes.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_attempted_passes(self):
        """Get method for the number of passes attempted

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['pass_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for attempted passes.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_yards(self):
        """Get method for the number of passing yards the offense allowed

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['pass_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_touchdowns(self):
        """Get method for the number of passing touchdowns scored

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['pass_td'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_interceptions(self):
        """Get method for the number of interceptions thrown

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['pass_int'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for interceptions.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_yards_per_attempt(self):
        """Get method for the number of passing yards received per attempt

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__offense_stats[self.__offense_stats['year'] == self.__year]['pass_net_yds_per_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing yards per attempt.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_first_downs(self):
        """Get method for the number of passing first downs obtained

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['pass_fd'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing first downs.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_attempted_rushes(self):
        """Get method for the number of times a rush was attempted

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['rush_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing attempts.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_yards(self):
        """Get method for the rushing yards the offense

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['rush_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing yards.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_touchdowns(self):
        """Get method for the rushing touchdowns scored

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['rush_td'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing touchdowns.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_yards_per_attempt(self):
        """Get method for the rushing yards per attempt

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__offense_stats[self.__offense_stats['year'] == self.__year]['rush_yds_per_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing yards per attempt.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_first_downs(self):
        """Get method for the rushing first downs obtained

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['rush_fd'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing first downs.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_penalties(self):
        """Get method for the number of penalties

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['penalties'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for penalties.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_yards_from_penalties(self):
        """Get method for the number of penalty yards accrued

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['penalties_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for yards from penalties.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_first_downs_from_penalties(self):
        """Get method for the number of first downs from penalties

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['pen_fd'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for first downs from penalties.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_drives(self):
        """Get method for the number of drives

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_stats[self.__offense_stats['year'] == self.__year]['drives'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for drives.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_of_drives_ending_in_score(self):
        """Get method for the percentage of drives that end in a score

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__offense_stats[self.__offense_stats['year'] == self.__year]['score_pct'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for percentage of drives ending in a score.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_of_drives_ending_in_turnovers(self):
        """Get method for the percentage of drives ended in a turnover

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__offense_stats[self.__offense_stats['year'] == self.__year]['turnover_pct'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for percentage of drives ending in a turnover.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_starting_field_position(self):
        """Get method for the average starting field position

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__offense_stats[self.__offense_stats['year'] == self.__year]['start_avg'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average starting field position.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_time_per_drive(self):
        """Get method for the average time per drive

        Returns:
            timedelta64: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return self.__offense_stats[self.__offense_stats['year'] == self.__year]['time_avg'].values[0]
        except ValueError as e:
            error_message = ("Invalid value for average time drives lasted.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_plays_per_drive(self):
        """Get method for the average number of plays attempted per drive

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__offense_stats[self.__offense_stats['year'] == self.__year]['plays_per_drive'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for number of plays per drive.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_yards_per_drive(self):
        """Get method for the average number of yards received per drive

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__offense_stats[self.__offense_stats['year'] == self.__year]['yds_per_drive'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average yards per drive.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_points_per_drive(self):
        """Get method for the average number of points scored per drive

        Returns:
            float: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return float(self.__offense_stats[self.__offense_stats['year'] == self.__year]['points_avg'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average points per drive.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_points_ranking(self):
        """Get method for the offense's ranking for points scored

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['points'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for points ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_total_yards_ranking(self):
        """Get method for the offense's ranking for total yards

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['total_yards'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for total yards ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_turnovers_ranking(self):
        """Get method for turnovers ranking

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['turnovers'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for turnovers ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_fumbles_lost_ranking(self):
        """Get method for the ranking for fumbles lost

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['fumbles_lost'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for fumbles lost ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_first_downs_ranking(self):
        """Get method for ranking of first downs obtained

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['first_down'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for first down ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_attempted_passes_ranking(self):
        """Get method for the ranking for the number of passes attempted

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['pass_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for attempted passes ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_yards_ranking(self):
        """Get method for the ranking for the passing yards gained

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['pass_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing yards ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_touchdowns_ranking(self):
        """Get method for the ranking for the passing touchdowns scored

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['pass_td'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing touchdown ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_interceptions_ranking(self):
        """Get method for the ranking for number of interceptions thrown

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['pass_int'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for intercepted passes ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_passing_yards_per_attempt_ranking(self):
        """Get method for the ranking for the number of passing yards gained per attempt

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['pass_net_yds_per_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for passing yards per attempt ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_attempted_rushes_ranking(self):
        """Get method for the ranking for the number of times a rush was attempted

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['rush_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing attempts ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_yards_ranking(self):
        """Get method for the ranking for the number rushing yards gained

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['rush_yds'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing yards ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_touchdowns_ranking(self):
        """Get method for the ranking for the number rushing touchdowns scored

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['rush_td'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing touchdowns ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_rushing_yards_per_attempt_ranking(self):
        """Get method for the ranking for the number rushing yards per attempt

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['rush_yds_per_att'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for rushing yards per attempt ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_of_drives_ending_in_score_ranking(self):
        """Get method for the ranking of the percentage of drives ending in a score

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['score_pct'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for percentage of drives ending in a score ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_percentage_of_drives_ending_in_turnover_ranking(self):
        """Get method for the ranking of the percentage of drives that ended in a turnover

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['turnover_pct'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for percentage of drives ending in a turnover ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_starting_field_position_ranking(self):
        """Get method for the ranking of the average starting field position

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['start_avg'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average starting field position ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_time_per_drive_ranking(self):
        """Get method for the ranking of the average time it took for a drive to end

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['time_avg'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average time of possession per drive ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_plays_per_drive_ranking(self):
        """Get method for the ranking of the average number of plays per drive

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['plays_per_drive'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average plays per drive ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_yards_per_drive_ranking(self):
        """Get method for the ranking of the average number of yards per drive

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['yds_per_drive'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average yards per drive ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
        
    def get_average_points_per_drive_ranking(self):
        """Get method for the ranking of the average number of points scored per drive

        Returns:
            int: The correlating value from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm
        
        Raises:
            ValueError: Value cannot be cast
        """
        try:
            return int(self.__offense_ranks[self.__offense_ranks['year'] == self.__year]['points_avg'].values[0])
        except ValueError as e:
            error_message = ("Invalid value for average points per drive ranking.\nYear:{0}\n\nException:{1}".format(self.__year, e))
            self.__logging(error_message)
            raise ValueError("{0}{1}".format(self.__generic_error_message, e))
    
    def get_average_points_per_game(self):
        """GET the average numbers of points per game

        Returns:
            float: Divides the points by the number of games in a season
        """
        return float(self.get_points() / self.season_games)
    
    def get_average_yards_per_game(self):
        """GET the average number of yards per game

        Returns:
            float: Divides the total yards by the number of games in a season
        """
        return float(self.get_total_yards() / self.season_games)
    
    def get_average_offensive_plays_attempted_per_game(self):
        """GET the average number of offensive plays an attempted per game

        Returns:
            float: Divdes the all the offensive plays by the number of games in a season
        """
        return float(self.get_offensive_plays() / self.season_games)
    
    def get_average_turnovers_per_game(self):
        """GET the average number of turnovers per game

        Returns:
            float: Divides the turnovers by the number of games in a season
        """
        return float(self.get_turnovers() / self.season_games)
    
    def get_average_fumbles_lost_per_game(self):
        """GET the average number of fumbles lost per game

        Returns:
            float: Divides the fumbles lost by the total number of games in a season
        """
        return float(self.get_fumble_lost() / self.season_games)
    
    def get_average_first_downs_per_game(self):
        """GET the average number of first downs per game

        Returns:
            float: Divides the number of first downs by the number of games in a season
        """
        return float(self.get_first_downs() / self.season_games)
    
    def get_completion_percentage(self):
        """GET the percentage of passes completed

        Returns:
            float: Divides the number of completed passes by the number of passes attempted and multiplies that value by 100
        """
        return (float(self.get_completed_passes() / self.get_attempted_passes()) * 100)
    
    def get_average_number_of_completed_passes_per_game(self):
        """GET the average number of completed passes per game

        Returns:
            float: Divides the completed passes by the number of games in a season
        """
        return float(self.get_completed_passes() / self.season_games)
    
    def get_average_number_of_passes_attempted_per_game(self):
        """GET the average number of passes attempted per game

        Returns:
            float: Divides the number of passes attempted by the number of games in a season
        """
        return float(self.get_attempted_passes() / self.season_games)
    
    def get_average_passing_yards_per_game(self):
        """GET the average number of passing yards per game

        Returns:
            float: Divides the number of passing yards by the number of games in a season
        """
        return float(self.get_passing_yards() / self.season_games)
    
    def get_average_passing_touchdowns_per_game(self):
        """GET the average number of passing touchdowns per game

        Returns:
            float: Divides the number of passing touchdowns by the number of games in a season
        """
        return float(self.get_passing_touchdowns() / self.season_games)
    
    def get_average_interceptions_per_game(self):
        """GET the average number of interceptions  per game

        Returns:
            float: Divides the number of interceptions by the number of games in a season
        """
        return float(self.get_interceptions() / self.season_games)
    
    def get_average_passing_first_downs_per_game(self):
        """GET the average number of passing first downs per game

        Returns:
            float: Divides the passing first downs by the number of games in a season
        """
        return float(self.get_passing_first_downs() / self.season_games)
    
    def get_average_number_of_rushing_attempts_per_game(self):
        """GET the average number of rushing attempts per game

        Returns:
            float: Divides the number of rushing attempts by the number of games in a season
        """
        return float(self.get_attempted_rushes() / self.season_games)
    
    def get_average_rushing_yards_per_game(self):
        """GET the average number of rushing yards per game

        Returns:
            float: Divides the rushing yards by the number of games in a season
        """
        return float(self.get_rushing_yards() / self.season_games)
    
    def get_average_rushing_touchdowns_per_game(self):
        """GET the average number of rushing touchdowns per game

        Returns:
            float: Divides the rushing touchdowns by the number of games in a season
        """
        return float(self.get_rushing_touchdowns() / self.season_games)
    
    def get_average_rushing_first_downs_per_game(self):
        """GET the average number of rushing first downs per game

        Returns:
            float: Divides the rushing first downs by the number of games in a season
        """
        return float(self.get_rushing_first_downs() / self.season_games)
    
    def __logging(self, message):
        """Checks to see if there is a logger and if there is logs the message to the error log
        
        Args:
            message (str): Error message
        """
        if (self.__logger):
            self.__logger.error(message)


if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")