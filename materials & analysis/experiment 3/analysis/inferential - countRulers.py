import numpy as np
import pandas as pd 

import matplotlib.pyplot as plt


gens = pd.read_csv('data/test.csv')
# ^ 'Unnamed: 0', 'trial', 'block', 's1', 's2', 'connected', 'response', 'accuracy', 'rt', 'counter'

gens = gens[(gens['block'] == 0)]

gens['s1_val'] = gens['s1'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)
gens['s2_val'] = gens['s2'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)

gens['diff'] = np.abs(gens['s1_val'] - gens['s2_val'])

gens['response'] = gens['response'].replace({'yes': 1, 'no': 0})
gens['response'] = gens['response'].replace({'respA': 1, 'respB': 0})

gens['response_standard'] = gens['response']




# count rule learners 8-0
rulers80 = 0

for subj in gens[gens['condition'] == 1]['id'].unique():
	subj_data = gens[gens['id'] == subj]
	cname = subj_data['condition'].unique()[0]
	cindex = subj_data['condition'].unique()[0]-1

	subj_av_data = subj_data.groupby('diff').mean()
	if subj_av_data[subj_av_data.index >= 9]['response_standard'].sum() >= 6:
		# print(subj, '|', subj_av_data[subj_av_data.index >= 9]['response_standard'].sum())
		rulers80 += 1

print('Total rule learners (8-0):', rulers80)





# count rule learners 8-1
rulers81 = 0

for subj in gens[gens['condition'] == 2]['id'].unique():
	subj_data = gens[gens['id'] == subj]
	cname = subj_data['condition'].unique()[0]
	cindex = subj_data['condition'].unique()[0]-1

	subj_av_data = subj_data.groupby('diff').mean()
	if subj_av_data[subj_av_data.index >= 9]['response_standard'].sum() >= 6:
		# print(subj, '|', subj_av_data[subj_av_data.index >= 9]['response_standard'].sum())
		rulers81 += 1

print('Total rule learners (8-1):', rulers81)







# count rule learners 8-7
rulers87 = 0

for subj in gens[gens['condition'] == 3]['id'].unique():
	subj_data = gens[gens['id'] == subj]
	cname = subj_data['condition'].unique()[0]
	cindex = subj_data['condition'].unique()[0]-1

	subj_av_data = subj_data.groupby('diff').mean()
	if subj_av_data[subj_av_data.index >= 9]['response_standard'].sum() >= 6:
		# print(subj, '|', subj_av_data[subj_av_data.index >= 9]['response_standard'].sum())
		rulers87 += 1

print('Total rule learners (8-7):', rulers87)






# count rule learners 8-4
rulers84 = 0

for subj in gens[gens['condition'] == 4]['id'].unique():
	subj_data = gens[gens['id'] == subj]
	cname = subj_data['condition'].unique()[0]
	cindex = subj_data['condition'].unique()[0]-1

	subj_av_data = subj_data.groupby('diff').mean()
	if subj_av_data[subj_av_data.index >= 9]['response_standard'].sum() >= 6:
		# print(subj, '|', subj_av_data[subj_av_data.index >= 9]['response_standard'].sum())
		rulers84 += 1

print('Total rule learners (8-4):', rulers84)






