import numpy as np
import pandas as pd 

import shapes

# data1 = pd.read_csv('data1.csv')
# for stim in data1.index:
#     stim_id = data1.loc[stim, 'ID']
#     category = data1.loc[stim, 'Category']
#     d1 = data1.loc[stim, 'Dim1']
#     d2 = data1.loc[stim, 'Dim2']

#     shapes.generate_flower(d1, d2, 'stim0/' + stim_id + '.png')


# data2 = pd.read_csv('data2.csv')
# for stim in data2.index:
#     stim_id = data2.loc[stim, 'ID']
#     category = data2.loc[stim, 'Category']
#     d1 = data2.loc[stim, 'Dim1']
#     d2 = data2.loc[stim, 'Dim2']

#     shapes.generate_flower(d1, d2, 'stim1/' + stim_id + '.png')




data1 = pd.read_csv('data1.csv')
for stim in data1.index:
    stim_id = data1.loc[stim, 'ID']
    category = data1.loc[stim, 'Category']
    d1 = data1.loc[stim, 'Dim1']
    d2 = data1.loc[stim, 'Dim2']

    shapes.generate_flower(d1, d2, 'stim2/' + stim_id + '.png', compress_edge = False)


data2 = pd.read_csv('data2.csv')
for stim in data2.index:
    stim_id = data2.loc[stim, 'ID']
    category = data2.loc[stim, 'Category']
    d1 = data2.loc[stim, 'Dim1']
    d2 = data2.loc[stim, 'Dim2']

    shapes.generate_flower(d1, d2, 'stim3/' + stim_id + '.png', compress_edge = False)


