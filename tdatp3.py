#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from types import *
import ana
import time
import itertools

class Objeto():
	def __init__(self, tam):
		assert type(tam) is FloatType
		self.tam = tam

	def __str__(self):
		return str(self.tam)

	def getTam(self):
		return self.tam

class Envase():
	def __init__(self):
		self._list=[]
		self.max=1
		self.count=0

	def __str__(self):
		s = "{"
		s += "%s" % self._list[0]
		for i in self._list[1:]:
			s+= ";%s" % i
		s += "}"
		return s

	def envasar(self, obj):
		if (self.count+obj.getTam())<=self.max:
			self._list.append(obj)
			self.count+=obj.getTam()
			return True
		else:
			return False
"""
Dada una lista de objetos, crea todas las 
permutaciones posibles
"""			
def brutus(l):
	n=len(l)
	gen=itertools.permutations(l)
	(e,c)=(None,None)
	while True:
		try:
			aux=gen.next() 
		except StopIteration:
			break
		x=aprox(aux)
		if (x[1]<c)or(c is None):
			c=x[1]
			e=x[0]
	return (e,c)

"""
El algoritmo de aproximacion recibe como parametro
una lista que contiene los objetos a envasar
O(n)
"""
def aprox(l):
	r=[]
	e=Envase()
	count=1
	for obj in l:
		if not e.envasar(obj):
			r.append(e)
			e=Envase() #Se abre otro envase
			count+=1
			e.envasar(obj)
	r.append(e)
	return (r,count)

def loadFile():
	try:
		_file = open(sys.argv[2])
	except IOError:
		print "El archivo no pudo ser abierto, verificar parametros"
		usage()
		return False
	l=[]
	n=_file.readline().replace('\n','')
	n=int(n)
	_file.readline() #Linea en blanco
	for line in _file:
		tam=line.replace('\n','').replace(',','.')
		tam=float(tam)
		obj=Objeto(tam)
		l.append(obj)
	return l

def usage():
	print "Usage:"
	print "python tdatp3.py A|E <archivo datos> \n or"
	print "./tdatp3 A|E <archivo datos>"

def checkArgs():

	if (len(sys.argv) is not 3)or(sys.argv[1] is not "A" and sys.argv[1] is not "E"):
		usage()
		return False
	return True

def runBrutus(l):
	start=time.time()
	print "Solucion exacta"
	(r,c)= brutus(l)
	for e in r:
		print e
	print "Son %s envaces" % c
	elapsed=time.time()-start
	print "time elapsed %s ms" % (elapsed*1000)

def runAprox(l):
	start=time.time()
	print "Solucion aproximada"
	(r,c) = aprox(l)
	for e in r:
		print e
	print "Son %s envaces" % c
	elapsed=time.time()-start
	print "time elapsed %s ms" % (elapsed*1000)


def main():
	l=None
	if not checkArgs():
		return
	l=loadFile()
	if not l:
		return
	caso = sys.argv[1]
	if caso is 'A':
		runAprox(l)
	elif caso is 'E':
		runBrutus(l)
	else:
		print "Algo fallo"

if __name__ == '__main__':
	main()