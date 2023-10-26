import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo

def get_player_common_info(player_name):
    # Get player information
    player_dict = players.find_players_by_full_name(player_name)
    if not player_dict:
        print(f"No player found with name {player_name}")
        return None
    player_id = player_dict[0]['id']
    
    # Get common player info
    common_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id).get_data_frames()[0]
    
    # Save to CSV
    common_info.to_csv(f'{player_name}_common_info.csv', index=False)
    
    print(f"Data saved to {player_name}_common_info.csv")

# Example usage
player_name = "LeBron James"
get_player_common_info(player_name)
