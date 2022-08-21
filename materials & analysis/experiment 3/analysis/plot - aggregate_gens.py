import numpy as np
import pandas as pd 

import matplotlib.pyplot as plt

import resources

c1_structure = np.array([
	[0,0],
	[8,1],
])

c2_structure = np.array([
	[1,0],
	[8,1],
])

c3_structure = np.array([
	[7,0],
	[8,1],
])

c4_structure = np.array([
	[4,0],
	[8,1],
])



gens = pd.read_csv('data/test.csv')
# ^ 'Unnamed: 0', 'trial', 'block', 's1', 's2', 'connected', 'response', 'accuracy', 'rt', 'counter'

gens = gens[(gens['block'] == 0)]

gens['s1_val'] = gens['s1'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)
gens['s2_val'] = gens['s2'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)

gens['diff'] = np.abs(gens['s1_val'] - gens['s2_val'])

gens['response'] = gens['response'].replace({'yes': 1, 'no': 0})
gens['response'] = gens['response'].replace({'respA': 1, 'respB': 0})

gens['response_standard'] = gens['response']

c1 = gens[gens['condition'] == 1].groupby('diff').mean()['response_standard']
c2 = gens[gens['condition'] == 2].groupby('diff').mean()['response_standard']
c3 = gens[gens['condition'] == 3].groupby('diff').mean()['response_standard']
c4 = gens[gens['condition'] == 4].groupby('diff').mean()['response_standard']

c1n = gens[gens['condition'] == 1]['id'].unique().shape[0]
c2n = gens[gens['condition'] == 2]['id'].unique().shape[0]
c3n = gens[gens['condition'] == 3]['id'].unique().shape[0]
c4n = gens[gens['condition'] == 4]['id'].unique().shape[0]

print(c1n,c2n,c3n,c4n)


fig, ax = plt.subplots(1,4, figsize = [15,3])

ax[0].plot(
	range(c1.shape[0]),
	c1.values,
	linewidth = 2, color = 'black', zorder = 0,
)
ax[0].scatter(
	range(c1.shape[0]),
	c1.values
)

ax[0].scatter(
	*c1_structure[0,:].T,
	c = 'orange', marker = 's', alpha = .6, s = 200, edgecolor = 'black', linewidth = 2,
)
ax[0].scatter(
	*c1_structure[1,:].T,
	c = 'blue', marker = 'd', alpha = .6, s = 200, edgecolor = 'black', linewidth = 2,
)

ax[1].plot(
	range(c2.shape[0]),
	c2.values,
	linewidth = 2, color = 'black', zorder = 0,
)
ax[1].scatter(
	range(c2.shape[0]),
	c2.values
)
ax[1].scatter(
	*c2_structure[0,:].T,
	c = 'orange', marker = 's', alpha = .6, s = 200, edgecolor = 'black', linewidth = 2,
)
ax[1].scatter(
	*c2_structure[1,:].T,
	c = 'blue', marker = 'd', alpha = .6, s = 200, edgecolor = 'black', linewidth = 2,
)


ax[2].plot(
	range(c4.shape[0]),
	c4.values,
	linewidth = 2, color = 'black', zorder = 0,
)
ax[2].scatter(
	range(c4.shape[0]),
	c4.values
)
ax[2].scatter(
	*c4_structure[0,:].T,
	c = 'orange', marker = 's', alpha = .6, s = 200, edgecolor = 'black', linewidth = 2,
)
ax[2].scatter(
	*c4_structure[1,:].T,
	c = 'blue', marker = 'd', alpha = .6, s = 200, edgecolor = 'black', linewidth = 2,
)



ax[3].plot(
	range(c3.shape[0]),
	c3.values,
	linewidth = 2, color = 'black', zorder = 0,
)
ax[3].scatter(
	range(c3.shape[0]),
	c3.values
)
ax[3].scatter(
	*c3_structure[0,:].T,
	c = 'orange', marker = 's', alpha = .6, s = 200, edgecolor = 'black', linewidth = 2,
)
ax[3].scatter(
	*c3_structure[1,:].T,
	c = 'blue', marker = 'd', alpha = .6, s = 200, edgecolor = 'black', linewidth = 2,
)





for a in ax.flatten():
	a.set_xticks(range(0,17,2))
	a.set_ylim([-.1, 1.1])
	a.set_yticks([0,1])
	a.set_yticklabels([0,1])
	a.set_xlabel('|feature 1 - feature 2|')

ax[0].set_ylabel('Response\nProbability', fontweight = 'bold', fontsize = 13,)


ax[0].set_title('0-8', fontweight = 'bold', fontsize = 20,)
ax[1].set_title('1-8', fontweight = 'bold', fontsize = 20,)
ax[2].set_title('4-8', fontweight = 'bold', fontsize = 20,)
ax[3].set_title('7-8', fontweight = 'bold', fontsize = 20,)

ax[0].set_xlabel('|length 1 - length 2|\n\nN = ' + str(int(c1n)), fontweight = 'bold', fontsize = 10,)
ax[1].set_xlabel('|length 1 - length 2|\n\nN = ' + str(int(c2n)), fontweight = 'bold', fontsize = 10,)
ax[2].set_xlabel('|length 1 - length 2|\n\nN = ' + str(int(c4n)), fontweight = 'bold', fontsize = 10,)
ax[3].set_xlabel('|length 1 - length 2|\n\nN = ' + str(int(c3n)), fontweight = 'bold', fontsize = 10,)


# ax[0].set_title('condition 1\n(classification)')


plt.tight_layout()
plt.savefig('plots/gens.png')