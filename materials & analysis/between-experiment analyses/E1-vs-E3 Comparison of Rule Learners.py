import numpy as np
import pandas as pd 

# import matplotlib.pyplot as plt

c1_structure = np.array([
    [8,1]
])

c2_structure = np.array([
    [1,1]
])

c3_structure = np.array([
    [0,1]
])



gensE1 = pd.read_csv('../experiment 1/analysis/data/gens.csv')
gensE3 = pd.read_csv('../experiment 3/analysis/data/test.csv')




gensE1 = gensE1[(gensE1['block'] == 0) & (gensE1['condition'] == 2)]

gensE1['s1_val'] = gensE1['s1'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)
gensE1['s2_val'] = gensE1['s2'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)

gensE1['diff'] = np.abs(gensE1['s1_val'] - gensE1['s2_val'])

gensE1['response'] = gensE1['response'].replace({'yes': 1, 'no': 0})
gensE1['response'] = gensE1['response'].replace({'respA': 1, 'respB': 0})

gensE1['response_standard'] = gensE1['response']




# count rule learners 8-diff condition e1
rulersE1 = 0

for subj in gensE1['id'].unique():
    subj_data = gensE1[gensE1['id'] == subj]
    cname = subj_data['condition'].unique()[0]
    cindex = subj_data['condition'].unique()[0]-1

    subj_av_data = subj_data.groupby('diff').mean()
    if subj_av_data[subj_av_data.index >= 9]['response_standard'].sum() >= 6:
        # print(subj, '|', subj_av_data[subj_av_data.index >= 9]['response_standard'].sum())
        rulersE1 += 1

print('Total rule learners (diff-8):', rulersE1)






gensE3 = gensE3[(gensE3['block'] == 0) & (gensE3['condition'] == 1)]

gensE3['s1_val'] = gensE3['s1'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)
gensE3['s2_val'] = gensE3['s2'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)

gensE3['diff'] = np.abs(gensE3['s1_val'] - gensE3['s2_val'])

gensE3['response'] = gensE3['response'].replace({'yes': 1, 'no': 0})
gensE3['response'] = gensE3['response'].replace({'respA': 1, 'respB': 0})

gensE3['response_standard'] = gensE3['response']




# count rule learners 8-diff condition e3
rulersE3 = 0

for subj in gensE3['id'].unique():
    subj_data = gensE3[gensE3['id'] == subj]
    cname = subj_data['condition'].unique()[0]
    cindex = subj_data['condition'].unique()[0]-1

    subj_av_data = subj_data.groupby('diff').mean()
    if subj_av_data[subj_av_data.index >= 9]['response_standard'].sum() >= 6:
        # print(subj, '|', subj_av_data[subj_av_data.index >= 9]['response_standard'].sum())
        rulersE3 += 1

print('Total rule learners (8-0):', rulersE3)




# chi square test of independence
import scipy.stats as stats

contTable = np.array([
    #  rule like | non rule like
    [rulersE1, len(gensE1['id'].unique()) - rulersE1], # e1
    [rulersE3, len(gensE3['id'].unique()) - rulersE3], # e3
])

print(contTable)

chi2, p, dof, expected = stats.chi2_contingency(contTable)

print('chi2:', chi2.round(3), '| p:', p.round(3), '| dof:', dof)

print(expected)

