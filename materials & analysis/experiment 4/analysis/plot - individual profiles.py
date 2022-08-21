'''
This code will replicate the individual subject generalization profiles in our Psychonomics 2020 poster

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
catmap_numcolor = {'a': 1, 'b': 0, 'gen': .5}


all_data = pd.read_csv('data/all_data_e1.csv')
c1_data = all_data[all_data['condition'] == 2].copy()  # <-- condition 1 is marked by label 2 (0,1 were used for prior pilot work, so that's why their named that)
c2_data = all_data[all_data['condition'] == 3].copy() # <-- condition 2 is marked by label 3


# add relevant columns
catdata['Category_num'] = catdata['Category'].map(lambda x: catmap_numcolor[x])
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
subjects_c1 = c1_data['id'].unique()

c1_data['response_color'] = c1_data['response'].map(lambda x: catmap[x])
c1_data['response_numeric'] = c1_data['response'].map(lambda x: catmap_numeric[x])
c1_data['category_numeric'] = c1_data['category'].map(lambda x: catmap_numeric[x])
c1_data['dim1'] = c1_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim1'].values[0])
c1_data['dim2'] = c1_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim2'].values[0])


c1_s_acc = {}

fig = plt.figure(
    figsize = [14,30]
)
d = 5
gs = GridSpec(len(subjects_c1) // d + 3, d)

plt.suptitle('Experiment 4 | Identicality\nAverages\n', fontsize = '25', fontweight = 'bold')

for s, subject in enumerate(subjects_c1):
    ax = plt.subplot(gs[s // d + 2, s % d])
    subjdata = c1_data[(c1_data['id'] == subject) & (c1_data['phase'] != 'classification_train')]

    # print(subjdata['response_numeric'])
    # print(subjdata.columns)
    # exit()

    ax.scatter(
        *subjdata[subjdata['response_numeric'] == 0][['dim1','dim2']].values.T,
        c = subjdata[subjdata['response_numeric'] == 0]['response_numeric'],
        s = 160, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
        edgecolor = [[0,0,0,1] if p == 'classification_test_gen' else [0,0,0,0] for p in subjdata[subjdata['response_numeric'] == 0]['phase'].values],
        linewidth = 1,
    )
    ax.scatter(
        *subjdata[subjdata['response_numeric'] == 1][['dim1','dim2']].values.T,
        c = subjdata[subjdata['response_numeric'] == 1]['response_numeric'],
        s = 160, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
        edgecolor = [[0,0,0,1] if p == 'classification_test_gen' else [0,0,0,0] for p in subjdata[subjdata['response_numeric'] == 1]['phase'].values],
        linewidth = 1,
    )


    subjdata_test = c1_data[(c1_data['id'] == subject) & (c1_data['phase'] == 'classification_test_gen') & (c1_data['category'] != 'gen')]
    # print(subjdata_test[['category', 'response']])
    # print(subjdata_test['category'] == subjdata_test['response'])
    ax.set_title(
        'id: ' + str(s) + ' | acc: ' + str(np.equal(subjdata_test['category'].values, subjdata_test['response'].values).mean().round(2)), fontweight = 'bold'
    )

    c1_s_acc[subject] = np.equal(subjdata_test['category'].values, subjdata_test['response'].values).mean()

    clean(ax)
    ax.set_facecolor([.9,.9,.9])
    ax.set_ylim([-.1,1.1]); ax.set_xlim([-.1,1.1])


c1_data['s_acc'] = c1_data['id'].map(lambda x: c1_s_acc[x])






## div ax
div_ax = plt.subplot(gs[1:2,:])
div_ax.imshow(np.ones([1,100]), cmap = 'binary', vmin=0, vmax=1)
div_ax.set_xlabel('\nIndividual Subjects:', fontsize=25, fontweight = 'bold')
div_ax.set_xticks([]); div_ax.set_yticks([]); 







## plot actual
ax = plt.subplot(gs[0, 0])
ax.scatter(
    *catdata[catdata['Category']=='orange'][['Dim1','Dim2']].values.T,
    c = catdata[catdata['Category']=='orange']['Category_num'],
    s = 200, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *catdata[catdata['Category']=='blue'][['Dim1','Dim2']].values.T,
    c = catdata[catdata['Category']=='blue']['Category_num'],
    s = 200, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *catdata[catdata['Category']=='black'][['Dim1','Dim2']].values.T,
    c = catdata[catdata['Category']=='black']['Category'],
    s = 200, marker = '*', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)

ax.set_xlabel('Actual Category\nStructure', fontsize = 18)
clean(ax)
ax.set_facecolor([.9,.9,.9])
ax.set_ylim([-.1,1.1]); ax.set_xlim([-.1,1.1])



## plot average
avgdata = c1_data[
    c1_data['phase'] != 'classification_train'
].groupby('stim_id').mean()

ax = plt.subplot(gs[0, 1])

ax.scatter(
    *avgdata[avgdata['category_numeric']==0][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==0]['response_numeric'],
    s = 200, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *avgdata[avgdata['category_numeric']==1][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==1]['response_numeric'],
    s = 200, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *avgdata[avgdata['category_numeric']==.5][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==.5]['response_numeric'],
    s = 400, marker = '*', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.set_xlabel('Average\nn = ' + str(len(c1_data['id'].unique())), fontsize = 18)
clean(ax)
ax.set_facecolor([.9,.9,.9])
ax.set_ylim([-.1,1.1]); ax.set_xlim([-.1,1.1])




## plot average <90
avgdata = c1_data[
    (c1_data['phase'] != 'classification_train') & 
    (c1_data['s_acc'] >= .9)
].groupby('stim_id').mean()

ax = plt.subplot(gs[0, 2])
ax.scatter(
    *avgdata[avgdata['category_numeric']==0][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==0]['response_numeric'],
    s = 200, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *avgdata[avgdata['category_numeric']==1][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==1]['response_numeric'],
    s = 200, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *avgdata[avgdata['category_numeric']==.5][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==.5]['response_numeric'],
    s = 400, marker = '*', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.set_xlabel('Average >90%\nn = ' + str(len(c1_data[(c1_data['s_acc'] >= .9)]['id'].unique())), fontsize = 18)
clean(ax)
ax.set_facecolor([.9,.9,.9])
ax.set_ylim([-.1,1.1]); ax.set_xlim([-.1,1.1])






## plot average >90
avgdata = c1_data[
    (c1_data['phase'] != 'classification_train') & 
    (c1_data['s_acc'] <= .9)
].groupby('stim_id').mean()

ax = plt.subplot(gs[0, 3])
a = ax.scatter(
    *avgdata[avgdata['category_numeric']==0][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==0]['response_numeric'],
    s = 200, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *avgdata[avgdata['category_numeric']==1][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==1]['response_numeric'],
    s = 200, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *avgdata[avgdata['category_numeric']==.5][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==.5]['response_numeric'],
    s = 400, marker = '*', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.set_xlabel('Average <90%\nn = ' + str(len(c1_data[(c1_data['s_acc'] <= .9)]['id'].unique())), fontsize = 18)
clean(ax)
ax.set_facecolor([.9,.9,.9])
ax.set_ylim([-.1,1.1]); ax.set_xlim([-.1,1.1])

cbar_ax = plt.subplot(gs[0,4])
cbar = fig.colorbar(a, ax = cbar_ax)
cbar.set_ticks([0,.5, 1])
cbar.ax.set_yticklabels(['100%\nSetosa\nResponse', 'Chance', '100%\nVersicolor\nResponse'], fontsize = 13, fontweight = 'bold')
cbar_ax.remove()





plt.tight_layout()
plt.savefig('plots/E4 - Individual Profiles Identicality.png')
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

subjects_c2 = c2_data['id'].unique()

# add relevant columns
c2_data['response_color'] = c2_data['response'].map(lambda x: catmap[x])
c2_data['response_numeric'] = c2_data['response'].map(lambda x: catmap_numeric[x])
c2_data['category_numeric'] = c2_data['category'].map(lambda x: catmap_numeric[x])
c2_data['dim1'] = c2_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim1'].values[0])
c2_data['dim2'] = c2_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim2'].values[0])

c2_data['dim2'] = (-1 * c2_data['dim2']) + (c2_data['dim2'].mean() * 2)


c2_s_acc = {}

fig = plt.figure(
    figsize = [14,27]
)
d = 5
gs = GridSpec(len(subjects_c2) // d + 3, d)

plt.suptitle('Experiment 4 | Non-Identicality\nAverages\n', fontsize = '25', fontweight = 'bold')

for s, subject in enumerate(subjects_c2):
    ax = plt.subplot(gs[s // d + 2, s % d])
    subjdata = c2_data[(c2_data['id'] == subject) & (c2_data['phase'] != 'classification_train')]

    ax.scatter(
        *subjdata[subjdata['response_numeric'] == 0][['dim1','dim2']].values.T,
        c = subjdata[subjdata['response_numeric'] == 0]['response_numeric'],
        s = 160, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
        edgecolor = [[0,0,0,1] if p == 'classification_test_gen' else [0,0,0,0] for p in subjdata[subjdata['response_numeric'] == 0]['phase'].values],
        linewidth = 1,
    )
    ax.scatter(
        *subjdata[subjdata['response_numeric'] == 1][['dim1','dim2']].values.T,
        c = subjdata[subjdata['response_numeric'] == 1]['response_numeric'],
        s = 160, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
        edgecolor = [[0,0,0,1] if p == 'classification_test_gen' else [0,0,0,0] for p in subjdata[subjdata['response_numeric'] == 1]['phase'].values],
        linewidth = 1,
    )


    subjdata_test = c2_data[(c2_data['id'] == subject) & (c2_data['phase'] == 'classification_test_gen') & (c2_data['category'] != 'gen')]
    # print(subjdata_test[['category', 'response']])
    # print(subjdata_test['category'] == subjdata_test['response'])
    ax.set_title(
        'id: ' + str(s) + ' | acc: ' + str(np.equal(subjdata_test['category'].values, subjdata_test['response'].values).mean().round(2)), fontweight = 'bold'
    )

    c2_s_acc[subject] = np.equal(subjdata_test['category'].values, subjdata_test['response'].values).mean()

    clean(ax)
    ax.set_facecolor([.9,.9,.9])
    ax.set_ylim([-.1,1.1]); ax.set_xlim([-.1,1.1])


c2_data['s_acc'] = c2_data['id'].map(lambda x: c2_s_acc[x])






## div ax
div_ax = plt.subplot(gs[1:2,:])
div_ax.imshow(np.ones([1,100]), cmap = 'binary', vmin=0, vmax=1)
div_ax.set_xlabel('\nIndividual Subjects:', fontsize=25, fontweight = 'bold')
div_ax.set_xticks([]); div_ax.set_yticks([]); 







## plot actual
catdata_flipped = catdata.copy()
catdata_flipped['Dim2'] = (-1 * catdata_flipped['Dim2']) + (catdata_flipped['Dim2'].mean() * 2)

ax = plt.subplot(gs[0, 0])
ax.scatter(
    *catdata_flipped[catdata_flipped['Category']=='orange'][['Dim1','Dim2']].values.T,
    c = catdata_flipped[catdata_flipped['Category']=='orange']['Category_num'],
    s = 200, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *catdata_flipped[catdata_flipped['Category']=='blue'][['Dim1','Dim2']].values.T,
    c = catdata_flipped[catdata_flipped['Category']=='blue']['Category_num'],
    s = 200, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *catdata_flipped[catdata_flipped['Category']=='black'][['Dim1','Dim2']].values.T,
    c = catdata_flipped[catdata_flipped['Category']=='black']['Category'],
    s = 200, marker = '*', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.set_xlabel('Actual Category\nStructure', fontsize = 18)
clean(ax)
ax.set_facecolor([.9,.9,.9])
ax.set_ylim([-.1,1.1]); ax.set_xlim([-.1,1.1])



## plot average
avgdata = c2_data[
    c2_data['phase'] != 'classification_train'
].groupby('stim_id').mean()

ax = plt.subplot(gs[0, 1])
ax.scatter(
    *avgdata[avgdata['category_numeric']==0][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==0]['response_numeric'],
    s = 200, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *avgdata[avgdata['category_numeric']==1][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==1]['response_numeric'],
    s = 200, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *avgdata[avgdata['category_numeric']==.5][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==.5]['response_numeric'],
    s = 400, marker = '*', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax
ax.set_xlabel('Average\nn = ' + str(len(c2_data['id'].unique())), fontsize = 18)
clean(ax)
ax.set_facecolor([.9,.9,.9])
ax.set_ylim([-.1,1.1]); ax.set_xlim([-.1,1.1])




## plot average <90
avgdata = c2_data[
    (c2_data['phase'] != 'classification_train') & 
    (c2_data['s_acc'] >= .9)
].groupby('stim_id').mean()

ax = plt.subplot(gs[0, 2])
ax.scatter(
    *avgdata[avgdata['category_numeric']==0][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==0]['response_numeric'],
    s = 200, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *avgdata[avgdata['category_numeric']==1][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==1]['response_numeric'],
    s = 200, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *avgdata[avgdata['category_numeric']==.5][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==.5]['response_numeric'],
    s = 400, marker = '*', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax
ax.set_xlabel('Average >90%\nn = ' + str(len(c2_data[(c2_data['s_acc'] >= .9)]['id'].unique())), fontsize = 18)
clean(ax)
ax.set_facecolor([.9,.9,.9])
ax.set_ylim([-.1,1.1]); ax.set_xlim([-.1,1.1])






## plot average >90
avgdata = c2_data[
    (c2_data['phase'] != 'classification_train') & 
    (c2_data['s_acc'] <= .9)
].groupby('stim_id').mean()

ax = plt.subplot(gs[0, 3])
a = ax.scatter(
    *avgdata[avgdata['category_numeric']==0][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==0]['response_numeric'],
    s = 200, marker = '^', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *avgdata[avgdata['category_numeric']==1][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==1]['response_numeric'],
    s = 200, marker = 'o', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax.scatter(
    *avgdata[avgdata['category_numeric']==.5][['dim1','dim2']].values.T,
    c = avgdata[avgdata['category_numeric']==.5]['response_numeric'],
    s = 400, marker = '*', cmap = newcmp, vmin = 0, vmax = 1,
    edgecolor = 'black',
    linewidth = 1,
)
ax
ax.set_xlabel('Average <90%\nn = ' + str(len(c2_data[(c2_data['s_acc'] <= .9)]['id'].unique())), fontsize = 18)
clean(ax)
ax.set_facecolor([.9,.9,.9])
ax.set_ylim([-.1,1.1]); ax.set_xlim([-.1,1.1])

cbar_ax = plt.subplot(gs[0,4])
cbar = fig.colorbar(a, ax = cbar_ax)
cbar.set_ticks([0,.5, 1])
cbar.ax.set_yticklabels(['100%\nSetosa\nResponse', 'Chance', '100%\nVersicolor\nResponse'], fontsize = 13, fontweight = 'bold')
cbar_ax.remove()





plt.tight_layout()
plt.savefig('plots/E4 - Individual Profiles Non-Identicality.png')
plt.close()




