from urllib.request import FancyURLopener
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


class MyOpener(FancyURLopener):
    def __init__(self):
        """Initialize
        """
        FancyURLopener.__init__(self)

    def create_user_agent(self):
        """Generates a random user agent for use

        Returns:
            Object: A user agent
        """
        self.__setup_random_user_agent()
        user_agent = self.__user_agent_rotator.get_random_user_agent()
        return user_agent

    def __setup_random_user_agent(self):
        """Generates a random user for use when creating the user agent
        """
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [
            OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
        self.__user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems,
                                            limit=100)


if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")
