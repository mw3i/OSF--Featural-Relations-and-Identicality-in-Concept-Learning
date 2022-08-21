import os, json

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

## import pilot
gens = []

src = '../experiment/data/'
for filename in os.listdir(src):

    if filename.endswith('.json'):
        with open(os.path.join(src, filename), 'r') as filedata:
            res = json.load(filedata)
            subj = pd.DataFrame(res['results']['results']['generalizationPhase'][1:], columns = res['results']['results']['generalizationPhase'][0])

            subj['id'] = res['id']
            subj['condition'] = res['condition']
            
            gens.append(subj)






gens = pd.concat(gens, ignore_index = True)
print(gens)



gens.to_csv('data/gens.csv')


