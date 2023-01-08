# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
# Load the tracking data from a CSV file
tracking_data = pd.read_csv('filtered_data.csv')
# Remove rows with a distance to the quarterback of 0 and where the player is a quarterback
tracking_data = tracking_data.loc[(tracking_data['distance_qb'] != 0) & (tracking_data['officialPosition'] != 'QB')]
CLUSTER_COUNT = 14
# Use KMeans clustering to group plays based on the distance from the quarterback
kmeans = KMeans(n_clusters=CLUSTER_COUNT)
clusters = kmeans.fit_predict(tracking_data[['distance_qb']])
#Getting unique labels


# Add the cluster labels to the data
tracking_data['cluster'] = clusters

# Group the data by cluster and calculate the mean distance from the quarterback for each cluster
cluster_stats = tracking_data.groupby('cluster')['distance_qb'].mean()
tempDic = {}
tempList = []
cur = 0
for i in cluster_stats:
    tempDic[cur] = i
    tempList.append(i)
    cur += 1

bfSort = tempList[:]
tempList.sort()

newDic = {}
for i in range(CLUSTER_COUNT):
    newDic[i] = tempList[i]

mapDic = {}
for i in range(CLUSTER_COUNT):
    for j in newDic:
        if newDic[j]==tempDic[i]:
            value = j
            break
    mapDic[i] = value

# Sort the clusters by their ranking
tracking_data['cluster'] = tracking_data['cluster'].map(mapDic)
clusters = [mapDic[k] for k in clusters]
cluster_stats = tracking_data.groupby('cluster')['distance_qb'].mean()
cluster_stats = cluster_stats.sort_values()

# Print the sorted clusters
print(cluster_stats)

import matplotlib.pyplot as plt
#graph the clusters
df = tracking_data[['cluster','distance_qb', 'change_angle_qb']]
u_labels = np.unique(clusters)

#plotting the results:
for i in u_labels:
    temp = df[clusters == i]
    plt.scatter(temp[['change_angle_qb']] , temp[['distance_qb']],  label = i)
plt.legend()
plt.show()

