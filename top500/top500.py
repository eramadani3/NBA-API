from nba_api.stats.endpoints import leagueleaders
import pandas as pd

# Pull data for the top 500 scorers by PTS column
top_500 = leagueleaders.LeagueLeaders(
    per_mode_simple='PerGame',
    season='2020-21',
    season_type_all_star='Regular Season',
    stat_category_abbreviation='PTS'
).get_data_frames()[0][:500]

# Group players by name and player ID and calculate average stats
top_500_avg = top_500.groupby(['player_name', 'player_id']).mean()[[
    'min', 'fgm', 'fga', 'ftm', 'fta', 'pts', 'fg3m', 'fg3a', 'gp'
]]

# Save to CSV
top_500_avg.to_csv('top_500_avg_stats.csv')
