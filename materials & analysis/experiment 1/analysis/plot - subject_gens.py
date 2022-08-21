import numpy as np
import pandas as pd 

import matplotlib.pyplot as plt

c1_structure = np.array([
	[1,0],
	[8,1]
])

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

# c1 = gens[gens['condition'] == 1].groupby('diff').mean()['response_standard']
# c2 = gens[gens['condition'] == 2].groupby('diff').mean()['response_standard']
# c3 = gens[gens['condition'] == 3].groupby('diff').mean()['response_standard']

counts = {}
cdata = gens.groupby('id').mean()['condition']
for c in cdata.unique():
	counts[c] = cdata[cdata == c].shape[0]

fig, ax = plt.subplots(
	max(counts.values()),4,
	figsize = [8,144]
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

ax[0,0].set_title('condition 1\n(classification)')
ax[0,1].set_title('condition 2\n(observation |f1-f2|=8)')
ax[0,2].set_title('condition 3\n(observation |f1-f2|=1)')
ax[0,3].set_title('condition 4\n(observation |f1-f2|=0)')

for a in ax.flatten():
	a.set_xticks(range(0,17,2))
	a.set_ylim([-.1, 1.1])
	a.set_yticks([0,1])
	a.set_yticklabels([0,1])

ax[-1,0].set_xlabel('|feature 1 - feature 2|')
ax[-1,1].set_xlabel('|feature 1 - feature 2|')
ax[-1,2].set_xlabel('|feature 1 - feature 2|')
ax[-1,3].set_xlabel('|feature 1 - feature 2|')


plt.tight_layout()
plt.savefig('plots/gensubs.png')