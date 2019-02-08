from rest_framework import serializers
from nba_app.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('teamid', 'season', 'leagueid', 'num', 'position', 'height', 'weight', 'birth_date', 'age', 'school', 'player', 'playerid', 'exp')
