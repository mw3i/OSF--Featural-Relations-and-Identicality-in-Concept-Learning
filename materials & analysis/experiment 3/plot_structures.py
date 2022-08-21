import numpy as np
import matplotlib.pyplot as plt 



structures = {
	'0-8': np.array([
		[0,0],
		[8,1],
	]),
	'1-8': np.array([
		[1,0],
		[8,1],
	]),
	'4-8': np.array([
		[4,0],
		[8,1],
	]),
	'7-8': np.array([
		[7,0],
		[8,1],
	]),
}



fig, ax = plt.subplots(
	2,4,
	figsize = [12,6],
)


for _, s in enumerate(structures):

	# plot category
	ax[0,_].scatter(
		*structures[s][0],
		s = 150, color = 'orange', linewidth = 2, edgecolor = 'black', marker = 's',
		zorder = 100,
	)

	ax[0,_].scatter(
		*structures[s][1],
		s = 150, color = 'blue', linewidth = 2, edgecolor = 'black', marker = 'd',
		zorder = 100,
	)

	for i in range(1,16+1):
		for ii in range(1,16+1):
			if (i + ii) < 17:
				if np.abs(i - ii) == structures[s][0,0]:
					ax[1,_].scatter(
						i, ii,
						s = 100, color = 'orange', linewidth = 2, edgecolor = 'black', marker = 's',
					)
				elif np.abs(i - ii) == structures[s][1,0]:
					ax[1,_].scatter(
						i, ii,
						s = 100, color = 'blue', linewidth = 2, edgecolor = 'black', marker = 'd',
					)
			else:
				ax[1,_].scatter(
					i, ii,
					s = 35, color = 'black', marker = 'x', alpha = .9
				)




for a in ax[0,:]:
	a.set_xlim([-1,17])
	a.set_ylim([-.1,1.1])
	a.set_yticks([0,1])
	a.set_xticks(range(0,17,2))

	# a.set_yticklabels(['A','B'])


for a in ax[1,:]:
	a.set_xlim([-.1,17])
	a.set_ylim([-.1,17])
	a.set_yticks(range(0,17,2))
	a.set_xticks(range(0,17,2))

ax[0,0].set_title('0-8', fontweight = 'bold', fontsize = 20,)
ax[0,1].set_title('1-8', fontweight = 'bold', fontsize = 20,)
ax[0,2].set_title('4-8', fontweight = 'bold', fontsize = 20,)
ax[0,3].set_title('7-8', fontweight = 'bold', fontsize = 20,)


ax[0,0].set_ylabel('Relational\nRepresentation', fontsize = 18, fontweight = 'bold')
ax[1,0].set_ylabel('Featural\nRepresentation', fontsize = 18, fontweight = 'bold')


plt.tight_layout()
plt.savefig('structures.png')