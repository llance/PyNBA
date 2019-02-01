import datetime
import json
from nba.models import Teams


def load_team(teams, db, upload_date):
    print(teams, upload_date)


    for team in teams:
        print('team is : %s' %(team))    
        team = Teams(
                        id = team['id'],
                        full_name = team['full_name'],
                        abbreviation = team['abbreviation'],
                        nickname = team['nickname'],
                        city = team['city'],
                        state = team['state'],
                        year_founded = team['year_founded']
                         )
        db.add(team)
    db.commit()
    return
