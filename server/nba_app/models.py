from django.db import models

# Create your models here.

class Player(models.Model):
    class Meta:
        managed = False
        db_table = "nba_api\".\"roster"

    teamid = models.IntegerField()
    season = models.IntegerField()
    leagueid = models.IntegerField()
    num = models.IntegerField()
    position = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight = models.IntegerField()
    birth_date = models.DateField()
    age = models.IntegerField()
    school = models.CharField(max_length=100)
    playerid = models.IntegerField(primary_key=True)
    player = models.CharField(max_length=100)
    exp = models.CharField(max_length=100)



class ShotChart(models.Model):
    class Meta:
        managed = False
        db_table = "nba_api\".\"shotchartdetail"
        unique_together = (('game_id', 'player_id', 'period', 'minutes_remaining', 'seconds_remaining', 'event_type', 'action_type', 'shot_type'),)

    grid_type = models.CharField(max_length=100)
    game_id = models.IntegerField()
    game_event_id = models.IntegerField()
    player_id = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=100)
    team_id = models.IntegerField()
    team_name = models.CharField(max_length=100)
    period = models.IntegerField()
    minutes_remaining = models.IntegerField()
    seconds_remaining = models.IntegerField()
    event_type = models.CharField(max_length=100)
    action_type = models.CharField(max_length=100)
    shot_type = models.CharField(max_length=100)
    shot_zone_basic = models.CharField(max_length=100)
    shot_zone_area = models.CharField(max_length=100)
    shot_zone_range = models.CharField(max_length=100)
    shot_distance = models.IntegerField()
    loc_x = models.IntegerField()
    loc_y = models.IntegerField()
    shot_attempted_flag = models.IntegerField()
    shot_made_flag = models.IntegerField()
    game_date = models.CharField(max_length=100)
    htm = models.CharField(max_length=100)
    vtm = models.CharField(max_length=100)