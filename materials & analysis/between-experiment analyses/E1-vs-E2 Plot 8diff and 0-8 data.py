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

c3c_structure = np.array([
    [0,0],
    [8,1],
])


gensE1 = pd.read_csv('../experiment 1/analysis/data/gens.csv')
gensE3 = pd.read_csv('../experiment 3/analysis/data/test.csv')

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
gensE3['s1_val'] = gensE3['s1'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)
gensE3['s2_val'] = gensE3['s2'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)

gensE3['diff'] = np.abs(gensE3['s1_val'] - gensE3['s2_val'])

gensE3['response'] = gensE3['response'].replace({'yes': 1, 'no': 0})
gensE3['response'] = gensE3['response'].replace({'respA': 1, 'respB': 0})

gensE3['response_standard'] = gensE3['response']

c1E3 = gensE3[(gensE3['condition'] == 1) & (gensE3['block'] == 0)].groupby('diff').mean()['response_standard']
c2E3 = gensE3[(gensE3['condition'] == 2) & (gensE3['block'] == 0)].groupby('diff').mean()['response_standard']
c3E3 = gensE3[(gensE3['condition'] == 3) & (gensE3['block'] == 0)].groupby('diff').mean()['response_standard']

c1nE3 = gensE3[gensE3['condition'] == 1]['id'].unique().shape[0]
c2nE3 = gensE3[gensE3['condition'] == 2]['id'].unique().shape[0]
c3nE3 = gensE3[gensE3['condition'] == 3]['id'].unique().shape[0]








# Plot stuff
fig, ax = plt.subplots(1,1, figsize = [4,4])

ax.scatter(
    range(c1E1.shape[0]),
    c1E1.values,
    label = 'E1'
)
ax.plot(
    range(c1E1.shape[0]),
    c1E1.values
)
ax.scatter(
    range(c1E3.shape[0]),
    c1E3.values,
    label = 'E3', marker = '*', s = 100,
)
ax.plot(
    range(c1E3.shape[0]),
    c1E3.values
)


ax.set_xticks(range(0,17,2))
ax.set_ylim([-.1, 1.1])
ax.set_yticks([0,1])
ax.set_yticklabels([0,1])
ax.set_xlabel('|feature 1 - feature 2|')
ax.legend()

ax.set_ylabel('Response Probability')


ax.set_title('E1 (n = ' + str(int(c1nE1)) + ')\n-vs-\nE3 (n = ' + str(int(c1nE3)) + ')')


# ax.set_title('condition 1\n(classification)')

# stats.ttest_ind

plt.tight_layout()
plt.savefig('E1 8-diff -vs- E3 0-8.png')



