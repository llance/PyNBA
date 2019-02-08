from rest_framework import serializers
from nba_app.models import Player, ShotChart


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('teamid', 'season', 'leagueid', 'num', 'position', 'height', 'weight', 'birth_date', 'age', 'school', 'player', 'playerid', 'exp')


class ShotChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShotChart
        fields = ('grid_type','game_id','game_event_id','player_id','player_name','team_id','team_name','period','minutes_remaining','seconds_remaining','event_type','action_type','shot_type','shot_zone_basic','shot_zone_area','shot_zone_range','shot_distance','loc_x','loc_y','shot_attempted_flag','shot_made_flag','game_date','htm','vtm')