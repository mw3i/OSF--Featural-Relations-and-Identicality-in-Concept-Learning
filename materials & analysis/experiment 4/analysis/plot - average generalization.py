'''
This code will replicate the aggregate generalization profiles in our Psychonomics 2020 poster

I apologize for how messy it is. I do a lot of the data cleaning in the same code as the plotting, which wasn't my best move

    - Matt
'''
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
catmap_numeric = {'Versicolor': 0, 'Setosa': 1, 'gen': .5}


catmap_strcolor = {'a': 'orange', 'b': 'blue', 'gen': 'black'}


all_data = pd.read_csv('data/all_data_e1.csv')
c1_data = all_data[all_data['condition'] == 2].copy()  # <-- condition 1 is marked by label 2 (0,1 were used for prior pilot work, so that's why their named that)
c2_data = all_data[all_data['condition'] == 3].copy() # <-- condition 2 is marked by label 3

# add relevant columns
catdata['Category'] = catdata['Category'].map(lambda x: catmap_strcolor[x])

# - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



# # # # # # # # # # # # # # # # # # # # # # # # 
#==============================================
# 
#        CONDITION 1
# 
#==============================================
# # # # # # # # # # # # # # # # # # # # # # # # 
subjects = c1_data['id'].unique()


c1_data['response_color'] = c1_data['response'].map(lambda x: catmap[x])
c1_data['response_numeric'] = c1_data['response'].map(lambda x: catmap_numeric[x])
c1_data['catnum'] = c1_data['category'].map(lambda x: catmap_numeric[x])
c1_data['dim1'] = c1_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim1'].values[0])
c1_data['dim2'] = c1_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim2'].values[0])

s_acc = {}

for s, subject in enumerate(subjects):
    subjdata = c1_data[(c1_data['id'] == subject) & (c1_data['phase'] != 'classification_train')]
    subjdata_test = c1_data[(c1_data['id'] == subject) & (c1_data['phase'] == 'classification_test_gen') & (c1_data['category'] != 'gen')]
    s_acc[subject] = np.equal(subjdata_test['category'].values, subjdata_test['response'].values).mean()
c1_data['s_acc'] = c1_data['id'].map(lambda x: s_acc[x])



fig = plt.figure(
    figsize = [10,5.5]
)
d = 4
gs = GridSpec(6,10)


## plot average
avgdata = c1_data[
    c1_data['phase'] != 'classification_train'
].groupby('stim_id').mean()

av_ax = plt.subplot(gs[:6, :6])
a = av_ax.scatter(
    *avgdata[avgdata['catnum'] == 1.0][['dim1','dim2']].values.T,
    c = avgdata[avgdata['catnum'] == 1.0]['response_numeric'],
    s = 1050, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 3,
)
av_ax.scatter(
    *avgdata[avgdata['catnum'] == 0.0][['dim1','dim2']].values.T,
    c = avgdata[avgdata['catnum'] == 0.0]['response_numeric'],
    s = 1050, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 3,
)
av_ax.scatter(
    *avgdata[avgdata['catnum'] == .5][['dim1','dim2']].values.T,
    c = avgdata[avgdata['catnum'] == .5]['response_numeric'],
    s = 1050, marker = '*', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 3,
)

av_ax.set_title('Average Generalization | n = ' + str(len(c1_data['id'].unique())), fontsize = 17, fontweight = 'bold',)
clean(av_ax)
av_ax.set_ylabel('Feature 2', fontsize = 15, fontweight = 'bold')
av_ax.set_xlabel('Feature 1', fontsize = 15, fontweight = 'bold')

av_ax.set_facecolor([.99,.99,.99])
av_ax.set_ylim([-.1,1.01]); av_ax.set_xlim([-.1,1.01])

cbar = fig.colorbar(a, ax=av_ax)
cbar.set_ticks([0,.5, 1])
cbar.ax.set_yticklabels(['100%\nSetosa\nResponse', 'Chance', '100%\nVersicolor\nResponse'], fontsize = 13, fontweight = 'bold')





profile_1_sharp = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
ax = plt.subplot(gs[:3, 7:10])
ax.set_title('Sharp\nGeneralizer', fontsize = 15, fontweight = 'bold')
ax.scatter(
    *catdata[catdata['Category'] == 'orange'][['Dim1','Dim2']].values.T,
    c = [1] * catdata[catdata['Category'] == 'orange'].shape[0],
    s = 150, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *catdata[catdata['Category'] != 'orange'][['Dim1','Dim2']].values.T,
    c = [0] * catdata[catdata['Category'] != 'orange'].shape[0],
    s = 150, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.set_yticks([]); ax.set_xticks([])
ax.set_ylim([-.1,1.01]); ax.set_xlim([-.1,1.01])
ax.set_facecolor([.99,.99,.99])


profile_2_sim = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
ax = plt.subplot(gs[3:6, 7:10])
ax.set_title('Similarity\nGeneralizer', fontsize = 15, fontweight = 'bold')

ax.scatter(
    *catdata[catdata['Category'] != 'blue'][['Dim1','Dim2']].values.T,
    c = [1] * catdata[catdata['Category'] != 'blue'].shape[0],
    s = 150, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *catdata[catdata['Category'] == 'blue'][['Dim1','Dim2']].values.T,
    c = [0] * catdata[catdata['Category'] == 'blue'].shape[0],
    s = 150, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)

ax.set_yticks([]); ax.set_xticks([])
ax.set_ylim([-.1,1.01]); ax.set_xlim([-.1,1.01])
ax.set_facecolor([.99,.99,.99])




plt.suptitle('Identicality', fontweight = 'bold', fontsize = 28)
plt.tight_layout()

fig.set_facecolor([0,0,0,0])
plt.text(0.7, 0.5, 'Idealized Profiles:', fontsize=24, transform=plt.gcf().transFigure, rotation = 90, fontweight = 'bold', verticalalignment = 'center')
# plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.savefig('plots/E4 - Avg Generalization Identicality.png')
plt.close()


# - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



# # # # # # # # # # # # # # # # # # # # # # # # 
#==============================================
# 
#        CONDITION 2
# 
#==============================================
# # # # # # # # # # # # # # # # # # # # # # # # 

subjects = c2_data['id'].unique()

c2_data['response_color'] = c2_data['response'].map(lambda x: catmap[x])
c2_data['response_numeric'] = c2_data['response'].map(lambda x: catmap_numeric[x])
c2_data['catnum'] = c2_data['category'].map(lambda x: catmap_numeric[x])
c2_data['dim1'] = c2_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim1'].values[0])
c2_data['dim2'] = c2_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim2'].values[0])

s_acc = {}

for s, subject in enumerate(subjects):
    subjdata = c2_data[(c2_data['id'] == subject) & (c2_data['phase'] != 'classification_train')]
    subjdata_test = c2_data[(c2_data['id'] == subject) & (c2_data['phase'] == 'classification_test_gen') & (c2_data['category'] != 'gen')]
    s_acc[subject] = np.equal(subjdata_test['category'].values, subjdata_test['response'].values).mean()
c2_data['s_acc'] = c2_data['id'].map(lambda x: s_acc[x])



fig = plt.figure(
    figsize = [10,5.5]
)
d = 4
gs = GridSpec(6,10)


## plot average
avgdata = c2_data[
    c2_data['phase'] != 'classification_train'
].groupby('stim_id').mean()

av_ax = plt.subplot(gs[:6, :6])
avgdata['dim2'] = (-1 * avgdata['dim2']) + (avgdata['dim2'].mean() * 2)
a = av_ax.scatter(
    *avgdata[avgdata['catnum'] == 1.0][['dim1','dim2']].values.T,
    c = avgdata[avgdata['catnum'] == 1.0]['response_numeric'],
    s = 1050, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 3,
)
av_ax.scatter(
    *avgdata[avgdata['catnum'] == 0.0][['dim1','dim2']].values.T,
    c = avgdata[avgdata['catnum'] == 0.0]['response_numeric'],
    s = 1050, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 3,
)
av_ax.scatter(
    *avgdata[avgdata['catnum'] == .5][['dim1','dim2']].values.T,
    c = avgdata[avgdata['catnum'] == .5]['response_numeric'],
    s = 1050, marker = '*', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 3,
)

av_ax.set_title('Average Generalization | n = ' + str(len(c2_data['id'].unique())), fontsize = 17, fontweight = 'bold',)
clean(av_ax)
av_ax.set_ylabel('Feature 2', fontsize = 15, fontweight = 'bold')
av_ax.set_xlabel('Feature 1', fontsize = 15, fontweight = 'bold')

av_ax.set_facecolor([.99,.99,.99])
av_ax.set_ylim([-.1,1.01]); av_ax.set_xlim([-.1,1.01])

cbar = fig.colorbar(a, ax=av_ax)
cbar.set_ticks([0,.5, 1])
cbar.ax.set_yticklabels(['100%\nSetosa\nResponse', 'Chance', '100%\nVersicolor\nResponse'], fontsize = 13, fontweight = 'bold')





catdata_flipped = catdata.copy()
catdata_flipped['Dim2'] = (-1 * catdata_flipped['Dim2']) + (catdata_flipped['Dim2'].mean() * 2)

profile_1_sharp = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
ax = plt.subplot(gs[:3, 7:10])
ax.set_title('Sharp\nGeneralizer', fontsize = 15, fontweight = 'bold')
ax.scatter(
    *catdata_flipped[catdata_flipped['Category'] == 'orange'][['Dim1','Dim2']].values.T,
    c = [1] * catdata_flipped[catdata_flipped['Category'] == 'orange'].shape[0],
    s = 150, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *catdata_flipped[catdata_flipped['Category'] != 'orange'][['Dim1','Dim2']].values.T,
    c = [0] * catdata_flipped[catdata_flipped['Category'] != 'orange'].shape[0],
    s = 150, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.set_yticks([]); ax.set_xticks([])
ax.set_ylim([-.1,1.01]); ax.set_xlim([-.1,1.01])
ax.set_facecolor([.99,.99,.99])


profile_2_sim = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
ax = plt.subplot(gs[3:6, 7:10])
ax.set_title('Similarity\nGeneralizer', fontsize = 15, fontweight = 'bold')

ax.scatter(
    *catdata_flipped[catdata_flipped['Category'] != 'blue'][['Dim1','Dim2']].values.T,
    c = [1] * catdata_flipped[catdata_flipped['Category'] != 'blue'].shape[0],
    s = 150, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *catdata_flipped[catdata_flipped['Category'] == 'blue'][['Dim1','Dim2']].values.T,
    c = [0] * catdata_flipped[catdata_flipped['Category'] == 'blue'].shape[0],
    s = 150, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)

ax.set_yticks([]); ax.set_xticks([])
ax.set_ylim([-.1,1.01]); ax.set_xlim([-.1,1.01])
ax.set_facecolor([.99,.99,.99])




plt.suptitle('Non-Identicality', fontweight = 'bold', fontsize = 28)
plt.tight_layout()

fig.set_facecolor([0,0,0,0])
plt.text(0.7, 0.5, 'Idealized Profiles:', fontsize=24, transform=plt.gcf().transFigure, rotation = 90, fontweight = 'bold', verticalalignment = 'center')
# plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.savefig('plots/E4 - Avg Generalization Non-Identicality.png')
plt.close()


