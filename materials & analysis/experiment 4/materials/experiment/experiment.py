'''
Experiment
'''

## Python Standard Library
import sys
import os
import datetime
import time

## external dependencies
from psychopy import visual

## Internal Dependencies
import config
import pyxpr.utils
from pyxpr.events import initializer, instructions, classification, endorsement, comparison




##--------------------------------------------------
## SETUP
config.settings['experiment_time'] = '-'.join([str(d) for d in datetime.datetime.now().timetuple()][:6])

# Show initial dialogue window if True
if config.settings['show_initial_dialogue'] == True:
	initial_info = initializer.run(
		conditions = [2,3]
	)
else:
	initial_info = ['debug', 1]

# Define Subject Dictionary (this is where we'll store all the information about the subject)
subject = {
	'id': str(initial_info[0]),
	'condition': int(initial_info[1]),
	'datafile_path': os.path.join(config.settings['data_folder'], str(initial_info[0]) + '_' + config.settings['experiment_time'] + '.csv')
}

if config.settings['save_data'] == True:
	with open(subject['datafile_path'], 'w'):
		pass

if subject['id'] == 'debug':
	config.settings['debug_mode'] = True
else:
	config.settings['debug_mode'] = False

## build experiment window (little bit faster to pass the window as an argument to each event rather than making a new one on the fly each time an event changes)
if config.settings.get('window_size', 'full') == 'full':
	win = visual.Window(fullscr = True, units = 'pix', color = config.settings.get('window_color', [1,1,1]))
else:
	win = visual.Window(config.settings['window_size'], units = 'pix', color = config.settings.get('window_color', [1,1,1]))


cat_labels = ['Setosa', 'Versicolor']





##--------------------------------------------------
## RUN EXPERIMENT
##--------------------------------------------------

#__Training Phase
instructions.run(
	window = win,
	debug_mode = config.settings['debug_mode'],
	text_file = './materials/instructions/classification_train.txt',
	continue_option = 'click',
)

classification.run(
	config.stimuli[subject['condition']],
	labels = config.training_labels,
	supervised = True,
	num_blocks = config.training_blocks,

	experiment_id = config.settings['experiment_id'],
	phase_id = 'classification_train',
	subject_info = subject,
	save_data = True,
	debug_mode = config.settings['debug_mode'],
	window = win,
	stim_position = config.display['stim_position'],
	response_btn_labels = cat_labels,

	# early_finish = True,
)





#__Test Phase
instructions.run(
	window = win,
	debug_mode = config.settings['debug_mode'],
	text_file = './materials/instructions/classification_test.txt',
	continue_option = 'click',
)

classification.run( # gen
	config.gen_stimuli[subject['condition']] + config.stimuli[subject['condition']],
	labels = config.gen_labels + config.training_labels,
	supervised = False,
	num_blocks = 1,

	experiment_id = config.settings['experiment_id'],
	phase_id = 'classification_test_gen',
	subject_info = subject,
	save_data = True,
	debug_mode = config.settings['debug_mode'],
	window = win,
	stim_position = config.display['stim_position'],
	response_btn_labels = cat_labels,
	ask_typicality = False,
	singleClick = True,
	early_finish = False,
)

# classification.run(
# 	config.stimuli[subject['condition']],
# 	labels = config.training_labels,
# 	supervised = False,
# 	num_blocks = 1,

# 	experiment_id = config.settings['experiment_id'],
# 	phase_id = 'classification_test',
# 	subject_info = subject,
# 	save_data = True,
# 	debug_mode = config.settings['debug_mode'],
# 	window = win,
# 	stim_position = config.display['stim_position'],
# 	response_btn_labels = cat_labels,
# 	ask_typicality = False,
# 	singleClick = True,
# 	early_finish = False,
# )






#__Exit Experiment
instructions.run(
	window = win,
	debug_mode = config.settings['debug_mode'],
	text_file = './materials/instructions/exit_instructions.txt',
	continue_option = 'click',
)


