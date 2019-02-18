from nba_app.models import Player, ShotChart
from nba_app.serializers import PlayerSerializer, ShotChartSerializer

from rest_framework.views import APIView
from rest_framework.response import Response




class PlayersList(APIView):
    """
    List all players, or create a new player.
    """
    def get(self, request, format=None):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)




class ShotChartList(APIView):
    """
    List all players, or create a new player.
    """
    def get(self, request, player_id, format=None):
        shotcharts = ShotChart.objects.filter(player_id=player_id)
        serializer = ShotChartSerializer(shotcharts, many=True)
        return Response(serializer.data)
