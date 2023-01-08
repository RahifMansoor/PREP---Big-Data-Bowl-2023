import matplotlib
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and a subplot
fig, ax = plt.subplots()

import pandas as pd


new_id = 297

def read_pressure_model(new_id):
    df = pd.read_csv('prepmodel.csv')
    df = df[df['newId'] == new_id]
    pressure_model = df.groupby('displayName')['modelPressure'].apply(list).to_dict()
    return pressure_model

pressure_model = read_pressure_model(new_id)
values = list(pressure_model.values())

# Set x-axis values
x = range(len(values[0]))

# Set y-axis values for each line
y1 = values[0]
y2 = values[1]
y3 = values[2]
y4 = values[3]
#y5 = values[4]
#y6 = values[5]

sorted_keys = sorted(pressure_model)

# Plot the lines and set the labels using the sorted keys
line1, = ax.plot(x, y1, 'r-', label=sorted_keys[0])
line2, = ax.plot(x, y2, 'b-', label=sorted_keys[1])
line3, = ax.plot(x, y3, 'g-', label=sorted_keys[2])
line4, = ax.plot(x, y4, 'k-', label=sorted_keys[3])
#line5, = ax.plot(x, y5, 'y-', label=sorted_keys[4])
#line6, = ax.plot(x, y6, 'm-', label=sorted_keys[5])
# Set title and labels

# Add legend
plt.legend(loc='upper left')

# Set limits for x- and y-axis
plt.xlim(0, len(values[0])-1)
plt.ylim(0.5, 4)

plt.title('gameId: 2021091202, playID: 2543')
plt.xlabel('frameID')
plt.ylabel('pressure')

# Set the update function for the animation
def update(num):
    line1.set_data(x[:num], y1[:num])
    line2.set_data(x[:num], y2[:num])
    line3.set_data(x[:num], y3[:num])
    line4.set_data(x[:num], y4[:num])
    line5.set_data(x[:num], y5[:num])
    line6.set_data(x[:num], y5[:num])
    return line1, line2, line3, line4, line5, line6

# Create the animation using FuncAnimation
ani = FuncAnimation(fig, update, interval=200, repeat=True)

# Save the animation as a gif
ani.save('animation3.gif', writer='imagemagick', fps=10)

# Show the animation
plt.show()
