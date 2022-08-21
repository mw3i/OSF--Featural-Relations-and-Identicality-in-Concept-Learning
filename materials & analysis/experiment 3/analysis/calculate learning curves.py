import os, json

import numpy as np
import pandas as pd 
import scipy.stats as stats
import matplotlib.pyplot as plt

import resources

data = {
    'subj': {},
    'trainAcc':[],
    'allTrain': [],
}

blocksize = 4
trialsizes = [16 * blocksize, 22 * blocksize, 16 * blocksize, 20 * blocksize]
stimsetsizes = [16, 22, 16, 20]

src = '../experiment/data/'

for f, file in enumerate(os.listdir(src)):
    if file.endswith('.json'):
        with open(os.path.join(src,file), 'r') as filedata:
            s = json.load(filedata)
            data['subj'][f] = {
                'id': f,
                'cond': int(s['condition']),
                'res': {
                    'train': pd.DataFrame(s['results']['results']['trainingPhase'][1:], columns = s['results']['results']['trainingPhase'][0]),
                }
            }

            data['subj'][f]['res']['train']['id'] = f
            data['allTrain'].append(data['subj'][f]['res']['train'])



            trial_acc = data['subj'][f]['res']['train']['accuracy'].to_list()
            # print(len(trial_acc))
            trialsize = trialsizes[int(s['condition'])-1]
            if len(trial_acc[:trialsize]) < trialsize:
                whatsleft = trialsize - len(trial_acc)
                trial_acc += [1] * whatsleft

            block_acc = []
            for i in range(0,trialsize,stimsetsizes[int(s['condition'])-1]):
                block_acc.append(
                    np.mean(trial_acc[i:i + stimsetsizes[int(s['condition'])-1]])
                )
            
            data['trainAcc'].append(
                [f, s['condition']] + block_acc
            )
            # print(s['id'], '\t', s['condition'], '\t', data['subj'][f]['res']['train'].shape[0], trialsizes[int(s['condition'])-1], '\t', data['subj'][f]['res']['train'].shape[0] < trialsizes[int(s['condition'])-1])


data['trainAcc'] = pd.DataFrame(
    data['trainAcc'],
    columns = ['id', 'condition'] + ['block' + str(b) for b in range(blocksize)]
)
# data['trainAcc'].to_csv('testtrainacc.csv')

c1_n = data['trainAcc'][data['trainAcc']['condition'] == '1']['id'].unique().shape[0]
c2_n = data['trainAcc'][data['trainAcc']['condition'] == '2']['id'].unique().shape[0]
c4_n = data['trainAcc'][data['trainAcc']['condition'] == '4']['id'].unique().shape[0]
c3_n = data['trainAcc'][data['trainAcc']['condition'] == '3']['id'].unique().shape[0]

print(c1_n, c2_n, c3_n, c4_n)



plt.plot(
    data['trainAcc'][data['trainAcc']['condition'] == '1'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True),
    c = plt.get_cmap("tab10")(0), zorder = 0, linewidth = 3,
)
plt.plot(
    data['trainAcc'][data['trainAcc']['condition'] == '2'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True),
    c = plt.get_cmap("tab10")(1), zorder = 0, linewidth = 3,
)
plt.plot(
    data['trainAcc'][data['trainAcc']['condition'] == '4'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True),
    c = plt.get_cmap("tab10")(2), zorder = 0, linewidth = 3,
)
plt.plot(
    data['trainAcc'][data['trainAcc']['condition'] == '3'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True),
    c = plt.get_cmap("tab10")(3), zorder = 0, linewidth = 3,
)

plt.scatter(
    range(blocksize),
    data['trainAcc'][data['trainAcc']['condition'] == '1'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True),
    label = '0-8 | N = ' + str(c1_n), marker = 'o', s = 200, color = plt.get_cmap("tab10")(0), edgecolor = 'black',
)
plt.scatter(
    range(blocksize),
    data['trainAcc'][data['trainAcc']['condition'] == '2'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True),
    label = '1-8 | N = ' + str(c2_n), marker = '*', s = 200, color = plt.get_cmap("tab10")(1), edgecolor = 'black',
)
plt.scatter(
    range(blocksize),
    data['trainAcc'][data['trainAcc']['condition'] == '4'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True),
    label = '4-8 | N = ' + str(c4_n), marker = 'P', s = 200, color = plt.get_cmap("tab10")(2), edgecolor = 'black',
)
plt.scatter(
    range(blocksize),
    data['trainAcc'][data['trainAcc']['condition'] == '3'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True),
    label = '7-8 | N = ' + str(c3_n), marker = '^', s = 200, color = plt.get_cmap("tab10")(3), edgecolor = 'black',
)


## error bars
plt.fill_between(
    range(blocksize),
    data['trainAcc'][data['trainAcc']['condition'] == '1'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True) + data['trainAcc'][data['trainAcc']['condition'] == '1'][['block' + str(b) for b in range(blocksize)]].sem(skipna = True),
    data['trainAcc'][data['trainAcc']['condition'] == '1'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True) - data['trainAcc'][data['trainAcc']['condition'] == '1'][['block' + str(b) for b in range(blocksize)]].sem(skipna = True),
    color = plt.get_cmap("tab10")(0), alpha = .25, edgecolor = 'black', zorder = 0
)
plt.fill_between(
    range(blocksize),
    data['trainAcc'][data['trainAcc']['condition'] == '2'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True) + data['trainAcc'][data['trainAcc']['condition'] == '2'][['block' + str(b) for b in range(blocksize)]].sem(skipna = True),
    data['trainAcc'][data['trainAcc']['condition'] == '2'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True) - data['trainAcc'][data['trainAcc']['condition'] == '2'][['block' + str(b) for b in range(blocksize)]].sem(skipna = True),
    color = plt.get_cmap("tab10")(1), alpha = .25, edgecolor = 'black', zorder = 0
)
plt.fill_between(
    range(blocksize),
    data['trainAcc'][data['trainAcc']['condition'] == '4'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True) + data['trainAcc'][data['trainAcc']['condition'] == '3'][['block' + str(b) for b in range(blocksize)]].sem(skipna = True),
    data['trainAcc'][data['trainAcc']['condition'] == '4'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True) - data['trainAcc'][data['trainAcc']['condition'] == '3'][['block' + str(b) for b in range(blocksize)]].sem(skipna = True),
    color = plt.get_cmap("tab10")(2), alpha = .25, edgecolor = 'black', zorder = 0
)
plt.fill_between(
    range(blocksize),
    data['trainAcc'][data['trainAcc']['condition'] == '3'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True) + data['trainAcc'][data['trainAcc']['condition'] == '3'][['block' + str(b) for b in range(blocksize)]].sem(skipna = True),
    data['trainAcc'][data['trainAcc']['condition'] == '3'][['block' + str(b) for b in range(blocksize)]].mean(skipna = True) - data['trainAcc'][data['trainAcc']['condition'] == '3'][['block' + str(b) for b in range(blocksize)]].sem(skipna = True),
    color = plt.get_cmap("tab10")(3), alpha = .25, edgecolor = 'black', zorder = 0
)



plt.xlabel('Block', fontsize = 19, fontweight = 'bold')
plt.ylabel('Accuracy', fontsize = 19, fontweight = 'bold')
plt.title('Learning Accuracy over Time', fontsize = 22, fontweight = 'bold')

plt.xticks(range(0,blocksize), range(1,blocksize+1))
plt.ylim([0,1.1])
plt.legend()

plt.tight_layout()




plt.savefig('plots/e1cLearningCurves.png')

