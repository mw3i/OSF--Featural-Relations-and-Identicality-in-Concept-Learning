import numpy as np
import pandas as pd 
import scipy.stats as stats
import matplotlib.pyplot as plt

c1_structure = np.array([
	[1,0],
	[8,1]
])

c2_structure = np.array([
	[8,1]
]) # diff 8

c3_structure = np.array([
	[1,1]
]) # diff 1

c4_structure = np.array([
	[0,1]
]) # diff 0


gens = pd.read_csv('data/gens.csv')
# ^ 'Unnamed: 0', 'trial', 'block', 's1', 's2', 'connected', 'response', 'accuracy', 'rt', 'counter'

gens['s1_val'] = gens['s1'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)
gens['s2_val'] = gens['s2'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)

gens['diff'] = np.abs(gens['s1_val'] - gens['s2_val'])

gens['response'] = gens['response'].replace({'yes': 1, 'no': 0})

gens['response_standard'] = gens['response']
gens.loc[gens['condition'] == 1, 'response_standard'] = gens.loc[gens['condition'] == 1].apply(lambda x: np.abs((1 - x['response']) - (1 - x['counter'])), axis = 1)

# print(gens['condition'])

c1 = gens[gens['condition'] == 1].groupby('diff').mean()['response_standard']
c2 = gens[gens['condition'] == 2].groupby('diff').mean()['response_standard']
c3 = gens[gens['condition'] == 3].groupby('diff').mean()['response_standard']
c4 = gens[gens['condition'] == 4].groupby('diff').mean()['response_standard']


print(
	'8_diff: _M_ =',
	str((gens[(gens['condition'] == 2) & (gens['diff'] == 8)].groupby('id').mean()['response_standard'].mean() * 100).round(3)) + '%, _SD_ =',
	str((gens[(gens['condition'] == 2) & (gens['diff'] == 8)].groupby('id').mean()['response_standard'].std() * 100).round(3)) + '%',
)

print(
	'1_diff: _M_ =',
	str((gens[(gens['condition'] == 3) & (gens['diff'] == 1)].groupby('id').mean()['response_standard'].mean() * 100).round(3)) + '%, _SD_ =',
	str((gens[(gens['condition'] == 3) & (gens['diff'] == 1)].groupby('id').mean()['response_standard'].std() * 100).round(3)) + '%',

)

print(
	'0_diff: _M_ =',
	str((gens[(gens['condition'] == 4) & (gens['diff'] == 0)].groupby('id').mean()['response_standard'].mean() * 100).round(3)) + '%, _SD_ =',
	str((gens[(gens['condition'] == 4) & (gens['diff'] == 0)].groupby('id').mean()['response_standard'].std() * 100).round(3)) + '%',

)

## data in long format (because i thought id need it; turns out scipy does it oldschool)
responses = pd.DataFrame({
	'decisions': np.concatenate([
		gens[(gens['condition'] == 2) & (gens['diff'] == 8)].groupby('id').mean()['response_standard'],
		gens[(gens['condition'] == 3) & (gens['diff'] == 1)].groupby('id').mean()['response_standard'],
		gens[(gens['condition'] == 4) & (gens['diff'] == 0)].groupby('id').mean()['response_standard'],
	]),
	'condition': np.concatenate([
		['cond1'] * gens[(gens['condition'] == 2) & (gens['diff'] == 8)].groupby('id').mean()['response_standard'].shape[0],
		['cond2'] * gens[(gens['condition'] == 3) & (gens['diff'] == 1)].groupby('id').mean()['response_standard'].shape[0],
		['cond3'] * gens[(gens['condition'] == 4) & (gens['diff'] == 0)].groupby('id').mean()['response_standard'].shape[0],
	]),
})

print('\n-------\n')
## Anova comparing learning accuracy
f,p = stats.f_oneway(
	gens[(gens['condition'] == 2) & (gens['diff'] == 8)].groupby('id').mean()['response_standard'],
	gens[(gens['condition'] == 3) & (gens['diff'] == 1)].groupby('id').mean()['response_standard'],
	gens[(gens['condition'] == 4) & (gens['diff'] == 0)].groupby('id').mean()['response_standard'],
)

print('_F_ = ', f.round(3), ',', '_p_ = ', p.round(3))