import numpy as np
import pandas as pd 
import scipy.stats as stats
import matplotlib.pyplot as plt

import resources

gens = pd.read_csv('data/test.csv')
# ^ 'Unnamed: 0', 'trial', 'block', 's1', 's2', 'connected', 'response', 'accuracy', 'rt', 'counter'

gens = gens[(gens['block'] == 0)]

gens['s1_val'] = gens['s1'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)
gens['s2_val'] = gens['s2'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)

gens['diff'] = np.abs(gens['s1_val'] - gens['s2_val'])

gens['response'] = gens['response'].replace({'yes': 1, 'no': 0})
gens['response'] = gens['response'].replace({'respA': 1, 'respB': 0})

gens['response_standard'] = gens['response']
# print(gens['condition'])






c1acc = np.array([
	*gens[(gens['condition'] == 1) & (gens['diff'] == 8)].groupby('id').mean()['response_standard'].values,
	*( (gens[(gens['condition'] == 1) & (gens['diff'] == 0)].groupby('id').mean()['response_standard'].values - 1) * -1),
])
print(c1acc.mean().round(3), c1acc.std().round(3))

c2acc = np.array([
	*gens[(gens['condition'] == 2) & (gens['diff'] == 8)].groupby('id').mean()['response_standard'].values,
	*( (gens[(gens['condition'] == 2) & (gens['diff'] == 1)].groupby('id').mean()['response_standard'].values - 1) * -1),
])
print(c2acc.mean().round(3), c2acc.std().round(3))

c3acc = np.array([
	*gens[(gens['condition'] == 3) & (gens['diff'] == 8)].groupby('id').mean()['response_standard'].values,
	*( (gens[(gens['condition'] == 3) & (gens['diff'] == 7)].groupby('id').mean()['response_standard'].values - 1) * -1),
])
print(c3acc.mean().round(3), c3acc.std().round(3))


c4acc = np.array([
	*gens[(gens['condition'] == 4) & (gens['diff'] == 8)].groupby('id').mean()['response_standard'].values,
	*( (gens[(gens['condition'] == 4) & (gens['diff'] == 4)].groupby('id').mean()['response_standard'].values - 1) * -1),
])
print(c4acc.mean().round(3), c4acc.std().round(3))




## Anova comparing learning accuracy
f,p = stats.f_oneway(
	c1acc,
	c2acc,
	c4acc,
)
print('f:', f, '|', 'p:', p)

# # post hoc ttests
# t,p = stats.ttest_ind(
# 	gens[(gens['condition'] == 1) & (gens['diff'] == 8)].groupby('id').mean()['response_standard'],
# 	gens[(gens['condition'] == 2) & (gens['diff'] == 8)].groupby('id').mean()['response_standard'],
# )
# print('8v1 t:', t, '|', 'p:', p)

# t,p = stats.ttest_ind(
# 	gens[(gens['condition'] == 1) & (gens['diff'] == 8)].groupby('id').mean()['response_standard'],
# 	gens[(gens['condition'] == 3) & (gens['diff'] == 8)].groupby('id').mean()['response_standard'],
# )
# print('8v0t:', t, '|', 'p:', p)




