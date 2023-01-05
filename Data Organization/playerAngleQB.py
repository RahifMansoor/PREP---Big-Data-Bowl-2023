import pandas as pd
from math import *
player_tracking_data = pd.read_csv("data_with_distance_qb.csv")
lst = []
angle_qb = []
count = 1
interval = 0
prev = interval
# Calculate the angle between the QB and each player at each frame
for i in range(player_tracking_data.shape[0]-1):
    if player_tracking_data.loc[i].at['time'] != player_tracking_data.loc[i+1].at['time']:
        for j in range(prev, interval+1):
            if player_tracking_data.loc[j].at['officialPosition'] == "QB":
                qbX = int(player_tracking_data.loc[j].at['x'])
                qbY = int(player_tracking_data.loc[j].at['y'])
        for j in range(prev, interval+1):
            if player_tracking_data.loc[j].at['officialPosition'] == "QB":
                angle_qb.append(0)
            else:
                try:
                    angle_qb.append(atan(abs( (qbY - player_tracking_data.loc[j].at['y'])/(qbX - player_tracking_data.loc[j].at['x']))) * 180 / pi)
                except:
                    angle_qb.append(0)
                    continue
        prev = interval + 1
        interval += 1
    else:
        interval += 1
    
# this gets filtered out later on
angle_qb.append(0)
angle_qb.append(0)
angle_qb.append(0)
angle_qb.append(0)
angle_qb.append(0)

player_tracking_data['angle_qb'] = angle_qb
player_tracking_data.to_csv("data_with_angles.csv", index=False)