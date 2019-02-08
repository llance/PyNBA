from django.contrib.auth.models import User, Group
from rest_framework import viewsets, serializers
from nba_app.models import Player
from nba_app.serializers import PlayerSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, action

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from django.http import HttpResponse




class PlayersList(APIView):
    """
    List all players, or create a new player.
    """
    def get(self, request, format=None):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
