import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import os

# Function to get player career stats by player name
def get_player_career_stats(player_name):
    # Get player ID from player name
    player_info = players.find_players_by_full_name(player_name)
    if not player_info:
        print(f'Player not found: {player_name}')
        return None

    player_id = player_info[0]['id']

    # Get player career stats
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_df = career_stats.get_data_frames()[0]

    return career_df

# Define the path to the draft_picks folder
draft_picks_folder = os.path.join('..', 'draft_picks')

# Define the path to the career_stats folder
career_stats_folder = os.path.join('..', 'career_stats')
os.makedirs(career_stats_folder, exist_ok=True)

# Loop through each draft pick file from 1 to 60
for pick_number in range(1, 61):
    # Build the file path
    csv_file = os.path.join(draft_picks_folder, f'nba_draft_pick_{pick_number}.csv')

    # Check if the file exists
    if not os.path.exists(csv_file):
        print(f'File not found: {csv_file}')
        continue

    # Read CSV file
    df = pd.read_csv(csv_file)

    # Create a folder for this draft pick number
    pick_folder = os.path.join(career_stats_folder, f'draft_pick_{pick_number}')
    os.makedirs(pick_folder, exist_ok=True)

    # Loop through each player in the CSV file
    for index, row in df.iterrows():
        player_name = row['PLAYER_NAME']
        print(f'Fetching career stats for {player_name}')

        # Get player career stats
        career_df = get_player_career_stats(player_name)
        if career_df is not None:
            # Build the file path for career stats
            career_csv_file = os.path.join(pick_folder, f'{player_name}_career_stats.csv')
            # Replace any characters in player_name that are invalid in file names
            career_csv_file = career_csv_file.replace('/', '_').replace('\\', '_')

            # Write career stats to a new CSV file
            career_df.to_csv(career_csv_file, index=False)
