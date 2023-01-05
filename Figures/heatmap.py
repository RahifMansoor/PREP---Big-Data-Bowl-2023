# credit to Nick Wan for the base code https://www.kaggle.com/code/nickwan/animated-gif-for-plays-python/notebook
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

# for mpl animation
import matplotlib.animation as animation
from matplotlib import rc
rc('animation', html='html5')

def get_play_by_frame(fid, ax, los, one_play):
    ax.cla()

    
  # get game and play IDs
    gid = one_play['gameId_x'].unique()[0]
    pid = one_play['playId_x'].unique()[0]

  # isolates a given frame within one play
    one_frame = one_play.loc[one_play['frameId_x']==fid]

    import numpy as np

    # kdeplot for heatmap (repeatedly called to have proper labeling)
    sns.kdeplot(data=one_frame, x='x_x',y='y_x', cmap="flare",
                         weights='modelPressure', fill=True, ax=ax).axvline(los, c='k', ls=':')
    # scatterplot for players (repeatedly called to have proper labeling)
    sns.scatterplot(x='x_x',y='y_x',data=one_frame, legend=False,
                         hue='team_x', ax=ax, s=50).axvline(los, c='k', ls=':')
    sns.kdeplot(data=one_frame, x='x_x',y='y_x',cmap="flare",
                         weights='modelPressure', fill=True, ax=ax).axvline(0, c='k', ls='-')
    sns.scatterplot(x='x_x',y='y_x',data=one_frame, legend=False,
                         hue='team_x', ax=ax, s=50).axvline(0, c='k', ls='-')
    sns.kdeplot(data=one_frame, x='x_x',y='y_x',cmap="flare",
                         weights='modelPressure', fill=True, ax=ax).axvline(100, c='k', ls='-')
    sns.scatterplot(x='x_x',y='y_x',data=one_frame, legend=False,
                         hue='team_x', ax=ax, s=50).axvline(100, c='k', ls='-')
    sns.kdeplot(data=one_frame, x='x_x',y='y_x',cmap="flare",
                         weights='modelPressure', fill=True, ax=ax).set_yticks([])
    sns.scatterplot(x='x_x',y='y_x',data=one_frame, legend=False,
                         hue='team_x', ax=ax, s=50).set_yticks([])
    sns.kdeplot(data=one_frame, x='x_x',y='y_x',cmap="flare",
                         weights='modelPressure', fill=True, ax=ax).set_ylabel('')
    sns.scatterplot(x='x_x',y='y_x',data=one_frame, legend=False,
                         hue='team_x', ax=ax, s=50).set_ylabel('')
    sns.kdeplot(data=one_frame, x='x_x',y='y_x',cmap="flare",
                         weights='modelPressure', fill=True, ax=ax).set_xlim(-10,110)
    sns.scatterplot(x='x_x',y='y_x',data=one_frame, legend=False,
                         hue='team_x', ax=ax, s=50).set_xlim(-10,110)
    sns.kdeplot(data=one_frame, x='x_x',y='y_x',cmap="flare",
                         weights='modelPressure', fill=True, ax=ax).set_ylim(0,54)
    sns.scatterplot(x='x_x',y='y_x',data=one_frame, legend=False,
                         hue='team_x', ax=ax, s=50).set_ylim(0,54)
    sns.kdeplot(data=one_frame, x='x_x',y='y_x',cmap="flare",
                         weights='modelPressure', fill=True, ax=ax).set_title(f"game {gid} play {pid}")
    sns.scatterplot(x='x_x',y='y_x',data=one_frame, legend=False,
                         hue='team_x', ax=ax, s=50).set_title(f"game {gid} play {pid}")
    sns.kdeplot(data=one_frame, x='x_x',y='y_x',cmap="flare",
                         weights='modelPressure', fill=True, ax=ax).set_facecolor("green")
    sns.scatterplot(x='x_x',y='y_x',data=one_frame, legend=False,
                         hue='team_x', ax=ax, s=50).set_facecolor("green")
    sns.despine(left=True)
    
    # add player circles for one specific player
    temp_frame = one_play[(one_play['frameId_x'] == fid)]

    if (not temp_frame.empty):
        one_frame2 = temp_frame[temp_frame['jerseyNumber'] == 43]
        one_frame2 = one_frame2.head(1)
    else:
        one_frame2 = pd.DataFrame()
    if (not one_frame2.empty):
        a = plt.Circle( (float(one_frame2['x_x']), float(one_frame2['y_x'])),
                                      radius=0.8 ,
                                      fill = False, color='black', animated=True )
        sns.kdeplot(data=one_frame, x='x_x',y='y_x',cmap="flare", legend=True,
                         weights='pressure', fill=True, ax=ax).add_patch(a)
        sns.scatterplot(x='x_x',y='y_x',data=one_frame, 
                         hue='team_x', ax=ax, s=50).add_patch(a)
    plt.show()


def animate_play(one_play):    
    gid = one_play['gameId_x'].unique()[0]
    pid = one_play['playId_x'].unique()[0]

  # get line of scrimmage info from the football X location from the  first frame of data 
    los = one_play.loc[(one_play['frameId_x']==1) & (one_play['team_x']=='football'), 'x_x'].values[0]

  # set figure size; this is hard coded but seemed to work well  
    fig = plt.figure(figsize=(14.4, 6.4))

  # get current axis of the figure
    ax = fig.gca()

  # matplotlib animate function
  # relies on get_play_by_frame()  
  # `interval = 100` is something like frames per second i think 
  # repeat=True is to have the animation continuously repeat  
    ani = animation.FuncAnimation(fig, get_play_by_frame, 
                                frames=one_play['frameId_x'].unique().shape[0],
                                interval=100, repeat=True, 
                                fargs=(ax,los,one_play,))
  # close the matplotlib figure when done (if you're batch processing gifs, this allows you to end one gif and begin another gif of a play)
    plt.close()

  # save the matplotlib animation as a gif
  # requires imagemagick or some sort of gif renderer
  # this works in google colab if you apt install imagemagick
    ani.save(f'{gid}_{pid}.gif', writer='imagemagick', fps=10)
    return ani

import pandas as pd
gameId = 2021091202
playId = 2543
newId = 297
# Load the data from week1-8.csv and pressure.csv
week1_8 = pd.read_csv('week1.csv')
pressure = pd.read_csv('model_data_pressure.csv')
week1 = week1_8[week1_8['playId'] == playId]
pressure = pressure[pressure['newId'] == newId]
# Join the two datasets on the jerseyNumber variable
result = pd.merge(week1, pressure, on='jerseyNumber', how='left')

# If a player exists in week1.csv but not in pressure.csv, give them a pressure of 0.01
result = result.fillna({'modelPressure': 0.10})

# Save the resulting dataframe to a new CSV file
data = result

play = data.loc[(data['gameId_x']==gameId) & (data['playId_x']==playId)]

animate_play(play)