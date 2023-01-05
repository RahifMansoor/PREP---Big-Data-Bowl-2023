import pandas as pd

data = pd.read_csv("model_data_pressure..csv")
data = data[data['officialPosition'].isin(['OLB', 'DE', 'DT', 'NT'])]
unique = data['displayName'].unique()
temp = []
for name in unique:
    if len(data[data['displayName'] == name]) >= 5000:
        temp.append(name)
data = data[data['modelPressure'] >= 0.375]
unique = data['displayName'].unique()
means = []
speeds = []
accel = []
dis = []
angle = []
changeangle = []
for name in unique:
    if len(data[data['displayName'] == name]) >= 70 and name in temp:
        tempData = data[data['displayName'] == name]
        speeds.append(str(round(float(tempData[['s']].mean()),2)))
        accel.append(str(round(float(tempData[['a']].mean()),2)))
        dis.append(str(round(float(tempData[['dis']].mean()),2)))
        angle.append(str(round(float(tempData[['angle_qb']].mean()),2)))
        changeangle.append(str(round(float(tempData[['change_angle_qb']].mean()),2)))
        means.append(str(float(tempData[['modelPressure']].mean())) + " " + str(name) + " " + str(len(tempData[['modelPressure']])))
means.sort()
means.reverse()

for i in range(1, len(means[:21])):
    print(str(i)+ ". " + str(means[i-1]) + " s:"+ speeds[i-1] + " a:"+accel[i-1] + " dis:"+dis[i-1] + " angle:"+angle[i-1] + " change_angle:"+changeangle[i-1])
