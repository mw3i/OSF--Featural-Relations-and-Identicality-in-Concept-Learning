import numpy as np
import pandas as pd 

import matplotlib.pyplot as plt


c2_structure = np.array([
	[8,1]
])


R6c2_structure = np.array([
	[8,1]
])

R8c2_structure = np.array([
	[8,1]
])

gens = pd.read_csv('data/gens.csv')
# ^ 'Unnamed: 0', 'trial', 'block', 's1', 's2', 'connected', 'response', 'accuracy', 'rt', 'counter'

# gens = gens[(gens['block'] == 0) & (gens['condition'] == 1)]
gens = gens[(gens['block'] == 0)]

gens['s1_val'] = gens['s1'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)
gens['s2_val'] = gens['s2'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)

gens['diff'] = np.abs(gens['s1_val'] - gens['s2_val'])

gens['response'] = gens['response'].replace({'yes': 1, 'no': 0})
gens['response'] = gens['response'].replace({'respA': 1, 'respB': 0})

gens['response_standard'] = gens['response']



rulers = 0
gens6 = []

for subj in gens[gens['condition'] == 2]['id'].unique():
	subj_data = gens[gens['id'] == subj]
	cname = subj_data['condition'].unique()[0]
	cindex = subj_data['condition'].unique()[0]-1

	subj_av_data = subj_data.groupby('diff').mean()
	if subj_av_data[subj_av_data.index >= 9]['response_standard'].sum() >= 6:
		print(subj, '|', subj_av_data[subj_av_data.index >= 9]['response_standard'].sum())
		rulers += 1
		gens6.append(subj)


rulers = 0
gens8 = []

for subj in gens[gens['condition'] == 2]['id'].unique():
	subj_data = gens[gens['id'] == subj]
	cname = subj_data['condition'].unique()[0]
	cindex = subj_data['condition'].unique()[0]-1

	subj_av_data = subj_data.groupby('diff').mean()
	if subj_av_data[subj_av_data.index >= 9]['response_standard'].sum() >= 7:
		print(subj, '|', subj_av_data[subj_av_data.index >= 9]['response_standard'].sum())
		rulers += 1
		gens8.append(subj)



print('Total rule learners:', rulers)




R6c2 = gens[(gens['condition'] == 2) & (gens['id'].isin(gens6))].groupby('diff').mean()['response_standard']
R8c2 = gens[(gens['condition'] == 2) & (gens['id'].isin(gens8))].groupby('diff').mean()['response_standard']
c2 = gens[gens['condition'] == 2].groupby('diff').mean()['response_standard']




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
	range(R6c2.shape[0]),
	R6c2.values,
	linewidth = 2, color = 'black', zorder = 0
)
ax[1].scatter(
	range(R6c2.shape[0]),
	R6c2.values,
	s = 70,
)
ax[1].scatter(
	*R6c2_structure.T,
	c = R6c2_structure[:,-1],
	alpha = .6, cmap = 'binary', vmin = 0, vmax = 1, marker = 'o', s = 200, edgecolor = 'black', linewidth = 2,
)
ax[1].axvline(R6c2_structure[0,0], alpha = .6, linewidth = 2, color = 'red', linestyle='--', zorder = 0)


ax[2].plot(
	range(R8c2.shape[0]),
	R8c2.values,
	linewidth = 2, color = 'black', zorder = 0
)
ax[2].scatter(
	range(R8c2.shape[0]),
	R8c2.values,
	s = 70,
)
ax[2].scatter(
	*R8c2_structure.T,
	c = R8c2_structure[:,-1],
	alpha = .6, cmap = 'binary', vmin = 0, vmax = 1, marker = 'o', s = 200, edgecolor = 'black', linewidth = 2,
)
ax[2].axvline(R8c2_structure[0,0], alpha = .6, linewidth = 2, color = 'red', linestyle='--', zorder = 0)






for a in ax.flatten():
	a.set_xticks(range(0,17,2))
	a.set_ylim([-.1, 1.1])
	a.set_yticks([0,1])
	a.set_yticklabels([0,1])

ax[0].set_ylabel('Response\nProbability', fontweight = 'bold', fontsize = 13,)

ax[0].set_title('All Subjects\nN = ' + str(int(gens[gens['condition'] == 2]['id'].unique().shape[0])), fontweight = 'bold', fontsize = 13,)
ax[1].set_title('at least 6/7 generalized\nN = ' + str(int(len(gens6))), fontweight = 'bold', fontsize = 13,)
ax[2].set_title('at least 7/7 generalized\nN = ' + str(int(len(gens8))), fontweight = 'bold', fontsize = 13,)




plt.tight_layout()
plt.savefig('plots/gen -vs- rule.png')