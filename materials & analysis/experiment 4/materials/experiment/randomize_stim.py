import os
import numpy as np 
import pandas as pd 


subject_data_folder = 'subject_data/'



# for _, file in enumerate(os.listdir(subject_data_folder)):
#     if file.endswith('.csv'): 
#         os.rename(
#             os.path.join(subject_data_folder, file),
#             os.path.join(subject_data_folder, str(_) + '.csv'),
#         )




import pandas as pd 
for _, file in enumerate(os.listdir(subject_data_folder)):
    if file.endswith('.csv'): 
        # data = pd.read_csv(os.path.join(subject_data_folder, file))
        data = np.genfromtxt(os.path.join(subject_data_folder, file), delimiter = ',', dtype = str)
        data[:,0] = 'id-' + str(file.split('.')[0])
        np.savetxt(os.path.join(subject_data_folder, 'upd', file), data, delimiter = ',', fmt = '%s')

