 ## Python Standard Library
import sys
import os
import csv
import pickle

## External Dependencies
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


# from: https://stackoverflow.com/questions/22566284/matplotlib-how-to-plot-images-instead-of-points <-- thanks joe kington
def imscatter(x, y, image, ax=None, zoom=1):
    if ax is None:
        ax = plt.gca()
    try:
        image = plt.imread(image)
    except TypeError:
        # Likely already an array...
        pass
    im = OffsetImage(image, zoom=zoom)
    x, y = np.atleast_1d(x, y)
    artists = []
    for x0, y0 in zip(x, y):
        ab = AnnotationBbox(im, (x0, y0), xycoords='data', frameon=False)
        artists.append(ax.add_artist(ab))
    ax.update_datalim(np.column_stack([x, y]))
    ax.autoscale()
    return artists









fig, ax = plt.subplots(
    2,2,
    figsize = [15,15],
)



data1 = pd.read_csv('data1.csv')
data2 = pd.read_csv('data2.csv')



colmap = {
    'a': 'orange',
    'b': 'blue',
    'gen': 'black'
}
data1['color'] = data1['Category'].map(lambda x: colmap[x])

ax[0,0].scatter(
    data1['Dim1'],
    data1['Dim2'],
    c = data1['color'],
    s = 750,
)


for stim in data1.index:
    imscatter(
        data1.loc[stim,'Dim1'],
        data1.loc[stim,'Dim2'],
        'stim2/' + data1.loc[stim,'ID'] + '.png',
        ax = ax[0,1],
        zoom = .12,
    )







data2['color'] = data2['Category'].map(lambda x: colmap[x])

ax[1,0].scatter(
    data2['Dim1'],
    data2['Dim2'],
    c = data2['color'],
    s = 500,
)


for stim in data2.index:
    imscatter(
        data2.loc[stim,'Dim1'],
        data2.loc[stim,'Dim2'],
        'stim3/' + data2.loc[stim,'ID'] + '.png',
        ax = ax[1,1],
        zoom = .12,
    )




ax[0,0].set_ylabel('experimental\ncondition', fontsize = 20, fontweight = 'bold')
ax[1,0].set_ylabel('control\ncondition', fontsize = 20, fontweight = 'bold')






for a in ax.flatten(): [a.set_xticks([]), a.set_yticks([])]
# plt.tight_layout()
plt.savefig('disp.png')
