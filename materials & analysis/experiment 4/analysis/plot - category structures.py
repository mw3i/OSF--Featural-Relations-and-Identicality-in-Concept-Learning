'''
This code will replicate the category structures figure in our Psychonomics 2020 poster

I apologize for how messy it is. I do a lot of the data cleaning in the same code as the plotting, which wasn't my best move

    - Matt
'''
import copy

import numpy as np 
import pandas as pd 

import matplotlib.pyplot as plt 
from matplotlib.gridspec import GridSpec

from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
bottom = cm.get_cmap('Oranges', 128)
top = cm.get_cmap('Blues_r', 128)

newcolors = np.vstack((top(np.linspace(.25, 1, 128)),
                       bottom(np.linspace(0,.75, 128))))
newcmp = ListedColormap(newcolors, name='OrangeBlue')


import parse

# parse.parse()

clean = lambda ax: [ax.set_xticks([]), ax.set_yticks([])]

catdata = pd.read_csv('../materials/stim gen/data1.csv')
catmap = {'Versicolor': 'blue', 'Setosa': 'orange'}
catmap_numeric = {'Versicolor': 0, 'Setosa': 1}

catmap_e2 = {'Alpha': 'blue', 'Beta': 'orange'}
catmap_numeric_e2 = {'Alpha': 0, 'Beta': 1}

catmap_strcolor = {'a': 'orange', 'b': 'blue', 'gen': 'black'}
catmap_numcolor = {'a': 1, 'b': 0, 'gen': .5}

# add relevant columns
catdata['Category_num'] = catdata['Category'].map(lambda x: catmap_numcolor[x])
catdata['Category'] = catdata['Category'].map(lambda x: catmap_strcolor[x])



# - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 




fig, ax = plt.subplots(
    1,2,
    figsize = [8,4.5],
    sharey = True
)
ax[0].scatter(
    catdata[catdata['Category']=='blue']['Dim1'] - catdata[catdata['Category']=='blue']['Dim2'],
    catdata[catdata['Category']=='blue']['Category_num'],
    c = catdata[catdata['Category']=='blue']['Category_num'],
    s = 460, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 2,
)
ax[0].scatter(
    catdata[catdata['Category']=='orange']['Dim1'] - catdata[catdata['Category']=='orange']['Dim2'],
    catdata[catdata['Category']=='orange']['Category_num'],
    c = catdata[catdata['Category']=='orange']['Category_num'],
    s = 460, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 2,
)
for row in catdata[catdata['Category']=='black'][['Dim1','Dim2']].values[2:,:]:
    ax[0].text(
        row[0] - row[1],
        .5,
        r'$\neq$',
        ha = 'center', va = 'center', fontsize = 28, fontweight = 'bold',
    )
for row in catdata[catdata['Category']=='black'][['Dim1','Dim2']].values[:2,:]:
    ax[0].text(
        row[0] - row[1],
        .5,
        r'$=$',
        ha = 'center', va = 'center', fontsize = 28, fontweight = 'bold',
    )


clean(ax[0])

ax[0].set_xticks([-1,0,1]) 
# ax[0].set_facecolor([.99,.99,.99])
ax[0].set_ylim([-.1,1.1]), ax[0].set_xlim([-1,1])




catdata2 = copy.deepcopy(catdata)
catdata2['Dim1'] = (-1 * catdata['Dim1']) + (catdata['Dim1'].mean() * 2)

ax[1].scatter(
    catdata2[catdata2['Category']=='blue']['Dim1'] - catdata2[catdata2['Category']=='blue']['Dim2'],
    catdata2[catdata2['Category']=='blue']['Category_num'],
    c = catdata2[catdata2['Category']=='blue']['Category_num'],
    s = 460, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 2,
)
ax[1].scatter(
    catdata2[catdata2['Category']=='orange']['Dim1'] - catdata2[catdata2['Category']=='orange']['Dim2'],
    catdata2[catdata2['Category']=='orange']['Category_num'],
    c = catdata2[catdata2['Category']=='orange']['Category_num'],
    s = 460, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 2,
)
for row in catdata2[catdata2['Category']=='black'][['Dim1','Dim2']].values:
    ax[1].text(
        row[0] - row[1],
        .5,
        r'$\neq$',
        ha = 'center', va = 'center', fontsize = 28, fontweight = 'bold',
    )


clean(ax[1])
ax[1].set_xticks([-1,0,1]) 
# ax[1].set_facecolor([.99,.99,.99])
ax[1].set_ylim([-.1,1.1]); ax[1].set_xlim([-1,1])




ax[0].set_ylabel('Category', fontsize = 18, fontweight = 'bold')
ax[0].set_xlabel('Feature 1 - Feature 2', fontsize = 18, fontweight = 'bold')
ax[1].set_xlabel('Feature 1 - Feature 2', fontsize = 18, fontweight = 'bold')


ax[0].set_title('Identicality\nStructure', fontsize = 25, fontweight = 'bold')
ax[1].set_title('Non-Identicality\nStructure', fontsize = 25, fontweight = 'bold')





# fig.set_facecolor([0,0,0,0])
plt.suptitle('Relational Representation')
plt.tight_layout()
plt.savefig('plots/E4 - structures (relational).png')
plt.close()







fig, ax = plt.subplots(
    1,2,
    figsize = [8,4.5],
    sharey = True
)

ax[0].scatter(
    *catdata[catdata['Category']=='blue'][['Dim1','Dim2']].values.T,
    c = catdata[catdata['Category']=='blue']['Category_num'],
    s = 460, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 2,
)

ax[0].scatter(
    *catdata[catdata['Category']=='orange'][['Dim1','Dim2']].values.T,
    c = catdata[catdata['Category']=='orange']['Category_num'],
    s = 460, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 2,
)

for row in catdata[catdata['Category']=='black'][['Dim1','Dim2']].values[2:,:]:
    ax[0].text(
        *row,
        r'$\neq$',
        ha = 'center', va = 'center', fontsize = 28, fontweight = 'bold',
    )
for row in catdata[catdata['Category']=='black'][['Dim1','Dim2']].values[:2,:]:
    ax[0].text(
        *row,
        r'$=$',
        ha = 'center', va = 'center', fontsize = 28, fontweight = 'bold',
    )

clean(ax[0])
ax[0].set_ylim([-.1,1.1]); ax[0].set_xlim([-.1,1.1])





ax[1].scatter(
    *catdata2[catdata2['Category']=='blue'][['Dim1','Dim2']].values.T,
    c = catdata2[catdata2['Category']=='blue']['Category_num'],
    s = 460, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 2,
)

ax[1].scatter(
    *catdata2[catdata2['Category']=='orange'][['Dim1','Dim2']].values.T,
    c = catdata2[catdata2['Category']=='orange']['Category_num'],
    s = 460, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 2,
)


for row in catdata2[catdata2['Category']=='black'][['Dim1','Dim2']].values:
    ax[1].text(
        *row,
        r'$\neq$',
        ha = 'center', va = 'center', fontsize = 28, fontweight = 'bold',
    )

clean(ax[1])
ax[1].set_ylim([-.1,1.1]); ax[1].set_xlim([-.1,1.1])




ax[0].set_ylabel('Feature 2', fontsize = 18, fontweight = 'bold')
ax[0].set_xlabel('Feature 1', fontsize = 18, fontweight = 'bold')
ax[1].set_xlabel('Feature 1', fontsize = 18, fontweight = 'bold')

plt.suptitle('Featural Representation')
ax[0].set_title('Identicality\nStructure', fontsize = 25, fontweight = 'bold')
ax[1].set_title('Non-Identicality\nStructure', fontsize = 25, fontweight = 'bold')




plt.tight_layout()
plt.savefig('plots/E4 - structures (featural).png')