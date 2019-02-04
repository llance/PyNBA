from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData, Table, Column, Integer, String, Date, Boolean,  DateTime, Float, ForeignKey
from sqlalchemy import PrimaryKeyConstraint


Base = declarative_base(metadata=MetaData(schema='nba_api'))

class Teams(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    abbreviation = Column(String)
    nickname = Column(String)
    city = Column(String)
    state = Column(String)
    year_founded = Column(Integer)

    def __repr__(self):
        return "<Teams(name='%s')>" % (self.name)

class Roster(Base):
    __tablename__ = 'roster'

    teamid = Column(Integer)
    season = Column(Integer)
    leagueid = Column(Integer)
    player = Column(String)
    num = Column(Integer)
    position = Column(String)
    height = Column(String)
    weight = Column(Integer)
    birth_date = Column(Date)
    age = Column(Integer)
    exp = Column(Integer)
    school = Column(String)
    playerid =Column(Integer, primary_key=True)

    def __repr__(self):
        return "<Roster(name='%s')>" % (self.name)

class ShotChartDetail(Base):
    __tablename__ = 'shotchartdetail'

    __table_args__ = (
        PrimaryKeyConstraint('game_id', 'player_id', 'period', 'minutes_remaining', 'seconds_remaining', 'event_type', 'action_type', 'shot_type'),
    )

    grid_type = Column(String)
    game_id = Column(Integer)
    game_event_id = Column(Integer)
    player_id = Column(Integer)
    player_name = Column(String)
    team_id = Column(Integer)
    team_name = Column(String)
    period = Column(Integer)
    minutes_remaining = Column(Integer)
    seconds_remaining = Column(Integer)
    event_type = Column(String)
    action_type = Column(String)
    shot_type = Column(String)
    shot_zone_basic = Column(String)
    shot_zone_area = Column(String)
    shot_zone_range = Column(String)
    shot_distance = Column(Integer)
    loc_x = Column(Integer)
    loc_y = Column(Integer)
    shot_attempted_flag = Column(Integer)
    shot_made_flag = Column(Integer)
    game_date = Column(String)
    htm = Column(String)
    vtm = Column(String)

    def __repr__(self):
        return "<ShotChartDetail(name='%s')>" % (self.name)


class PlayerCareerStats(Base):
    __tablename__ = 'playercareerstats'

    __table_args__ = (
        PrimaryKeyConstraint('player_id', 'season_id', 'team_id'),
    )

    player_id = Column(Integer)
    season_id = Column(String)
    league_id = Column(Integer)
    team_id = Column(Integer)
    team_abbreviation = Column(String)
    player_age = Column(Integer)
    gp = Column(Integer)
    gs = Column(Integer)
    min = Column(Integer)
    fgm = Column(Integer)
    fga = Column(Integer)
    fg_pct = Column(Integer)
    fg3m = Column(Integer)
    fg3a = Column(Integer)
    fg3_pct = Column(Integer)
    ftm = Column(Integer)
    fta = Column(Integer)
    ft_pct = Column(Integer)
    oreb = Column(Integer)
    dreb = Column(Integer)
    reb = Column(Integer)
    ast = Column(Integer)
    stl = Column(Integer)
    blk = Column(Integer)
    tov = Column(Integer)
    pf = Column(Integer)
    pts = Column(Integer)

    def __repr__(self):
        return "<PlayerCareerStats(name='%s')>" % (self.name)
