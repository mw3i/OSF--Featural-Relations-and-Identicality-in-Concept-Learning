import numpy as np
import matplotlib.pyplot as plt 



structures = {
	'Diff 8': [8,1],
	'Diff 1': [1,1],
	'Diff 0': [0,1],
}



fig, ax = plt.subplots(
	2,3,
	figsize = [11,6],
)


for _, s in enumerate(structures):

	# plot category
	ax[0,_].axvline(
		structures[s][0], color = 'red', linewidth = 3, linestyle = '--', alpha = .8
	)
	ax[0,_].scatter(
		*structures[s],
		s = 150, color = 'grey', linewidth = 2, edgecolor = 'black',
		zorder = 100,
	)

	for i in range(1,16+1):
		for ii in range(1,16+1):
			if (i + ii) < 17:
				if np.abs(i - ii) == structures[s][0]:
					ax[1,_].scatter(
						i, ii,
						s = 100, color = 'grey', linewidth = 2, edgecolor = 'black',
					)

			if (i + ii) >= 17:
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

ax[0,0].set_title('Diff-8', fontweight = 'bold', fontsize = 20,)
ax[0,1].set_title('Diff-1', fontweight = 'bold', fontsize = 20,)
ax[0,2].set_title('Diff-0', fontweight = 'bold', fontsize = 20,)


ax[0,0].set_ylabel('Relational\nRepresentation', fontsize = 18, fontweight = 'bold')
ax[1,0].set_ylabel('Featural\nRepresentation', fontsize = 18, fontweight = 'bold')


plt.tight_layout()
plt.savefig('structures.png')