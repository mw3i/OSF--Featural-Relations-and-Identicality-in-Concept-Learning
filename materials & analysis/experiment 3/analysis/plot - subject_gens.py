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



counts = {}
cdata = gens.groupby('id').mean()['condition']
for c in cdata.unique():
	counts[c] = cdata[cdata == c].shape[0]

fig, ax = plt.subplots(
	max(counts.values()),4,
	figsize = [8,120]
)


counts_plots = {c: 0 for c in cdata.unique()}

for subj in gens['id'].unique():
	subj_data = gens[gens['id'] == subj]
	cname = subj_data['condition'].unique()[0]
	cindex = subj_data['condition'].unique()[0]-1

	subj_av_data = subj_data.groupby('diff').mean()

	ax[counts_plots[cname],cindex].scatter(
		subj_av_data.index,
		subj_av_data['response_standard'],
	)
	
	ax[counts_plots[cname],cindex].set_xlabel(subj)
	counts_plots[cname] += 1

for a in ax.flatten():
	a.set_xticks(range(0,17,2))
	a.set_ylim([-.1, 1.1])
	a.set_yticks([0,1])
	a.set_yticklabels([0,1])


plt.tight_layout()
plt.savefig('plots/gensubs.png')