import numpy as np
import pandas as pd 

import matplotlib.pyplot as plt

c1_structure = np.array([
    [8,1]
])

c2_structure = np.array([
    [1,1]
])

c3_structure = np.array([
    [0,1]
])



gensE1 = pd.read_csv('../experiment 1/analysis/data/gens.csv')
gensE2 = pd.read_csv('../experiment 2/analysis/data/gens.csv')

# ^ 'Unnamed: 0', 'trial', 'block', 's1', 's2', 'connected', 'response', 'accuracy', 'rt', 'counter'

# clean a
gensE1['s1_val'] = gensE1['s1'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)
gensE1['s2_val'] = gensE1['s2'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)

gensE1['diff'] = np.abs(gensE1['s1_val'] - gensE1['s2_val'])

gensE1['response'] = gensE1['response'].replace({'yes': 1, 'no': 0})
gensE1['response'] = gensE1['response'].replace({'respA': 1, 'respB': 0})

gensE1['response_standard'] = gensE1['response']

c1E1 = gensE1[(gensE1['condition'] == 2) & (gensE1['block'] == 0)].groupby('diff').mean()['response_standard']
c2E1 = gensE1[(gensE1['condition'] == 3) & (gensE1['block'] == 0)].groupby('diff').mean()['response_standard']
c3E1 = gensE1[(gensE1['condition'] == 4) & (gensE1['block'] == 0)].groupby('diff').mean()['response_standard']
# ^ it's 2,3,4 because there was another condition not mentioned

c1nE1 = gensE1[gensE1['condition'] == 2]['id'].unique().shape[0]
c2nE1 = gensE1[gensE1['condition'] == 3]['id'].unique().shape[0]
c3nE1 = gensE1[gensE1['condition'] == 4]['id'].unique().shape[0]


# clean b
gensE2['s1_val'] = gensE2['s1'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)
gensE2['s2_val'] = gensE2['s2'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)

gensE2['diff'] = np.abs(gensE2['s1_val'] - gensE2['s2_val'])

gensE2['response'] = gensE2['response'].replace({'yes': 1, 'no': 0})
gensE2['response'] = gensE2['response'].replace({'respA': 1, 'respB': 0})

gensE2['response_standard'] = gensE2['response']

c1E2 = gensE2[(gensE2['condition'] == 1) & (gensE2['block'] == 0)].groupby('diff').mean()['response_standard']
c2E2 = gensE2[(gensE2['condition'] == 2) & (gensE2['block'] == 0)].groupby('diff').mean()['response_standard']
c3E2 = gensE2[(gensE2['condition'] == 3) & (gensE2['block'] == 0)].groupby('diff').mean()['response_standard']

c1nE2 = gensE2[gensE2['condition'] == 1]['id'].unique().shape[0]
c2nE2 = gensE2[gensE2['condition'] == 2]['id'].unique().shape[0]
c3nE2 = gensE2[gensE2['condition'] == 3]['id'].unique().shape[0]








# Plot stuff
fig, ax = plt.subplots(1,3, figsize = [12,4])

ax[0].scatter(
    range(c1E1.shape[0]),
    c1E1.values,
    label = 'E1'
)
ax[0].plot(
    range(c1E1.shape[0]),
    c1E1.values
)
ax[0].scatter(
    range(c1E2.shape[0]),
    c1E2.values,
    label = 'E2', marker = '*', s = 100,
)
ax[0].plot(
    range(c1E2.shape[0]),
    c1E2.values
)
ax[0].scatter(
    *c1_structure.T,
    c = c1_structure[:,-1],
    alpha = .6, cmap = 'binary', vmin = 0, vmax = 1, marker = 'o', s = 200, edgecolor = 'black', linewidth = 2,
)




ax[1].scatter(
    range(c2E1.shape[0]),
    c2E1.values,
    label = 'E1'
)
ax[1].plot(
    range(c2E1.shape[0]),
    c2E1.values
)
ax[1].scatter(
    range(c2E2.shape[0]),
    c2E2.values,
    label = 'E2', marker = '*', s = 100,
)
ax[1].plot(
    range(c2E2.shape[0]),
    c2E2.values
)
ax[1].scatter(
    *c2_structure.T,
    c = c2_structure[:,-1],
    alpha = .6, cmap = 'binary', vmin = 0, vmax = 1, marker = 'o', s = 200, edgecolor = 'black', linewidth = 2,
)



ax[2].scatter(
    range(c3E1.shape[0]),
    c3E1.values,
    label = 'E1', 
)
ax[2].plot(
    range(c3E1.shape[0]),
    c3E1.values
)
ax[2].scatter(
    range(c3E2.shape[0]),
    c3E2.values,
    label = 'E2', marker = '*', s = 100,
)
ax[2].plot(
    range(c3E2.shape[0]),
    c3E2.values
)
ax[2].scatter(
    *c3_structure.T,
    c = c3_structure[:,-1],
    alpha = .6, cmap = 'binary', vmin = 0, vmax = 1, marker = 'o', s = 200, edgecolor = 'black', linewidth = 2,
)

for a in ax.flatten():
    a.set_xticks(range(0,17,2))
    a.set_ylim([-.1, 1.1])
    a.set_yticks([0,1])
    a.set_yticklabels([0,1])
    a.set_xlabel('|feature 1 - feature 2|')
    a.legend()

ax[0].set_ylabel('Response Probability')


ax[0].set_title('E1 (n = ' + str(int(c1nE1)) + ')\n-vs-\nE2 (n = ' + str(int(c1nE2)) + ')')
ax[1].set_title('E1 (n = ' + str(int(c2nE1)) + ')\n-vs-\nE2 (n = ' + str(int(c2nE2)) + ')')
ax[2].set_title('E1 (n = ' + str(int(c3nE1)) + ')\n-vs-\nE2 (n = ' + str(int(c3nE2)) + ')')


# ax[0].set_title('condition 1\n(classification)')

# stats.ttest_ind

plt.tight_layout()
plt.savefig('E1 -vs- E2.png')



import scipy.stats as stats

# compare e1 with e2: diff8 critical item

print(gensE1[(gensE1['condition'] == 2) & (gensE1['diff'] == 8)]['response_standard'].mean().round(3), '|', gensE1[(gensE1['condition'] == 2) & (gensE1['diff'] == 8)]['response_standard'].std().round(3))
print(gensE2[(gensE2['condition'] == 1) & (gensE2['diff'] == 8)]['response_standard'].mean().round(3), '|', gensE2[(gensE2['condition'] == 1) & (gensE2['diff'] == 8)]['response_standard'].std().round(3))
    
t,p = stats.ttest_ind(
    gensE1[(gensE1['condition'] == 2) & (gensE1['diff'] == 8)].groupby('id').mean()['response_standard'],
    gensE2[(gensE2['condition'] == 1) & (gensE2['diff'] == 8)].groupby('id').mean()['response_standard'],
)
print('e1vb diff8-8:', t.round(3), '|', 'p:', p.round(3))

# compare e1 with e2: diff0 first non-target

print(gensE1[(gensE1['condition'] == 4) & (gensE1['diff'] == 1)]['response_standard'].mean().round(3), '|', gensE1[(gensE1['condition'] == 4) & (gensE1['diff'] == 1)]['response_standard'].std().round(3))
print(gensE2[(gensE2['condition'] == 3) & (gensE2['diff'] == 1)]['response_standard'].mean().round(3), '|', gensE2[(gensE2['condition'] == 3) & (gensE2['diff'] == 1)]['response_standard'].std().round(3))

t,p = stats.ttest_ind(
    gensE2[(gensE2['condition'] == 3) & (gensE2['diff'] == 1)].groupby('id').mean()['response_standard'],
    gensE1[(gensE1['condition'] == 4) & (gensE1['diff'] == 1)].groupby('id').mean()['response_standard'],
)
print('E1 vs E2 diff0-1:', t.round(3), '|', 'p:', p.round(3))




