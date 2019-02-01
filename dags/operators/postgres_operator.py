from airflow.models import BaseOperator
from contextlib import contextmanager
from nba_api.stats.static import players
from nba_api.stats.static import teams
from sqlalchemy.orm import sessionmaker, scoped_session
from operators.etl import load_team
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
        db_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=self.engine))
        yield db_session
        db_session.close()
        connection.close()

    def execute(self):
        all_teams = teams.get_teams()
        # print('all_teams : %s' %(all_teams))

        # for team in all_teams:
            # print('team is : %s' %(team))

        with self.db_session() as db:
            load_team(all_teams, db, '{{(execution_date - macros.timedelta(days=1)).strftime("%Y-%m-%dT00:00:00.000")}}')

        # with self.db_session() as db:



        # with self.db_session() as db:
        #     for group_obj in all_groups:
        #         for group in group_obj.results:
        #             time.sleep(0.4)
        #             group.get_events(m, **EVENT_KWARGS)
        #     load_groups(all_groups, db, self.start)