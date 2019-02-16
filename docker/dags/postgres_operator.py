from airflow.models import BaseOperator
from contextlib import contextmanager
from nba_api.stats.static import players
from nba_api.stats.static import teams
from operators.etl import load_groups
from sqlalchemy.orm import sessionmaker, scoped_session
import time

class PostgresOperator(BaseOperator):
    template_fields = ('start', 'end')

    def __init__(self,
                 engine,
                 start,
                 end,
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = engine
        self.start = start
        self.end = end

    @contextmanager
    def db_session(self):
        """ Creates a context with an open SQLAlchemy session.
        """
        connection = self.engine.connect()
        db_session = scoped_session(sessionmaker(autocommit=True, autoflush=True, bind=self.engine))
        yield db_session
        db_session.close()
        connection.close()

    def execute(self, context):
        all_teams = teams.get_teams()
        print('all_teams : %s' %(all_teams))


        # with self.db_session() as db:
        #     for group_obj in all_groups:
        #         for group in group_obj.results:
        #             time.sleep(0.4)
        #             group.get_events(m, **EVENT_KWARGS)
        #     load_groups(all_groups, db, self.start)