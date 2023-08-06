from PFRWebScraper.TeamData.TeamDefenseData import TeamDefenseData
from PFRWebScraper.TeamData.TeamOffenseData import TeamOffenseData
from PFRWebScraper.Includes.ScrapeDataAbstract import ScrapeDataAbstract
from PFRWebScraper.Includes.Configuration import Configuration
import datetime
import os


class ScrapeTeamData():
    def __init__(self):
        """Initialization
        """
        self.__config_parameters = Configuration().import_config("ScrapeData.config")
        self.__team_abbreviations = Configuration().import_config("TeamAbbreviations.config", section="TEAMTOABBREVIATION")
    
    def get_team_abbreviation(self, team_name=None):
        """Takes a team name and converts it to that team's abbreviation 

        Args:
            team_name (str): An NFL team's name

        Returns:
            str: Returns the abbreviation for the team's name
        """
        try:
            return self.__team_abbreviations[team_name.title()]
        except KeyError:
            return ""
    
    def scrape_defense(self, team_abbreviation, years_back=4):
        """Workflow for scraping data for a team's defense

        Args:
            years_back (int): Number of years of data that should be pulled
                                    in reference to a team's stats. Defaults to 4.
            team_abbreviation (str): The abbreviation of a team that the data will
                                    be scraped for.

        Returns:
            Object: Team Defense Data Object
        """
        self.__team_url = os.path.join(
            self.__config_parameters['baseURLTeam'], team_abbreviation)
        list_of_years_url = self.__obtain_years_list(years_back)
        defense_data_object = TeamDefenseData()
        
        for url in list_of_years_url:
            yearly_data = self.__scrape_team_data(url, "Opp. Stats", "Lg Rank Defense")
            if (len(yearly_data) > 0):
                defense_data_object.parse_defense_data(yearly_data)
                
        return defense_data_object

    def scrape_offense(self, team_abbreviation, years_back=4):
        """Workflow for scraping data for a team's offense

        Args:
            years_back (int): Number of years of data that should be pulled
                                    in reference to a team's stats. Defaults to 4.
            team_abbreviation (string): The abbreviation of a team that the data will
                                    be scraped for.

        Returns:
            Object: Team Offense Data Object
        """
        self.__team_url = os.path.join(
            self.__config_parameters['baseURLTeam'], team_abbreviation)
        list_of_years_url = self.__obtain_years_list(years_back)
        offense_data_object = TeamOffenseData()
        
        for url in list_of_years_url:
            yearly_data = self.__scrape_team_data(url, "Team Stats", "Lg Rank Offense")
            if (len(yearly_data) > 0):
                offense_data_object.parse_offense_data(yearly_data)
                
        return offense_data_object

    def __obtain_years_list(self, years_back):
        """Obtains a formatted list of urls with the years added to the teams

        Args:
            years_back (int): Total span of years that needs to be scraped starting
                            at present day

        Returns:
            list: List of urls
        """
        current_year = datetime.datetime.now().year
        list_of_years = list()

        for year in range(current_year, current_year - years_back, -1):
            list_of_years.append("{0}/{1}.htm".format(self.__team_url, str(year)))
            
        return list_of_years
    
    def __scrape_team_data(self, url, stats_reference, rankings_reference):
        """Navigates to the appropriate table and delegates the scraping
            of specific data to the two methods it calls below

        Args:
            url (string): URL of the site that will be scraped

        Returns:
            list: defensive stat dictionary, defensive ranking dictionary
        """
        scraper = ScrapeDataAbstract().create_scraper(url)
        stats = dict()
        rankings = dict()
        year = url.split("/")[5].replace(".htm", "")
        
        for all_team_stats in scraper.find_all(id="all_team_stats"):
            for div_team_stats in all_team_stats.find_all(id="div_team_stats"):
                for team_stats in div_team_stats.find_all(id="team_stats"):
                    for tbody in team_stats.find_all("tbody"):
                        for tr in tbody.find_all("tr"):
                            for th in tr.find_all("th"):
                                if (th.text == stats_reference):
                                    stats = self.__obtain_stats(year, tr.find_all("td"))
                                elif(th.text == rankings_reference):
                                    rankings = self.__obtain_ranks(year, tr.find_all("td"))
                            
        if (stats == {} or rankings == {}):
            return []
        else:
            return [stats, rankings]
    
    def __obtain_stats(self, year, stats_section):
        """Obtains the teams stats from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm

        Args:
            stats_section (Object): BeautifulSoup object pointing at the specific row within a table for the
                                            defense's opponent's data

        Returns:
            dict: Dictionary containing all the data within the row
        """
        stats = dict()
        
        stats['year'] = [int(year)]
        
        for stat in stats_section:
            if (stat['data-stat'] == 'points'):
                stats['points'] = [int(stat.text)]
            elif (stat['data-stat'] == 'total_yards'):
                stats['total_yards'] = [int(stat.text)]
            elif (stat['data-stat'] == 'plays_offense'):
                stats['plays_offense'] = [int(stat.text)]
            elif (stat['data-stat'] == 'yds_per_play_offense'):
                stats['yds_per_play_offense'] = [float(stat.text)]
            elif (stat['data-stat'] == 'turnovers'):
                stats['turnovers'] = [int(stat.text)]
            elif (stat['data-stat'] == 'fumbles_lost'):
                stats['fumbles_lost'] = [int(stat.text)]
            elif (stat['data-stat'] == 'first_down'):
                stats['first_down'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_cmp'):
                stats['pass_cmp'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_att'):
                stats['pass_att'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_yds'):
                stats['pass_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_td'):
                stats['pass_td'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_int'):
                stats['pass_int'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pass_net_yds_per_att'):
                stats['pass_net_yds_per_att'] = [float(stat.text)]
            elif (stat['data-stat'] == 'pass_fd'):
                stats['pass_fd'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rush_att'):
                stats['rush_att'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rush_yds'):
                stats['rush_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rush_td'):
                stats['rush_td'] = [int(stat.text)]
            elif (stat['data-stat'] == 'rush_yds_per_att'):
                stats['rush_yds_per_att'] = [float(stat.text)]
            elif (stat['data-stat'] == 'rush_fd'):
                stats['rush_fd'] = [int(stat.text)]
            elif (stat['data-stat'] == 'penalties'):
                stats['penalties'] = [int(stat.text)]
            elif (stat['data-stat'] == 'penalties_yds'):
                stats['penalties_yds'] = [int(stat.text)]
            elif (stat['data-stat'] == 'pen_fd'):
                stats['pen_fd'] = [int(stat.text)]
            elif (stat['data-stat'] == 'drives'):
                stats['drives'] = [int(stat.text)]
            elif (stat['data-stat'] == 'score_pct'):
                stats['score_pct'] = [float(stat.text)]
            elif (stat['data-stat'] == 'turnover_pct'):
                stats['turnover_pct'] = [float(stat.text)]
            elif (stat['data-stat'] == 'start_avg'):
                stats['start_avg'] = [float(stat.text.split(" ")[1])]
            elif (stat['data-stat'] == 'time_avg'):
                stats['time_avg'] = self.__convert_average_time(stat.text)
            elif (stat['data-stat'] == 'plays_per_drive'):
                stats['plays_per_drive'] = [float(stat.text)]
            elif (stat['data-stat'] == 'yds_per_drive'):
                stats['yds_per_drive'] = [float(stat.text)]
            elif (stat['data-stat'] == 'points_avg'):
                stats['points_avg'] = [float(stat.text)]
                
        return stats
    
    def __convert_average_time(self, time_avg):
        """_summary_

        Args:
            time_avg (string): Average time per drive

        Returns:
            timedelta: Average time per drive
        """
        return datetime.timedelta(hours=int(time_avg.split(":")[0]), minutes=int(time_avg.split(":")[1]))
    
    def __obtain_ranks(self, year, teams_rankings):
        """Obtains the team's ranking from https://www.pro-football-reference.com/{team-abbreviation}/{year}.htm

        Args:
            teams_rankings (Object): BeautifulSoup object pointing at the specific row within a table for the
                                            defense's ranking

        Returns:
            dict: Dictionary containing all the data within the row
        """
        rankings = dict()
        
        rankings['year'] = [int(year)]
        
        for ranking in teams_rankings:
            if (ranking['data-stat'] == 'points'):
                rankings['points'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'total_yards'):
                rankings['total_yards'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'turnovers'):
                rankings['turnovers'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'fumbles_lost'):
                rankings['fumbles_lost'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'first_down'):
                rankings['first_down'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'pass_att'):
                rankings['pass_att'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'pass_yds'):
                rankings['pass_yds'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'pass_td'):
                rankings['pass_td'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'pass_int'):
                rankings['pass_int'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'pass_net_yds_per_att'):
                rankings['pass_net_yds_per_att'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'rush_att'):
                rankings['rush_att'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'rush_yds'):
                rankings['rush_yds'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'rush_td'):
                rankings['rush_td'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'rush_yds_per_att'):
                rankings['rush_yds_per_att'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'score_pct'):
                rankings['score_pct'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'turnover_pct'):
                rankings['turnover_pct'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'start_avg'):
                rankings['start_avg'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'time_avg'):
                rankings['time_avg'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'plays_per_drive'):
                rankings['plays_per_drive'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'yds_per_drive'):
                rankings['yds_per_drive'] = [int(ranking.text)]
            elif (ranking['data-stat'] == 'points_avg'):
                rankings['points_avg'] = [int(ranking.text)]
        
        return rankings


if __name__ == '__main__':
    print("This is not meant to be run as a stand alone class")
    
    instance = ScrapeTeamData()
    
    temp = instance.scrape_offense("rai", 1)
    
    print(temp)
