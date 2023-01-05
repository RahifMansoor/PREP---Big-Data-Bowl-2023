import pandas as pd
from math import *
player_tracking_data = pd.read_csv("data_with_angles.csv")
lst = []
angle_qb = []
prevFrameP = []
nextFrameP = []
count = 1
interval = 0
prev = interval
changeAngle = []
# Calculate the change in angle between the QB and each player at each frame
for i in range(player_tracking_data.shape[0]-1):
    if player_tracking_data.loc[i].at['playId'] != player_tracking_data.loc[i+1].at['playId']:
        for j in range(prev, interval+1):
            changeAngle.append(0)
        prev = interval + 1
        interval +=  1
    elif player_tracking_data.loc[i].at['time'] != player_tracking_data.loc[i+1].at['time']:
        for j in range(prev, interval+1):
            if player_tracking_data.loc[j].at['officialPosition'] == "QB":
                prevFrameP.append(0)
            else:
                prevFrameP.append(player_tracking_data.loc[j].at['angle_qb'])
        for j in range(interval+1, (interval+1)*2 -prev):
            if player_tracking_data.loc[j].at['officialPosition'] == "QB":
                nextFrameP.append(0)
            else:
                nextFrameP.append(player_tracking_data.loc[j].at['angle_qb'])
        for j in range(interval+1-prev):
            changeAngle.append(abs(nextFrameP[j] - prevFrameP[j]))
        nextFrameP = []
        prevFrameP = []
        prev = interval + 1
        interval += 1
    else:
        interval += 1

# again this gets filtered out later on
changeAngle.append(0)
changeAngle.append(0)
changeAngle.append(0)
changeAngle.append(0)
changeAngle.append(0)
player_tracking_data['change_angle_qb'] = changeAngle
player_tracking_data.to_csv("data_with_change_angles.csv", index=False)