from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
import pandas as pd

# Players we want to look into
superstars = ["Stephen Curry", "Michael Jordan", "Kevin Durant", "LeBron James", "Allen Iverson"]

# Pull player ids from superstars
player_ids = [players.find_players_by_full_name(player_name)[0]['id'] for player_name in superstars]

# Pull game logs of each player
game_logs = []
for player_id, player_name in zip(player_ids, superstars):
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season=SeasonAll.all).get_data_frames()[0]
    game_logs.append(game_log)
    # Save the game log to a CSV file
    game_log.to_csv(f"{player_name}_game_log.csv", index=False)

player_data = dict(zip(superstars, game_logs))

# Enter any player from the superstar list to access their game log
print(player_data["LeBron James"])
