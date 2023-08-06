class StatTypeURLData():
    def __init__(self, logger=None):
        """Initialize

        Args:
            logger (Python Logger): User's instance of the python logger. Defaults to None.
        """
        self.__logger = logger
        self.__player_urls = list()
        self.__already_added = list()
    
    def set_stat_type_urls(self, url_data):
        """Obtains the information and stores it within the dict if the player has not been stored already

        Args:
            url_data (list): index 0 = player name
                             index 1 = player url

        Raises:
            Exception: Generic Exception to log whatever issue occurred
        """
        try:
            if (url_data):
                player_name = url_data[0]
                player_url = url_data[1]
                
                if(not self.__check_for_duplicate(player_name)):
                    self.__player_urls.append({
                            "name": player_name,
                            "url": player_url
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
    
    def get_list_of_urls(self):
        """Get method for the urls as a list

        Returns:
            list: A list of dictionaries containing the player's name and the url
        """
        return self.__player_urls
    
    def get_count_of_urls(self):
        """Returns the number of URLs stored within the dictionary

        Returns:
            int: Number of URLs stored in the dict
        """
        return len(self.__player_urls)
    
    def get_range_of_urls(self, start_pos, end_pos):
        """Get method for a specific range of URLs

        Args:
            start_pos (int): This is the ranking of the first player you will want to pull.  The programming will handle the proper indexing.
            end_pos (int): This is the ranking of the last player you will want to pull.  The programming will handle the proper indexing.

        Returns:
            list: A list of dictionaries containing the player's name and URL
        """
        try:
            return self.__player_urls[start_pos - 1: end_pos]
        except IndexError as e:
            self.__logging("The indexes provided were:\nStart Position: {0}\nEnd Position: {1}\nError: {2}".format(start_pos, end_pos, e))
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