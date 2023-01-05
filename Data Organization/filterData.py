import pandas as pd
player_tracking_data = pd.read_csv('data_with_change_angles.csv')

# Create an empty dataframe to store the modified tracking data
modified_tracking_data = pd.DataFrame()

# Get a list of unique playIds
play_ids = player_tracking_data['newId'].unique()
print(play_ids)

# Loop through each playId
for play_id in play_ids:
    # Filter the data to only include rows for the current playId
    play_data = player_tracking_data[player_tracking_data['newId'] == play_id]
    
    # Find the first row where the 'event' column is 'ball_snap'
    first_ball_snap = play_data[play_data['event'] == 'ball_snap']['time'].min()
    
    # Find the last row where the 'event' column is one of the following: 'pass_forward', 'qb_sack', 'qb_strip_sack', 'fumble', or 'run'
    last_pass_forward = play_data[(play_data['event'] == 'pass_forward') | (play_data['event'] == 'qb_sack') | (play_data['event'] == 'qb_strip_sack') | (play_data['event'] == 'fumble') | (play_data['event'] == 'run')]['time'].max()
    
    # Remove rows before the first ball snap event
    play_data = play_data.loc[play_data['time'] >= first_ball_snap]
    
    # Remove rows after the last pass forward event
    play_data = play_data.loc[play_data['time'] <= last_pass_forward]
    
    # Append the modified data for the current play to the modified_tracking_data dataframe
    modified_tracking_data = pd.concat([modified_tracking_data, play_data])
    
# Replace the original tracking data with the modified data
player_tracking_data = modified_tracking_data
# remove the quarterback from the data
player_tracking_data = player_tracking_data[player_tracking_data['officialPosition'].isin(['DE', 'DT', 'NT', 'OLB'])]
player_tracking_data.to_csv('plays_that_matter.csv', index=False)