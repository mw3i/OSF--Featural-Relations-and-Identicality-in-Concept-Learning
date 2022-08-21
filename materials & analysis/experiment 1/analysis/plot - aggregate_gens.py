import numpy as np
import pandas as pd 

import matplotlib.pyplot as plt


# c1_structure = np.array([
# 	[1,0],
# 	[8,1]
# ])

c2_structure = np.array([
	[8,1]
])

c3_structure = np.array([
	[1,1]
])

c4_structure = np.array([
	[0,1]
])



gens = pd.read_csv('data/gens.csv')
# ^ 'Unnamed: 0', 'trial', 'block', 's1', 's2', 'connected', 'response', 'accuracy', 'rt', 'counter'

gens['s1_val'] = gens['s1'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)
gens['s2_val'] = gens['s2'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)

gens['diff'] = np.abs(gens['s1_val'] - gens['s2_val'])

gens['response'] = gens['response'].replace({'yes': 1, 'no': 0})

gens['response_standard'] = gens['response']
gens.loc[gens['condition'] == 1, 'response_standard'] = gens.loc[gens['condition'] == 1].apply(lambda x: np.abs((1 - x['response']) - (1 - x['counter'])), axis = 1)

# print(gens['condition'])

c2 = gens[gens['condition'] == 2].groupby('diff').mean()['response_standard']
c3 = gens[gens['condition'] == 3].groupby('diff').mean()['response_standard']
c4 = gens[gens['condition'] == 4].groupby('diff').mean()['response_standard']

c2n = gens[gens['condition'] == 2]['id'].unique().shape[0]
c3n = gens[gens['condition'] == 3]['id'].unique().shape[0]
c4n = gens[gens['condition'] == 4]['id'].unique().shape[0]


fig, ax = plt.subplots(1,3, figsize = [9,3.1])


ax[0].plot(
	range(c2.shape[0]),
	c2.values,
	linewidth = 2, color = 'black', zorder = 0,
)
ax[0].scatter(
	range(c2.shape[0]),
	c2.values,
	s = 70,
)
ax[0].scatter(
	*c2_structure.T,
	c = c2_structure[:,-1],
	alpha = .6, cmap = 'binary', vmin = 0, vmax = 1, marker = 'o', s = 200, edgecolor = 'black', linewidth = 2,
)
ax[0].axvline(c2_structure[0,0], alpha = .6, linewidth = 2, color = 'red', linestyle='--', zorder = 0)





ax[1].plot(
	range(c3.shape[0]),
	c3.values,
	linewidth = 2, color = 'black', zorder = 0
)
ax[1].scatter(
	range(c3.shape[0]),
	c3.values,
	s = 70,
)
ax[1].scatter(
	*c3_structure.T,
	c = c3_structure[:,-1],
	alpha = .6, cmap = 'binary', vmin = 0, vmax = 1, marker = 'o', s = 200, edgecolor = 'black', linewidth = 2,
)
ax[1].axvline(c3_structure[0,0], alpha = .6, linewidth = 2, color = 'red', linestyle='--', zorder = 0)






ax[2].plot(
	range(c4.shape[0]),
	c4.values,
	linewidth = 2, color = 'black', zorder = 0
)
ax[2].scatter(
	range(c4.shape[0]),
	c4.values,
	s = 70
)
ax[2].scatter(
	*c4_structure.T,
	c = c4_structure[:,-1],
	alpha = .6, cmap = 'binary', vmin = 0, vmax = 1, marker = 'o', s = 200, edgecolor = 'black', linewidth = 2,
)
ax[2].axvline(c4_structure[0,0], alpha = .6, linewidth = 2, color = 'red', linestyle='--', zorder = 0)



for a in ax.flatten():
	a.set_xticks(range(0,17,2))
	a.set_ylim([-.1, 1.1])
	a.set_yticks([0,1])
	a.set_yticklabels([0,1])

ax[0].set_ylabel('Response\nProbability', fontweight = 'bold', fontsize = 13,)



ax[0].set_title('Diff-8', fontweight = 'bold', fontsize = 20,)
ax[1].set_title('Diff-1', fontweight = 'bold', fontsize = 20,)
ax[2].set_title('Diff-0', fontweight = 'bold', fontsize = 20,)

ax[0].set_xlabel('|length 1 - length 2|\n\nN = ' + str(int(c2n)), fontweight = 'bold', fontsize = 10,)
ax[1].set_xlabel('|length 1 - length 2|\n\nN = ' + str(int(c3n)), fontweight = 'bold', fontsize = 10,)
ax[2].set_xlabel('|length 1 - length 2|\n\nN = ' + str(int(c4n)), fontweight = 'bold', fontsize = 10,)



plt.tight_layout()
plt.savefig('plots/gens.png')