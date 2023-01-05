import pandas as pd
from math import *
player_tracking_data = pd.read_csv("data_with_newId.csv")
distance_qb = []
count = 1
interval = 0
prev = interval
# Calculate the distance between the QB and each player at each frame
for i in range(player_tracking_data.shape[0]-1):
    if player_tracking_data.loc[i].at['time'] != player_tracking_data.loc[i+1].at['time']:
        for j in range(prev, interval+1):
            if player_tracking_data.loc[j].at['officialPosition'] == "QB":
                qbX = int(player_tracking_data.loc[j].at['x'])
                qbY = int(player_tracking_data.loc[j].at['y'])
        for j in range(prev, interval+1):
            if player_tracking_data.loc[j].at['officialPosition'] == "QB":
                distance_qb.append(None)
            else:
                distance_qb.append(((qbX - player_tracking_data.loc[j].at['x'])**2 + (qbY - player_tracking_data.loc[j].at['y'])**2) ** 0.5)
        prev = interval + 1
        interval += 1
    else:
        interval += 1

distance_qb.append(0)
distance_qb.append(0)
distance_qb.append(0)
distance_qb.append(0)
distance_qb.append(0)
player_tracking_data['distance_qb'] = distance_qb
player_tracking_data.to_csv("data_with_distance_qb.csv", index=False)
