class TeamURLData():
    def __init__(self, logger=None):
        """Initialize

        Args:
            logger (Python Logger): User's instance of the python logger. Defaults to None.
        """
        self.__logger = logger
        self.__player_urls = dict()
        self.__already_added = list()
    
    def set_team_urls(self, url_data):
        """Obtains the information and stores it within the dict if the player has not been stored already

        Args:
            url_data (list): index 0 = player name
                             index 1 = player url
                             index 2 = player position

        Raises:
            Exception: Generic Exception to log whatever issue occurred
        """
        try:
            if (url_data):
                player_name = url_data[0]
                player_url = url_data[1]
                player_position = url_data[2]
                
                if(not self.__check_for_duplicate(player_name)):
                    if (player_position not in self.__player_urls.keys()):
                        self.__player_urls[player_position] = []
                        
                    self.__player_urls[player_position].append({
                        "url": player_url,
                        "name": player_name
                    })
                    
                    self.__already_added.append(player_name)
        except Exception as e:
            self.__logging(e)
            raise Exception(e)
        
    def __check_for_duplicate(self, player_name):
        """Checks to see if the player's URL is already present

        Args:
            player_name (str): Player's name

        Returns:
            Bool: Returns True if name exists and False if it does not
        """
        if (player_name in self.__already_added):
            return True
        
        return False
    
    def get_dictionaries_of_urls(self):
        """Get method for the urls as a dictionary

        Returns:
            dict: A dictionary of URLs with the position of the players as the key
        """
        return self.__player_urls
    
    def get_quarterbacks(self):
        """Get method to get the quarterbacks

        Returns:
            list: A list of dictionaries of players whos position is QB.  If none were found returns empty string.
        """
        try:
            return self.__player_urls['QB']
        except KeyError as e:
            self.__logging("No quarterbacks available.\nError: {0}".format(e))
            return []
    
    def get_running_backs(self):
        """Get method to get the running backs

        Returns:
            list: A list of dictionaries of players whos position is RB.  If none were found returns empty string.
        """
        try:
            return self.__player_urls['RB']
        except KeyError as e:
            self.__logging("No running backs available.\nError: {0}".format(e))
            return []
    
    def get_fullbacks(self):
        """Get method to get the fullbacks

        Returns:
            list: A list of dictionaries of players whos position is FB.  If none were found returns empty string.
        """
        try:
            return self.__player_urls['FB']
        except KeyError as e:
            self.__logging("No fullbacks available.\nError: {0}".format(e))
            return []
    
    def get_wide_receivers(self):
        """Get method to get the wide receivers

        Returns:
            list: A list of dictionaries of players whos position is WR.  If none were found returns empty string.
        """
        try:
            return self.__player_urls['WR']
        except KeyError as e:
            self.__logging("No wide receivers available.\nError: {0}".format(e))
            return []
    
    def get_tight_ends(self):
        """Get method to get the tight ends

        Returns:
            list: A list of dictionaries of players whos position is TE.  If none were found returns empty string.
        """
        try:
            return self.__player_urls['TE']
        except KeyError as e:
            self.__logging("No tight ends available.\nError: {0}".format(e))
            return []
        
    def get_kickers(self):
        """Get method to get the kickers

        Returns:
            list: A list of dictionaries of players whos position is K.  If none were found returns empty string.
        """
        try:
            return self.__player_urls['K']
        except KeyError as e:
            self.__logging("No kickers available.\nError: {0}".format(e))
            return []
    
    def __logging(self, message):
        """If a logger exists it logs the error message

        Args:
            message (str): Error message
        """
        if (self.__logger):
            self._logger.error("Error: {0}".format(message))
    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")