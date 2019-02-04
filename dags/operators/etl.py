import datetime
import json
from nba.models import Teams, Roster, ShotChartDetail, PlayerCareerStats


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


def load_roster(rosters, db, upload_date):
    try:
        # print("rosters['resultSets'] is %s" %(rosters['resultSets']))
        for roster_data in rosters['resultSets'][0]['rowSet']:
            print('roster_data is %s' %(roster_data))
            roster = Roster(
                    teamid = roster_data[0],
                    season = roster_data[1],
                    leagueid = roster_data[2],
                    player = roster_data[3],
                    num = roster_data[4],
                    position = roster_data[5],
                    height = roster_data[6],
                    weight = roster_data[7],
                    birth_date = roster_data[8],
                    age = roster_data[9],
                    exp = roster_data[10],
                    school = roster_data[11],
                    playerid =roster_data[12]
                )
            db.add(roster)
        db.commit()
    except Exception as e:
        print('exception in load_roster : %s' %(e))
    else:
        pass
    finally:
        return

def load_shotchartdetail(shotchartdetails, db, upload_date):
    try:
        for shotchart in shotchartdetails['resultSets'][0]['rowSet']:
            # print('shotchart is :%s' %(shotchart))
            shotchartobj = ShotChartDetail(
                grid_type = shotchart[0],
                game_id = shotchart[1],
                game_event_id = shotchart[2],
                player_id = shotchart[3],
                player_name = shotchart[4],
                team_id = shotchart[5],
                team_name = shotchart[6],
                period = shotchart[7],
                minutes_remaining = shotchart[8],
                seconds_remaining = shotchart[9],
                event_type = shotchart[10],
                action_type = shotchart[11],
                shot_type = shotchart[12],
                shot_zone_basic = shotchart[13],
                shot_zone_area = shotchart[14],
                shot_zone_range = shotchart[15],
                shot_distance = shotchart[16],
                loc_x = shotchart[17],
                loc_y = shotchart[18],
                shot_attempted_flag = shotchart[19],
                shot_made_flag = shotchart[20],
                game_date = shotchart[21],
                htm = shotchart[22],
                vtm = shotchart[23]
                )
            db.add(shotchartobj)
        db.commit()

        # print('shotchartdetails is %s' %(shotchartdetails))
    except Exception as e:
        print('exception in load_shotchartdetail : %s' %(e))
    else:
        pass
    finally:
        return

def load_playercareerstats(playerstats, db, upload_date):
    try:
        for ps in playerstats:
            # print('shotchart is :%s' %(shotchart))
            playerstatobj = PlayerCareerStats(
                player_id =ps[0],
                season_id =ps[1],
                league_id =ps[2],
                team_id =ps[3],
                team_abbreviation =ps[4],
                player_age =ps[5],
                gp =ps[6],
                gs =ps[7],
                min =ps[8],
                fgm =ps[9],
                fga =ps[10],
                fg_pct =ps[11],
                fg3m =ps[12],
                fg3a =ps[13],
                fg3_pct =ps[14],
                ftm =ps[15],
                fta =ps[16],
                ft_pct =ps[17],
                oreb =ps[18],
                dreb =ps[19],
                reb =ps[20],
                ast =ps[21],
                stl =ps[22],
                blk =ps[23],
                tov =ps[24],
                pf =ps[25],
                pts =ps[26]
                )
            db.add(playerstatobj)
        db.commit()

    except Exception as e:
        print('exception in load_playercareerstats : %s' %(e))
    else:
        pass
    finally:
        return

