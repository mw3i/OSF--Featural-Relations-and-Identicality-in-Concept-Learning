## Python Standard Library
import sys
import os
import random
import csv

## External Dependencies
from psychopy import core, gui, visual, event

## Internal Dependencies
sys.path.append(os.path.abspath(os.path.join(__file__, '..')))
import event_utils



##__Forced Choice Phase
def run(
	stimuli,
	labels = None,
	randomize_presentation = True,

	supervised = True, # this determines whether participants recieve feedback
	num_blocks = 1,

	experiment_id = 'experiment',
	phase_id = 'forced_choice',
	subject_info = None,
	save_data = False,

	window = None,

	stim_position = [0,30],

	fixation_symbol = '',

	click_instructions_txt = 'Click a button to select the correct category.',
	click_instructions_txt_color = [-1,-1,-1], 
	click_instructions_position = [0, -180],

	feedback_txt_position = [0, -180],
	feedback_txt_color = [-1,-1,-1],
	
	continue_txt_position = [0, -230],
	continue_txt_color = [-1,-1,-1],

	response_btn_labels = None,
	response_btn_ypos = -310,
	response_btn_padding = 150,
	response_btn_box_size = [160, 80],
	response_btn_box_color = [.5, .8, .5],
	response_btn_txt_size = 22,
	response_btn_txt_font = 'Consolas',
	response_btn_txt_color = [-1,-1,-1],

	quit_keys = ['escape'],
	debug_mode = False,

	ask_typicality = False,
	typicality_message = 'How much does this object represent the category it belongs to?',
	typicality_labels = ['not at all typical', 'highly typical'],
	singleClick = False,

	early_finish = True,
	early_finish_lookback = 10,
	minimum_trials = 15,
	required_score = 10,
):

	# Initialize Main Psychopy win if one isn't included
	if window == None:
		window = event_utils.build_window()

	cursor = event.Mouse() # set initial cursor
	timer = core.Clock()

	if subject_info == None:
		subject_info = {
			'id': '0000',
			'condition': 0,
			'datafile_path': './subject_data.csv'
		}

	if (labels == None) & (supervised == True):
		print(phase_id + ' is set to "supeprvised", but no labels were provided. quitting experiment.')
		sys.exit()

	if response_btn_labels == None:
		if labels != None:
			response_btn_labels = list(set(labels))
		else:
			response_btn_labels = ['no', 'labels', 'provided']


	## Prepare Stimuli and Text Objects
	object_bin = {} 
	
	object_bin['stim'] = visual.ImageStim(
		window,
		pos = stim_position,
		name = 'image_stim',
		interpolate = True,
	)
	
	object_bin['response_btns'] = event_utils.make_button_row(
		window,    # psychopy win object (required argument)
		labels = response_btn_labels, 
		ypos = response_btn_ypos, 
		padding = 100,  # this determines how far apart butons will be evenly placed
		btn_box_size = response_btn_box_size, 
		btn_box_color = response_btn_box_color, 
		btn_txt_size = response_btn_txt_size,
		btn_txt_color = response_btn_txt_color,
		btn_txt_font = response_btn_txt_font,
	)
	
	object_bin['click_msg'] = visual.TextStim(
		window,
		text = click_instructions_txt,
		pos = click_instructions_position,
		color = click_instructions_txt_color
	)

	object_bin['feedback_msg'] = visual.TextStim(
		window,
		pos = feedback_txt_position,
		color = feedback_txt_color,
	)

	object_bin['click_anywhere_msg'] = visual.TextStim(
		window,
		text = 'Click anywhere to continue...',
		pos = continue_txt_position, 
		color = continue_txt_color,
	)

	object_bin['typicality_scale'] = visual.RatingScale(
		window,
		labels = typicality_labels,
		low = 0,
		high = 10,
		precision = 100,
		marker = 'circle',
		markerColor = [0,0,0],
		pos = [0,-150],
		size = 1,
		stretch = 1.2,
		textFont = 'arial',
		# textSize = ,
		showValue = False,
		acceptSize = 2,
		textColor = [-1,-1,-1],
		lineColor = [-1,-1,-1],
		mouseOnly = True,
		scale = None,
		singleClick = singleClick,
	)
	object_bin['typicality_message'] = visual.TextStim(
		window,
		text = typicality_message,
		pos = [0,-80],
		color = [-1,-1,-1],
	)

	##__ Start Phase
	trial_num = 0
	accuracy = []
	presentation_order = list(range(len(stimuli)))

	for block in range(num_blocks):
		if randomize_presentation == True:
			random.shuffle(presentation_order)

		for i in presentation_order:
			
			# set stimulus image
			object_bin['stim'].setImage(stimuli[i])

			# initially draw stimulus and response buttons
			event_utils.draw_objects_in_bin(
				window,
				object_bin, 
				object_list = ['stim', 'response_btns'],
			)           

			# wait some time
			if debug_mode == False: core.wait(.77)

			# draw click message
			event_utils.draw_objects_in_bin(
				window,
				object_bin, 
				object_list = ['stim', 'response_btns', 'click_msg'],
			)

			# wait some time
			if debug_mode == False: core.wait(.35)

			# wait for user to click a response button
			response, rt = event_utils.wait_for_btn_response(cursor, timer, object_bin['response_btns'], quit_keys=quit_keys)

			# check accuracy of subject's response
			correct_category = labels[i]
			if (supervised == True) & (correct_category != 'gen'):
				hit = response == correct_category
			else:
				hit = 'gen'
			accuracy.append(hit)

			if supervised == True:
				if response == correct_category:
					object_bin['feedback_msg'].setText('Correct! This is a ' + correct_category + ' flower')
				else:
					object_bin['feedback_msg'].setText('Incorrect... This is a ' + correct_category + ' flower')

				# draw feedback message
				event_utils.draw_objects_in_bin(
					window,
					object_bin, 
					object_list = ['stim', 'response_btns', 'feedback_msg'],
				)
			else:
				event_utils.draw_objects_in_bin(
					window,
					object_bin, 
					object_list = ['stim', 'response_btns'],
				)


			if debug_mode == False: core.wait(1)
			
			# draw continue message
			if supervised == True:
				event_utils.draw_objects_in_bin(
					window,
					object_bin, 
					object_list = ['stim', 'response_btns', 'feedback_msg', 'click_anywhere_msg'],
				)

			else:
				event_utils.draw_objects_in_bin(
					window,
					object_bin, 
					object_list = ['stim', 'response_btns', 'click_anywhere_msg'],
				)

			if debug_mode == False: core.wait(.35)

			if ask_typicality == True:
				event_utils.wait_for_click_response(cursor, timer, quit_keys=quit_keys)
				if debug_mode == False: core.wait(.35)

				# wait for user to click the rating response button
				cursor.clickReset()
				event.clearEvents()
				timer.reset()
				while object_bin['typicality_scale'].noResponse:
					if event.getKeys(keyList=quit_keys):
						print('user terminated')
						core.quit()
					event_utils.draw_objects_in_bin(window, object_bin,
						object_list = ['stim', 'typicality_scale', 'typicality_message']	
					)
				typicality_response = object_bin['typicality_scale'].getRating()
				typicality_rt = object_bin['typicality_scale'].getRT()
				object_bin['typicality_scale'].reset()
				window.flip()
				if debug_mode == False: core.wait(.55)


			else:
				event_utils.wait_for_click_response(cursor, timer, quit_keys=quit_keys)

				event_utils.draw_objects_in_bin(
					window,
					object_bin,
					object_list = ['response_btns'],
				)
				typicality_response = 'na'
				typicality_rt = 'na'

			if save_data == True:
				subject_data = [
					subject_info['id'],
					phase_id,
					subject_info['condition'],
					block,
					trial_num,
					stimuli[i],
					correct_category,
					response,
					hit,
					rt,
					typicality_response,
					typicality_rt,
				]
				with open(subject_info['datafile_path'], 'a') as file:
					csv_object = csv.writer(file)
					csv_object.writerow(subject_data)



			if early_finish == True:
				if trial_num > minimum_trials:
					if sum(accuracy[-early_finish_lookback:]) >= required_score:
						return

			trial_num = trial_num + 1









