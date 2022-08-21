'''
This code will replicate the learning curves in our Psychonomics 2020 poster

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
catmap_numeric = {'Versicolor': 0, 'Setosa': 1}

catmap_strcolor = {'a': 'orange', 'b': 'blue', 'gen': 'black'}
catmap_numcolor = {'a': 1, 'b': 0, 'gen': .5}


all_data_e1 = pd.read_csv('data/all_data_e1.csv')
c1_data = all_data_e1[all_data_e1['condition'] == 2].copy()  # <-- condition 1 is marked by label 2 (0,1 were used for prior pilot work, so that's why their named that)
c2_data = all_data_e1[all_data_e1['condition'] == 3].copy() # <-- condition 2 is marked by label 3

# add relevant columns
catdata['Category_num'] = catdata['Category'].map(lambda x: catmap_numcolor[x])
catdata['Category'] = catdata['Category'].map(lambda x: catmap_strcolor[x])


# - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

fig = plt.figure(
    figsize = [8,5]
)
# d = 5
# gs = GridSpec(len(subjects_c1) // d + 3, d)


subjects_c1 = c1_data['id'].unique()

c1_data['response_color'] = c1_data['response'].map(lambda x: catmap[x])
c1_data['response_numeric'] = c1_data['response'].map(lambda x: catmap_numeric[x])
c1_data['dim1'] = c1_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim1'].values[0])
c1_data['dim2'] = c1_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim2'].values[0])



c2_data['response_color'] = c2_data['response'].map(lambda x: catmap[x])
c2_data['response_numeric'] = c2_data['response'].map(lambda x: catmap_numeric[x])
c2_data['dim1'] = c2_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim1'].values[0])
c2_data['dim2'] = c2_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim2'].values[0])
c2_data['dim2'] = (-1 * c2_data['dim2']) + (c2_data['dim2'].mean() * 2)



# print(c1_data['stim_id'])
c1acc = c1_data[
    (c1_data['phase'] == 'classification_test_gen') & (c1_data['isCorrect'] != 'gen') 
].copy()






max_trials_possible = 16 * 5 # <-- 5 blocks total, max of 16*5 trials

blocks_c1 = []
vals_c1 = []

for s, subject in enumerate(c1_data['id'].unique()):
    subjdata = c1_data[(c1_data['id'] == subject) & (c1_data['phase'] == 'classification_train')]

    blocks_c1 += subjdata['block'].values.tolist()
    vals_c1 += subjdata['isCorrect'].replace({'False': 0, 'True': 1}).values.tolist()

    max_trial = subjdata['trial'].max()
    if max_trial < 16*4:
        for i in range(max_trial, max_trials_possible):
            blocks_c1.append(i // 16)
            vals_c1.append(1)

c1_train = pd.DataFrame({'block': blocks_c1, 'isCorrect': vals_c1})



blocks_c2 = []
vals_c2 = []

for s, subject in enumerate(c2_data['id'].unique()):
    subjdata = c2_data[(c2_data['id'] == subject) & (c2_data['phase'] == 'classification_train')]

    blocks_c2 += subjdata['block'].values.tolist()
    vals_c2 += subjdata['isCorrect'].replace({'False': 0, 'True': 1}).values.tolist()

    max_trial = subjdata['trial'].max()
    if max_trial < max_trials_possible:
        for i in range(max_trial, max_trials_possible):
            blocks_c2.append(i // 16)
            vals_c2.append(1)

c2_train = pd.DataFrame({'block': blocks_c2, 'isCorrect': vals_c2})



plt.plot(
    range(1,5+1),
    c1_train.groupby('block').mean()['isCorrect'],
    linewidth = 5, alpha = .9, color = 'orange'
)
plt.plot(
    range(1,5+1),
    c2_train.groupby('block').mean()['isCorrect'],
    linewidth = 5, alpha = .9, color = 'purple'
)


plt.scatter(
    range(1,5+1),
    c1_train.groupby('block').mean()['isCorrect'],
    marker = 'o', s = 200, edgecolor = 'orange', linewidth = 3, color = 'white', alpha = 1, zorder = 100, label = 'E1-C1',
)
plt.scatter(
    range(1,5+1),
    c2_train.groupby('block').mean()['isCorrect'],
    marker = '^', s = 200, edgecolor = 'purple', linewidth = 3, color = 'white', alpha = 1, zorder = 100, label = 'E1-C2',
)



plt.axhline(
    .5, linestyle = '--', linewidth = 5, color = 'black', alpha = .5
)



plt.xticks(range(1,5+1), [str(i) for i in range(1,5+1)], fontweight = 'bold', fontsize = 13)
plt.yticks(np.arange(.4,1.1,.1), [str(int(np.round(i,2) * 100)) + '%' for i in np.arange(.4,1.1,.1)], fontweight = 'bold', fontsize = 13)

plt.ylim([.4,1.01])


plt.xlabel('Training Blocks', fontweight = 'bold', fontsize = 20)
plt.ylabel('Accuracy', fontweight = 'bold', fontsize = 20)
plt.title('Learning Accuracy over Time', fontweight = 'bold', fontsize = 25)


plt.legend(loc = 'lower right')

fig.set_facecolor([0,0,0,0])

plt.tight_layout()
plt.savefig('plots/E4 - learning curves.png')
plt.close()

