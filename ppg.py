from nba_api.stats.endpoints import playercareerstats
import pandas as pd

# Define the player ID (e.g., Nikola Jokić)
player_id = '203999'

# Create a PlayerCareerStats object for the player
career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)

# Retrieve the data frames
data_frame = career_stats.get_data_frames()[0]

# Calculate PPG
data_frame['PPG'] = data_frame['PTS'] / data_frame['GP']

# Save the data frame to a CSV file
data_frame.to_csv('ppg_career_stats.csv', index=False)
