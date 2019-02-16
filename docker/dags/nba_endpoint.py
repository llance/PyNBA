import csv
import logging
import pandas as pd
import requests

from contextlib import contextmanager
from nba_api.stats.endpoints import shotchartdetail, commonteamroster
from nba_api.stats.static import players
from nba_api.stats.static import teams
from sqlalchemy.orm import sessionmaker, scoped_session




logger = logging.getLogger('root')


def get_all_players_shotchart():
    # all_players = players.get_players()
    all_teams = teams.get_teams()
    print('all_teams : %s' %(all_teams))
    # all_team_roster_list = []
    # for team in all_teams:
    #     team_roster = commonteamroster.CommonTeamRoster(season='2018-19', team_id=team['id'])
    #     print('team_roster for team : %s is %s' %(team['full_name'], team_roster.common_team_roster.get_dict() ))
    #     all_team_roster_list.append(team_roster.common_team_roster.get_data_frame())

    # all_team_roster_df = pd.concat(all_team_roster_list)

    # all_team_roster_df.to_csv(
    #                 path_or_buf='all_team_roster.csv',
    #                 sep='|',
    #                 encoding='utf-8',
    #                 # don't add quote on all columns because nexxus marketing adds quote
    #                 quoting=csv.QUOTE_NONE,
    #                 float_format='%.0f',  # make sure integer are not being casted to float like 123 to 123.0
    #                 index=False)  # don't export dataframe order index

    # for player in all_players:
    #     team_id = teams.find_team_name_by_id(player['id'])
    #     print(team_id)
      # shotchart = shotchartdetail.ShotChartDetail(team_id=, player_id=player['id'])
      # print('shotchart for player %s is %s' %(player['full_name'], shotchart))

def get_all_teams():
    all_teams = teams.get_teams()
    print('all_teams are %s' % (all_teams))
    return all_teams


def nba_api_get(url):
    try:
        if url:
            response = requests.get(url)
            print("get request to : %s's response is : %s, content is %s"  
                        %(url, str(response), response.content))
            # if response.status_code == requests.codes.ok:
            #   print(response)
            # else:
            #   pass
        else:
            raise ValueError('no url has been provided!')
                
    except requests.exceptions.Timeout:
        logger.error('GET request to %s Timed out with exception' %
                     (url))
        # Maybe set up for a retry, or continue in a retry loop
    except requests.exceptions.TooManyRedirects:
        logger.error('GET request to %s has TooManyRedirects' %
                     (url))
        # Tell the user their URL was bad and try a different one
    except requests.exceptions.RequestException as e:
        logger.error('GET request to %s failed with exception %s' %
                     (url, e))
    except Exception as e:
        logger.error("exception occured in get_entity_nm_id : %s" % (e))

get_all_players_shotchart()
