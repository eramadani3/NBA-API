from nba_api.stats.endpoints import playercareerstats
import pandas as pd

# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999')

# pandas data frames (optional: pip install pandas)
data_frame = career.get_data_frames()[0]
data_frame.to_csv('player_career_stats.csv', index=False)
