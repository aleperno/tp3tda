#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

class objeto():
	def __init__(self, tam):
		self.tam = tam

	def __str__():
		return self.tam

def loadFile():
	try:
		_file = open(sys.argv[2])
	except IOError:
		print "El archivo no pudo ser abierto, verificar parametros"
		usage()

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
	if not checkArgs() or not loadFile():
		return

if __name__ == '__main__':
	main()