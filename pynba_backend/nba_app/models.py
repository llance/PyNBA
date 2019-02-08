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

