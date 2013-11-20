#!/usr/bin/python

def paltolist(pal):
	aux = []
	for i in pal:
		aux.append(i)
	return aux

def ana(pallist):
	laux = []
	if (len(pallist) == 1):
		laux.append(pallist.pop())
	else:
		for i in pallist:
			laux1=[]
			laux1=pallist[:]
			laux1.remove(i)
			laux2=ana(laux1)
			for j in laux2:
				laux.append(i+j)
	return laux
