from airflow.models import BaseOperator
from contextlib import contextmanager
from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import shotchartdetail, commonteamroster, playercareerstats
from sqlalchemy.orm import sessionmaker, scoped_session
from operators.etl import load_team, load_roster, load_shotchartdetail, load_playercareerstats

import pandas as pd
import time


class PostgresOperator(BaseOperator):
    def __init__(self,
                 engine,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = engine
        self.execute()

    @contextmanager
    def db_session(self):
        """ Creates a context with an open SQLAlchemy session.
        """
        connection = self.engine.connect()
        db_session = scoped_session(sessionmaker(
            autocommit=False, autoflush=True, bind=self.engine))
        yield db_session
        db_session.close()
        connection.close()

    # def execute(self):
        # all_teams = teams.get_teams()
        # print('all_teams : %s' %(all_teams))

        # with self.db_session() as db:
        # load_team(all_teams, db, '{{(execution_date - macros.timedelta(days=1)).strftime("%Y-%m-%dT00:00:00.000")}}')

        #     all_team_roster_list = []
        #     for team in all_teams:
        #         time.sleep(3)
        #         team_roster = commonteamroster.CommonTeamRoster(season='2018-19', team_id=team['id'])
        #         with self.db_session() as db:
        #             load_roster(team_roster.get_dict(), db, '{{(execution_date - macros.timedelta(days=1)).strftime("%Y-%m-%dT00:00:00.000")}}')

    # def execute(self):
    #     # PlayerCareerStats
    #     with self.db_session() as db:
    #         all_team_roster = db.execute("SELECT * FROM nba_api.roster WHERE playerid NOT IN (SELECT DISTINCT player_id FROM nba_api.playercareerstats)")
    #         # loaded_playercareerstats = db.execute("SELECT DISTINCT player_id FROM nba_api.playercareerstats")
    #     # print(loaded_playercareerstats.keys())

    #     for roster in all_team_roster:
    #         #player_id
    #         # print(roster[10])
    #         time.sleep(3)
    #         playerstats = playercareerstats.PlayerCareerStats(player_id=roster[10])
    #         # print('playerstats is %s' %(playerstats.get_dict()['resultSets'][0]['rowSet']))
    #         with self.db_session() as db:
    #             load_playercareerstats(playerstats.get_dict()['resultSets'][0]['rowSet'], db, '{{(execution_date - macros.timedelta(days=1)).strftime("%Y-%m-%dT00:00:00.000")}}')

    def execute(self)
        try:
            with self.db_session() as db:
                player_team_by_season = db.execute("SELECT * FROM nba_api.playercareerstats WHERE player_id NOT IN (SELECT DISTINCT player_id FROM" +
                                                   " nba_api.shotchartdetail)")

            for player in player_team_by_season:
                # sleep minimum 3 seconds to avoid stats.nba.com endpoint blocking my ip for ddos
                time.sleep(3)

                print("getting %s's stats for season : %s" %
                      (player[0], player[1]))

                player_shot_chart = shotchartdetail.ShotChartDetail(team_id=player[3],
                                                                    player_id=player[0],
                                                                    context_measure_simple='FGA',  # FGA field goal attempted tracks all shots
                                                                    season_nullable=player[1])
                shot_chart = player_shot_chart.get_dict()

                with self.db_session() as db:
                    load_shotchartdetail(
                        shot_chart, db, '{{(execution_date - macros.timedelta(days=1)).strftime("%Y-%m-%dT00:00:00.000")}}')

        except Exception as e:
            print('exception in PostgresOperator.execute is %s' % (e))
