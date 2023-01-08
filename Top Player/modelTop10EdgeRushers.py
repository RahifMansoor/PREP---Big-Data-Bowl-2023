import pandas as pd

data = pd.read_csv("model_data_pressure.csv")
data = data[data['officialPosition'].isin(['OLB', 'DE'])]
unique = data['displayName'].unique()
temp = []
for name in unique:
    if len(data[data['displayName'] == name]) >= 5000:
        temp.append(name)
data = data[data['modelPressure'] >= 1.8]
unique = data['displayName'].unique()

means = []
speed = []
accel = []
dis = []
angle = []
changeangle = []
i = 0
data2 = []
for name in unique:
    if len(data[data['displayName'] == name]) >= 60 and name in temp:
        tempData = data[data['displayName'] == name]
        speed.append(str(round(float(tempData[['s']].mean()),2)))
        accel.append(str(round(float(tempData[['a']].mean()),2)))
        dis.append(str(round(float(tempData[['dis']].mean()),2)))
        angle.append(str(round(float(tempData[['angle_qb']].mean()),2)))
        changeangle.append(str(round(float(tempData[['change_angle_qb']].mean()),2)))
        means.append(str(float(tempData[['modelPressure']].mean())) + " " + str(name) + " " + str(len(tempData[['modelPressure']])) + " " + str(speed[i])+ " " + str(accel[i])+ " " + str(dis[i])+ " " + str(angle[i])+ " " + str(changeangle[i]) )
        
        i+=1
        
means.sort()
means.reverse()
names = []
pressures = []
speeds = []
accelerations = []
displacements = []
angles = []
change_in_angles = []
means = means[:10]
for i in means:
    temp = i.split(" ")
    names.append(temp[1] + " " + temp[2])
    pressures.append(float(temp[0]))
    speeds.append(float(temp[4]))
    accelerations.append(float(temp[5]))
    displacements.append(float(temp[6]))
    angles.append(float(temp[7]))
    change_in_angles.append(float(temp[8]))
for i in range(len(means)):
    print(str(i+1)+ ". " + str(means[i]))
