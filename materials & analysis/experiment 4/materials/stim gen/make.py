 ## Python Standard Library
import sys
import os
import csv
import pickle

## External Dependencies
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 


##__Make Categories
inputs = np.array([
    [.1,.1],
    [.2,.2],
    [.3,.3],
    [.4,.4],
    [.5,.5],
    [.6,.6],
    [.7,.7],
    [.8,.8],

    [.1, .7],
    [.2, .8],
    [.0, .8],
    [.1, .9],

    [.7, .1],
    [.8, .2],
    [.8, .0],
    [.9, .1],
])

labels = [
    'a','a','a','a','a','a','a','a', 
    'b','b','b','b','b','b','b','b',
]

gens = np.array([
    [.0, .0],
    [.9, .9],
    
    [.2, .4],
    [.3, .5],
    [.4, .6],
    [.5, .7],

    [.4, .2],
    [.5, .3],
    [.6, .4],
    [.7, .5],

    [.0, .2],
    [.2, .0],

    [.9, .7],
    [.7, .9],
])


## Plot structures as points
fig, ax = plt.subplots(1,1, figsize=(4,4))
ax.scatter(
    *inputs.T,
    color = ['orange' if l == 'a' else 'blue' for l in labels ],

)

# gens
ax.scatter(*gens.T, color = 'black')
ax.set_xlim([-.1,1.1]); ax.set_ylim([-.1,1.1])

ax.set_title('training data & gens')
plt.savefig('structures1.png')
plt.close()


## Save to File
d = pd.DataFrame({
    'ID': ['i-'+str(i) for i in range(inputs.shape[0])] + ['g-' + str(g) for g in range(gens.shape[0])],
    'Category': labels + ['gen'] * gens.shape[0],
    'Dim1': np.concatenate([inputs[:,0], gens[:,0]]),
    'Dim2': np.concatenate([inputs[:,1], gens[:,1]]),
})
# print(d)
d.to_csv('data1.csv', index = None)






##__V2
transform = np.array([
    [-1,0],
    [0,1]
])
inputs = inputs @ transform
inputs[:,0] += 1
gens = gens @ transform
gens[:,0] += 1


## Plot structures as points
fig, ax = plt.subplots(1,1, figsize=(4,4))

ax.scatter(
    *inputs.T,
    color = ['orange' if l == 'a' else 'blue' for l in labels ],

)

# gens
ax.scatter(*gens.T, color = 'black')
ax.set_xlim([-.1,1.1]); ax.set_ylim([-.1,1.1])

ax.set_title('training data & gens')
plt.savefig('structures2.png')
plt.close()


## Save to File
d = pd.DataFrame({
    'ID': ['i-'+str(i) for i in range(inputs.shape[0])] + ['g-' + str(g) for g in range(gens.shape[0])],
    'Category': labels + ['gen'] * gens.shape[0],
    'Dim1': np.concatenate([inputs[:,0], gens[:,0]]),
    'Dim2': np.concatenate([inputs[:,1], gens[:,1]]),
})
# print(d)
d.to_csv('data2.csv', index = None)