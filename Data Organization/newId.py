import pandas as pd
from math import *
player_tracking_data = pd.read_csv("player_tracking_data.csv")
lst = []
count = 1
# create new Id for each play because there are multiple of the same playId
for i in range(player_tracking_data.shape[0]-1):
    if player_tracking_data.loc[i].at['playId'] != player_tracking_data.loc[i+1].at['playId']:
        lst.append(count)
        count += 1
    else:
        lst.append(count)

lst.append(count)
player_tracking_data['newId'] = lst
player_tracking_data.to_csv("data_with_newId.csv", index=False)