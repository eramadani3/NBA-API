from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster, CommonPlayerInfo
from nba_api.stats.endpoints import playercareerstats
import os
import pandas as pd

nba_teams = teams.get_teams()

for team in nba_teams:
    team_name = team['full_name'].replace(' ', '_')
    dir_path = f"{os.getcwd()}/{team_name}"
    os.makedirs(dir_path, exist_ok=True)
    roster = commonteamroster.CommonTeamRoster(team_id=team['id'])
    roster_df = roster.get_data_frames()[0]
    player_ids = roster_df['PLAYER_ID'].tolist()
    for player_id in player_ids:
        career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
        career_df = career_stats.get_data_frames()[0]
        player_info = CommonPlayerInfo(player_id=player_id)
        player_info_df = player_info.get_data_frames()[0]
        full_name = player_info_df['DISPLAY_FIRST_LAST'].iloc[0]
        file_name = f"{full_name.replace(' ', '_')}_career_stats.csv"
        file_path = f"{dir_path}/{file_name}"
        career_df.to_csv(file_path, index=False)
