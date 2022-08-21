import numpy as np
import pandas as pd 

import matplotlib.pyplot as plt

import resources

c1_structure = np.array([
	[8,1]
])

c2_structure = np.array([
	[1,1]
])

c3_structure = np.array([
	[0,1]
])


gens = pd.read_csv('data/gens.csv')
# ^ 'Unnamed: 0', 'trial', 'block', 's1', 's2', 'connected', 'response', 'accuracy', 'rt', 'counter'

gens = gens[(gens['block'] == 0) & (gens['condition'] == 1)]

gens['s1_val'] = gens['s1'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)
gens['s2_val'] = gens['s2'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)

gens['diff'] = np.abs(gens['s1_val'] - gens['s2_val'])

gens['response'] = gens['response'].replace({'yes': 1, 'no': 0})
gens['response'] = gens['response'].replace({'respA': 1, 'respB': 0})

gens['response_standard'] = gens['response']



rulers = 0

for subj in gens['id'].unique():
	subj_data = gens[gens['id'] == subj]
	cname = subj_data['condition'].unique()[0]
	cindex = subj_data['condition'].unique()[0]-1

	subj_av_data = subj_data.groupby('diff').mean()
	if subj_av_data[subj_av_data.index >= 8]['response_standard'].sum() >= 6:
		print(subj, '|', subj_av_data[subj_av_data.index >= 8]['response_standard'].sum())
		rulers += 1



print('Total rule learners:', rulers)

