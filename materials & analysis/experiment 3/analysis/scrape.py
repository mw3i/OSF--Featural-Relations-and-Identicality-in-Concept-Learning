import os, json

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

## import pilot
test = []

src = '../experiment/data/'
for f,filename in enumerate(os.listdir(src)):

    if filename.endswith('.json'):
        with open(os.path.join(src, filename), 'r') as filedata:
            res = json.load(filedata)
            subj = pd.DataFrame(res['results']['results']['generalizationPhase'][1:], columns = res['results']['results']['generalizationPhase'][0])
            subj['id'] = f
            subj['condition'] = res['condition']
            
            test.append(subj)

test = pd.concat(test, ignore_index = True)

test.to_csv('data/test.csv')


training = []

for filename in os.listdir(src):

    if filename.endswith('.json'):
        with open(os.path.join(src, filename), 'r') as filedata:
            res = json.load(filedata)
            subj = pd.DataFrame(res['results']['results']['trainingPhase'][1:], columns = res['results']['results']['trainingPhase'][0])

            subj['id'] = res['id']
            subj['condition'] = res['condition']
            
            training.append(subj)

training = pd.concat(training, ignore_index = True)
print(training)
training.to_csv('data/training.csv')