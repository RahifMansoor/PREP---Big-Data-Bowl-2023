from matplotlib import cm
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# Create a dataframe with the variables as columns and player names as the index
df = pd.DataFrame({'Names': names,'Pressure': pressures,
                   'Speed': speeds,
                   'Acceleration': accelerations,
                   'Displacement': displacements,
                   'Angle': angles,
                  'ChangeAngle': change_in_angles
                  },
                  index=range(1, 11))

fig, ax =plt.subplots()
ax.axis('tight')
ax.axis('off')

# Create a table with the dataframe's values and the colors array
table = ax.table(cellText=df.values,
        colLabels=df.columns, rowLabels=df.index,
        loc="center",
        cellLoc="left")

vals = df['Pressure']

normal = cm.colors.Normalize(vals.min(), vals.max())
bcmap2 = plt.cm.Greens(normal(vals))

for idx, bb in enumerate(bcmap2):
    table[(idx+1, 1)].set_facecolor(bb)
    
vals = df['Speed']

normal = cm.colors.Normalize(vals.min(), vals.max())
bcmap2 = plt.cm.Greens(normal(vals))

for idx, bb in enumerate(bcmap2):
    table[(idx+1, 2)].set_facecolor(bb)

vals = df['Acceleration']

normal = cm.colors.Normalize(vals.min(), vals.max())
bcmap2 = plt.cm.Greens(normal(vals))

for idx, bb in enumerate(bcmap2):
    table[(idx+1, 3)].set_facecolor(bb)

vals = df['Displacement']

normal = cm.colors.Normalize(vals.min(), vals.max())
bcmap2 = plt.cm.Greens(normal(vals))

for idx, bb in enumerate(bcmap2):
    table[(idx+1, 4)].set_facecolor(bb)

vals = df['Angle']

normal = cm.colors.Normalize(vals.min(), vals.max())
bcmap2 = plt.cm.Greens(normal(vals))

for idx, bb in enumerate(bcmap2):
    table[(idx+1, 5)].set_facecolor(bb)
    
vals = df['ChangeAngle']

normal = cm.colors.Normalize(vals.min(), vals.max())
bcmap2 = plt.cm.Greens(normal(vals))

for idx, bb in enumerate(bcmap2):
    table[(idx+1, 6)].set_facecolor(bb)
    
plt.savefig("color.png", dpi=600)
plt.show()