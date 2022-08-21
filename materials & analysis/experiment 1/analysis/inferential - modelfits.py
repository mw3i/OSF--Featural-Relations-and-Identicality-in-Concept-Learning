import numpy as np
import pandas as pd 

import matplotlib.pyplot as plt
import matplotlib as mpl 
# mpl.use('tkagg')


model = 'radial'
structure = 4

# models = {
# 	'radial': radial,
# }

def radial(x,m,s):
	return 1 / (np.exp((s * (x - m)) ** 2))

def square(x,m,s):
	return np.where((m - s/2 < x) & (x < m + s/2), 1, 0)

# def piecewise(x,m,s):
# 	return (s*x - m) * ((s*x - m) > 0)

def piecewise(x,m,s):
	return (-np.abs(s*x + m) + 1) * ( (-np.abs(s*x + m) + 1) > 0)
	return (s*x - m) * ((s*x - m) > 0)


gens = pd.read_csv('data/gens.csv')
# ^ 'Unnamed: 0', 'trial', 'block', 's1', 's2', 'connected', 'response', 'accuracy', 'rt', 'counter'

gens['s1_val'] = gens['s1'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)
gens['s2_val'] = gens['s2'].str.split('/').apply(lambda x: x[-1]).apply(lambda x: x.split('.')[0]).astype(int)

gens['diff'] = np.abs(gens['s1_val'] - gens['s2_val'])

gens['response'] = gens['response'].replace({'yes': 1, 'no': 0})

gens['response_standard'] = gens['response']
gens.loc[gens['condition'] == 1, 'response_standard'] = gens.loc[gens['condition'] == 1].apply(lambda x: np.abs((1 - x['response']) - (1 - x['counter'])), axis = 1)

# print(gens['condition'])

# c1 = gens[gens['condition'] == 1].groupby('diff').mean()['response_standard']
diff8 = gens[gens['condition'] == 2].groupby('diff').mean()['response_standard']
diff1 = gens[gens['condition'] == 3].groupby('diff').mean()['response_standard']
diff0 = gens[gens['condition'] == 4].groupby('diff').mean()['response_standard']





fits = {}
for function, f in zip(['radial', 'square','piecewise'], [radial, square, piecewise]):
	fits[function] = {
		'Diff 8': {'params': None, 'fits': None,},
		'Diff 1': {'params': None, 'fits': None,},
		'Diff 0': {'params': None, 'fits': None,},
		'f': f,
	}


# get the fits
granularity = 100

## Radial
g = np.array(np.meshgrid(
	np.linspace(-25,25,granularity),
	np.linspace(-10,10,granularity),
))

fits['radial']['Diff 8']['params'] = g.reshape(2,-1).T

fits['radial']['Diff 8']['fits'] = np.full([fits['radial']['Diff 8']['params'].shape[0]], None)
for p, param_set in enumerate(fits['radial']['Diff 8']['params']):
	model_prediction = radial(diff8.index.values, *param_set)
	fit = np.sum((model_prediction - diff8.values) ** 2) # <-- sum squared error
	fits['radial']['Diff 8']['fits'][p] = fit


fits['radial']['Diff 1']['params'] = g.reshape(2,-1).T

fits['radial']['Diff 1']['fits'] = np.full([fits['radial']['Diff 1']['params'].shape[0]], None)
for p, param_set in enumerate(fits['radial']['Diff 1']['params']):
	model_prediction = radial(diff1.index.values, *param_set)
	fit = np.sum((model_prediction - diff1.values) ** 2) # <-- sum squared error
	fits['radial']['Diff 1']['fits'][p] = fit


fits['radial']['Diff 0']['params'] = g.reshape(2,-1).T

fits['radial']['Diff 0']['fits'] = np.full([fits['radial']['Diff 0']['params'].shape[0]], None)
for p, param_set in enumerate(fits['radial']['Diff 0']['params']):
	model_prediction = radial(diff0.index.values, *param_set)
	fit = np.sum((model_prediction - diff0.values) ** 2) # <-- sum squared error
	fits['radial']['Diff 0']['fits'][p] = fit







## Square
g = np.array(np.meshgrid(
	np.linspace(-25,25,granularity),
	np.linspace(-10,10,granularity),
))

fits['square']['Diff 8']['params'] = g.reshape(2,-1).T

fits['square']['Diff 8']['fits'] = np.full([fits['square']['Diff 8']['params'].shape[0]], None)
for p, param_set in enumerate(fits['square']['Diff 8']['params']):
	model_prediction = square(diff8.index.values, *param_set)
	fit = np.sum((model_prediction - diff8.values) ** 2) # <-- sum squared error
	fits['square']['Diff 8']['fits'][p] = fit


fits['square']['Diff 1']['params'] = g.reshape(2,-1).T

fits['square']['Diff 1']['fits'] = np.full([fits['square']['Diff 1']['params'].shape[0]], None)
for p, param_set in enumerate(fits['square']['Diff 1']['params']):
	model_prediction = square(diff1.index.values, *param_set)
	fit = np.sum((model_prediction - diff1.values) ** 2) # <-- sum squared error
	fits['square']['Diff 1']['fits'][p] = fit


fits['square']['Diff 0']['params'] = g.reshape(2,-1).T

fits['square']['Diff 0']['fits'] = np.full([fits['square']['Diff 0']['params'].shape[0]], None)
for p, param_set in enumerate(fits['square']['Diff 0']['params']):
	model_prediction = square(diff0.index.values, *param_set)
	fit = np.sum((model_prediction - diff0.values) ** 2) # <-- sum squared error
	fits['square']['Diff 0']['fits'][p] = fit










## Piecewise
g = np.array(np.meshgrid(
	np.linspace(-25,25,granularity),
	np.linspace(-10,10,granularity),
))

fits['piecewise']['Diff 8']['params'] = g.reshape(2,-1).T

fits['piecewise']['Diff 8']['fits'] = np.full([fits['piecewise']['Diff 8']['params'].shape[0]], None)
for p, param_set in enumerate(fits['piecewise']['Diff 8']['params']):
	model_prediction = piecewise(diff8.index.values, *param_set)
	fit = np.sum((model_prediction - diff8.values) ** 2) # <-- sum sqrd err
	fits['piecewise']['Diff 8']['fits'][p] = fit


fits['piecewise']['Diff 1']['params'] = g.reshape(2,-1).T

fits['piecewise']['Diff 1']['fits'] = np.full([fits['piecewise']['Diff 1']['params'].shape[0]], None)
for p, param_set in enumerate(fits['piecewise']['Diff 1']['params']):
	model_prediction = piecewise(diff1.index.values, *param_set)
	fit = np.sum((model_prediction - diff1.values) ** 2) # <-- sum sqrd err
	fits['piecewise']['Diff 1']['fits'][p] = fit


fits['piecewise']['Diff 0']['params'] = g.reshape(2,-1).T

fits['piecewise']['Diff 0']['fits'] = np.full([fits['piecewise']['Diff 0']['params'].shape[0]], None)
for p, param_set in enumerate(fits['piecewise']['Diff 0']['params']):
	model_prediction = piecewise(diff0.index.values, *param_set)
	fit = np.sum((model_prediction - diff0.values) ** 2) # <-- sum sqrd err
	fits['piecewise']['Diff 0']['fits'][p] = fit






## PLOT



d8_structure = np.array([
	[8,1]
])

d1_structure = np.array([
	[1,1]
])

d0_structure = np.array([
	[0,1]
])



fig, ax = plt.subplots(3,3, figsize = [10,10])


for f, function in enumerate(['radial', 'square', 'piecewise']):

	print(fits[function]['Diff 8']['params'][fits[function]['Diff 8']['fits'].argmin(),:])
	print(fits[function]['Diff 1']['params'][fits[function]['Diff 1']['fits'].argmin(),:])
	print(fits[function]['Diff 0']['params'][fits[function]['Diff 0']['fits'].argmin(),:])

	xspace = np.linspace(0,16,100)
	ax[f, 0].plot(
		xspace,
		fits[function]['f'](xspace, *fits[function]['Diff 8']['params'][fits[function]['Diff 8']['fits'].argmin(),:]),
		color = 'black', linewidth = 2,
		# piecewise(diff8.index.values, 0, 1)
	)

	ax[f, 0].scatter(
		diff8.index.values,
		diff8.values,
	)

	ax[f, 0].scatter(
		*d8_structure.T,
		c = d8_structure[:,-1],
		alpha = .6, cmap = 'binary', vmin = 0, vmax = 1, marker = 'o', s = 200, edgecolor = 'black', linewidth = 2,
	)
	model_prediction = fits[function]['f'](diff8.index.values, *fits[function]['Diff 8']['params'][fits[function]['Diff 8']['fits'].argmin(),:])
	sse = np.sum((model_prediction - diff8.values) ** 2)
	ax[f, 0].set_xlabel('|feature 1 - feature 2|\nSSE = ' + str(sse.round(4)), fontsize = 12, fontweight = 'bold')
	print(sse)





	ax[f, 1].plot(
		xspace,
		fits[function]['f'](xspace, *fits[function]['Diff 1']['params'][fits[function]['Diff 1']['fits'].argmin(),:]),
		color = 'black', linewidth = 2,
	)

	ax[f, 1].scatter(
		diff1.index.values,
		diff1.values,
	)
	ax[f, 1].scatter(
		*d1_structure.T,
		c = d1_structure[:,-1],
		alpha = .6, cmap = 'binary', vmin = 0, vmax = 1, marker = 'o', s = 200, edgecolor = 'black', linewidth = 2,
	)
	model_prediction = fits[function]['f'](diff1.index.values, *fits[function]['Diff 1']['params'][fits[function]['Diff 1']['fits'].argmin(),:])
	sse = np.sum((model_prediction - diff1.values) ** 2)
	ax[f, 1].set_xlabel('|feature 1 - feature 2|\nSSE = ' + str(sse.round(4)), fontsize = 12, fontweight = 'bold')
	print(sse)



	ax[f, 2].plot(
		xspace,
		fits[function]['f'](xspace, *fits[function]['Diff 0']['params'][fits[function]['Diff 0']['fits'].argmin(),:]),
		color = 'black', linewidth = 2,
	)

	ax[f, 2].scatter(
		diff0.index.values,
		diff0.values,
	)
	ax[f, 2].scatter(
		*d0_structure.T,
		c = d0_structure[:,-1],
		alpha = .6, cmap = 'binary', vmin = 0, vmax = 1, marker = 'o', s = 200, edgecolor = 'black', linewidth = 2,
	)
	model_prediction = fits[function]['f'](diff0.index.values, *fits[function]['Diff 0']['params'][fits[function]['Diff 0']['fits'].argmin(),:])
	sse = np.sum((model_prediction - diff0.values) ** 2)
	ax[f, 2].set_xlabel('|feature 1 - feature 2|\nSSE = ' + str(sse.round(4)), fontsize = 12, fontweight = 'bold')
	print(sse)




for a in ax.flatten():
	a.set_xticks(range(0,17,2))
	a.set_ylim([-.1, 1.1])
	a.set_yticks([0,1])
	a.set_yticklabels([0,1])

ax[0,0].set_ylabel('Response Probability\nRadial Basis', fontsize = 15, fontweight = 'bold')
ax[1,0].set_ylabel('Response Probability\nSquare', fontsize = 15, fontweight = 'bold')
ax[2,0].set_ylabel('Response Probability\nPiecewise-Linear', fontsize = 15, fontweight = 'bold')



ax[0,0].set_title('Diff 8', fontsize = 15, fontweight = 'bold')
ax[0,1].set_title('Diff 1', fontsize = 15, fontweight = 'bold')
ax[0,2].set_title('Diff 0', fontsize = 15, fontweight = 'bold')

plt.tight_layout()
plt.savefig('plots/fits.png')
plt.close()











fig = plt.figure(figsize = [20,20])
decorate = lambda a: [
	a.set_xlabel('center', fontsize = 15, fontweight = 'bold'),
	a.set_ylabel('sharpness', fontsize = 15, fontweight = 'bold'),
	a.set_zlabel('sum squared error', fontsize = 15, fontweight = 'bold'),
]


# radial
ax = fig.add_subplot(331, projection = '3d')
ax.plot_surface(
	g[0], g[1], fits['radial']['Diff 8']['fits'].reshape(g.shape[1], g.shape[1])
); decorate(ax)
ax.set_title('Radial\nDiff-8', fontsize = 15, fontweight = 'bold')

ax = fig.add_subplot(332, projection = '3d')
ax.plot_surface(
	g[0], g[1], fits['radial']['Diff 1']['fits'].reshape(g.shape[1], g.shape[1])
); decorate(ax)
ax.set_title('Radial\nDiff-1', fontsize = 15, fontweight = 'bold')

ax = fig.add_subplot(333, projection = '3d')
ax.plot_surface(
	g[0], g[1], fits['radial']['Diff 0']['fits'].reshape(g.shape[1], g.shape[1])
); decorate(ax)
ax.set_title('Radial\nDiff-0', fontsize = 15, fontweight = 'bold')


# square
ax = fig.add_subplot(334, projection = '3d')
ax.plot_surface(
	g[0], g[1], fits['square']['Diff 8']['fits'].reshape(g.shape[1], g.shape[1])
); decorate(ax)
ax.set_title('Square\nDiff-8', fontsize = 15, fontweight = 'bold')

ax = fig.add_subplot(335, projection = '3d')
ax.plot_surface(
	g[0], g[1], fits['square']['Diff 1']['fits'].reshape(g.shape[1], g.shape[1])
); decorate(ax)
ax.set_title('Square\nDiff-1', fontsize = 15, fontweight = 'bold')

ax = fig.add_subplot(336, projection = '3d')
ax.plot_surface(
	g[0], g[1], fits['square']['Diff 0']['fits'].reshape(g.shape[1], g.shape[1])
); decorate(ax)
ax.set_title('Square\nDiff-0', fontsize = 15, fontweight = 'bold')

# piecewise
ax = fig.add_subplot(337, projection = '3d')
ax.plot_surface(
	g[0], g[1], fits['piecewise']['Diff 8']['fits'].reshape(g.shape[1], g.shape[1])
); decorate(ax)
ax.set_title('Piecewise-Linear\nDiff-8', fontsize = 15, fontweight = 'bold')

ax = fig.add_subplot(338, projection = '3d')
ax.plot_surface(
	g[0], g[1], fits['piecewise']['Diff 1']['fits'].reshape(g.shape[1], g.shape[1])
); decorate(ax)
ax.set_title('Piecewise-Linear\nDiff-1', fontsize = 15, fontweight = 'bold')

ax = fig.add_subplot(339, projection = '3d')
ax.plot_surface(
	g[0], g[1], fits['piecewise']['Diff 0']['fits'].reshape(g.shape[1], g.shape[1])
); decorate(ax)
ax.set_title('Piecewise-Linear\nDiff-0', fontsize = 15, fontweight = 'bold')


# plt.tight_layout()
# plt.show()
plt.savefig('plots/surface.png')











