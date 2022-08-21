'''
This code will replicate the aggregate generalization profiles in our Psychonomics 2020 poster

I apologize for how messy it is. I do a lot of the data cleaning in the same code as the plotting, which wasn't my best move

    - Matt
'''
import numpy as np 
import pandas as pd 
import scipy

catdata = pd.read_csv('../materials/stim gen/data1.csv')
catmap = {'Versicolor': 'blue', 'Setosa': 'orange'}
catmap_numeric = {'Versicolor': 0, 'Setosa': 1}

catmap_e2 = {'Alpha': 'blue', 'Beta': 'orange'}
catmap_numeric_e2 = {'Alpha': 1, 'Beta': 0}


all_data = pd.read_csv('data/all_data_e1.csv')
c1_data = all_data[all_data['condition'] == 2].copy()  # <-- condition 1 is marked by label 2 (0,1 were used for prior pilot work, so that's why their named that)
c2_data = all_data[all_data['condition'] == 3].copy() # <-- condition 2 is marked by label 3


# - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



# # # # # # # # # # # # # # # # # # # # # # # # 
#==============================================
# 
#        CONDITION 1
# 
#==============================================
# # # # # # # # # # # # # # # # # # # # # # # # 
print('identicality condition:\n\n')
subjects = c1_data['id'].unique()

c1_data['response_color'] = c1_data['response'].map(lambda x: catmap[x])
c1_data['response_numeric'] = c1_data['response'].map(lambda x: catmap_numeric[x])
c1_data['dim1'] = c1_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim1'].values[0])
c1_data['dim2'] = c1_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim2'].values[0])


gendata = c1_data[(c1_data['phase'] != 'classification_train') & (c1_data['stim_id'].isin(['g-0','g-1']) == False) & (c1_data['stim_id'].str.startswith('i') == False)]

responses = gendata['response_numeric']
frequencies = [np.sum(responses == 0), np.sum(responses == 1)]


print('0 responses:', frequencies[0] / np.sum(frequencies))
print('1 responses:', frequencies[1] / np.sum(frequencies))

print('\n-\n')


x2, p = scipy.stats.chisquare(frequencies)

print('chi square test against proportions:\n\nchisquare =', x2, '\np =', p)


# - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

print('\n\n----------\n\n')


# # # # # # # # # # # # # # # # # # # # # # # # 
#==============================================
# 
#        CONDITION 2
# 
#==============================================
# # # # # # # # # # # # # # # # # # # # # # # # 
print('non-identicality condition:\n\n')

subjects = c2_data['id'].unique()

c2_data['response_color'] = c2_data['response'].map(lambda x: catmap[x])
c2_data['response_numeric'] = c2_data['response'].map(lambda x: catmap_numeric[x])
c2_data['dim1'] = c2_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim1'].values[0])
c2_data['dim2'] = c2_data['stim_id'].map(lambda x: catdata[catdata['ID'] == x]['Dim2'].values[0])

gendata = c2_data[(c2_data['phase'] != 'classification_train') & (c2_data['stim_id'].isin(['g-0','g-1']) == False) & (c2_data['stim_id'].str.startswith('i') == False)]

responses = gendata['response_numeric']
frequencies = [np.sum(responses == 0), np.sum(responses == 1)]

print('0 responses:', frequencies[0] / np.sum(frequencies))
print('1 responses:', frequencies[1] / np.sum(frequencies))

print('\n-\n')


x2, p = scipy.stats.chisquare(frequencies)

print('chi square test against proportions\n\nchisquare =', x2, '\np =', p)
