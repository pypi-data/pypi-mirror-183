import configparser
import os

class Configuration():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_path = self.__obtain_config_path()
        
    def __obtain_config_path(self):
        """Obtains the config path

        Returns:
            string: Config Directory
        """
        
        include_directory = os.path.dirname(__file__)
        src_directory = os.path.dirname(include_directory)
        return os.path.join(src_directory, "configs")
        
    def import_config(self, config_name, config_file=None, section="DEFAULT"):
        """Imports the desired config and adds it to the end of the config file
        specified.  If no config file is specified then it will return an
        initial dictionary containing the default config values

        Args:
            config_name (string): Name of config file
            config_file (dict, optional): Previously used config variable. Defaults to {}.
            section (str, optional): Section of the config you would like to access. Defaults to "DEFAULT".

        Raises:
            KeyError: The section specified does not exist within the config
            TypeError: A variable type other than dictionary was passed as a parameter
            FileExistsError: Config specified does not exist

        Returns:
            dict: A dictionary containing the config values from the section specified
        """
        config_file_path = os.path.join(self.config_path, config_name)
        if(self.__check_for_file(config_file_path)):
            self.config.read(config_file_path)
            if (config_file):
                config_file.update(self.config[section])
                return config_file
            else:
                try:
                    return self.config[section]
                except KeyError:
                    raise KeyError("Invalid Key - {0} for Config File - {1}".format(section, config_name))
        else:
            raise FileExistsError("Invalid Config file: {0}".format(config_name))
    
    def __check_for_file(self, config_path):
        """Checks to see if the file specified is a valid config file

        Args:
            config_path (string): Config File Path

        Returns:
            bool: It returns true if the file exists or false if the file does not exist
        """
        return os.path.isfile(config_path)
    
if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")