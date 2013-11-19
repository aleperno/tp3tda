#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from types import *

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
		s = "["
		for i in self._list:
			s += "%s, " % i
		s += "]"
		return s

	def envasar(self, obj):
		if (self.count+obj.getTam())<=self.max:
			self._list.append(obj)
			self.count+=obj.getTam()
			return True
		else:
			return False

def aprox(l):
	r=[]
	e=Envase()
	for obj in l:
		if not e.envasar(obj):
			r.append(e)
			e=Envase() #Se abre otro envase
			e.envasar(obj)
	r.append(e)
	return r

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

def main():
	l=None
	if not checkArgs():
		return
	l=loadFile()
	if not l:
		return
	r = aprox(l)
	for l in r:
		print l
if __name__ == '__main__':
	main()