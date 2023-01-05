# Import necessary libraries
import pandas as pd

# Load the play data from a CSV file
play_data = pd.read_csv('players.csv')

# Load the tracking data from multiple CSV files
tracking_data = pd.concat([
    pd.read_csv(f'week{i}.csv')
    for i in range(1, 9)
])

# Merge the play data and tracking data on gameId and playId
player_tracking_data = pd.merge(play_data, tracking_data, on=['nflId', ])

# Only include rows with specific players
player_tracking_data = player_tracking_data[player_tracking_data['officialPosition'].isin(['QB','DE', 'DT', 'NT', 'OLB'])]

# Drop unnecessary columns
player_tracking_data = player_tracking_data.drop(columns=['collegeName', 'birthDate', 'playDirection'])
player_tracking_data.head()

# Sort the data by gameId, time, and playId in that order
player_tracking_data = player_tracking_data.sort_values(['gameId', 'time', 'playId'])

# Save the play_tracking data to a CSV file
player_tracking_data.to_csv('player_tracking_data.csv', index=False)
