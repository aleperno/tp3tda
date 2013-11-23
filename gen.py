#!/usr/bin/python

import sys
from random import randint as r

_file = open('data_aux.txt','w+')
n = int(sys.argv[1])
_file.write(sys.argv[1]+'\n')
_file.write("\n")
for i in range(n):
	num=r(1,10)
	if num<10:
		s='0,'+str(num)+'\n'
	else:
		s='1,0\n'
	_file.write(s)