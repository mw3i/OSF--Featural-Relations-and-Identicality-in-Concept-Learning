import numpy as np 

stim = list(range(1,16+1))


print(stim)

pairlists = {
	x: [] for x in range(16)
	# abs(diff): [list of pairs with that abs(diff)]
}

for i in range(1,16+1):
	for ii in range(1,16+1):
		pairlists[abs(i - ii)].append([i-1,ii-1])

for p in pairlists:
	print(p, '|', len(pairlists[p]))


print(pairlists)





