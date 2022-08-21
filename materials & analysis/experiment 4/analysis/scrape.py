import os 

import numpy as np 
import pandas as pd 

def parse():
    columns = ['id', 'phase', 'condition', 'block', 'trial', 'stim_id', 'category', 'response', 'isCorrect', 'rt', '_', '__']
    all_data_e1 = pd.concat([
        pd.read_csv(os.path.join('../materials/e1/experiment/subject_data',file), names = columns)
        for file in os.listdir('../materials/e1/experiment/subject_data') if file.endswith('.csv')
    ])

    all_data_e1['stim_id'] = all_data_e1['stim_id'].map(lambda x: x.split('/')[-1].split('.')[0])
    all_data_e1.to_csv('data/all_data_e1.csv', index = None)


if __name__ == '__main__': 
    parse()