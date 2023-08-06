import pandas as pd

class PositionAbstract():
    def set_or_update_dataframe(self, dataframe_instance, dict_data):
        """Abstracted class that takes a dataframe and dict and updates the dataframe with the information

        Args:
            dataframe_instance (Dataframe): Dataframe containing data relevant to the dict
            dict_data (dict): Dictionary containing relevant data to the class executing the method

        Returns:
            Dataframe: Dataframe updated with the information from the dict
        """
        if (dict_data and isinstance(dict_data, dict) and len(dict_data) > 0):
            if(not dataframe_instance.empty):
                dataframe_instance = dataframe_instance.append(self.__convert_dict_to_dataframe(dict_data), ignore_index=True)
            else:
                dataframe_instance = self.__convert_dict_to_dataframe(dict_data)
                
        return dataframe_instance
    
    def __convert_dict_to_dataframe(self, dict_data):
        """Parses the dictionary's data and places them in their relevant references

        Args:
            dict_data (dict): Dictionary of data
            
        Return:
            dataframe_instance (DataFrame): Dataframe containing the data
        """
        dataframe_instance = pd.DataFrame.from_dict(dict_data)
        dataframe_instance['year'] = dataframe_instance['year'].astype(int)
        return dataframe_instance