# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans

# Load the tracking data from a CSV file
tracking_data = pd.read_csv('filtered_data.csv')

CLUSTER_COUNT = 10

# Use KMeans clustering to group plays based on the distance from the quarterback
kmeans = KMeans(n_clusters=CLUSTER_COUNT)

# Fit the model to the distance from the quarterback
clusters = kmeans.fit_predict(tracking_data[['distance_to_qb']])

# Add the cluster labels to the data
tracking_data['cluster'] = clusters

# Group the data by cluster and calculate the mean distance from the quarterback for each cluster
cluster_stats = tracking_data.groupby('cluster')['distance_to_qb'].mean()
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
cluster_stats = tracking_data.groupby('cluster')['distance_to_qb'].mean()
cluster_stats = cluster_stats.sort_values()

# Print the sorted clusters
print(cluster_stats)


