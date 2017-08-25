from __future__ import division

import numpy as np
import sys
from itertools import chain, islice
import math
import operator

if (len(sys.argv) != 3):
    print "usage: python executable.py sorted_Ocoords output.txt"
    sys.exit()

a = 4.492
NL = 30
Ocoords = []
sort = []
rij = []

with open(sys.argv[1], 'r') as filestream:
	while True:
	    lines_gen = list(islice(filestream,30))
	    if not lines_gen:
	        break
	    for lines in lines_gen:
			numstr = lines.split()
			numfl = map(float, numstr)
			Ocoords.append(numfl)

filestream.close()

def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]

Olayer = chunks(Ocoords,30)

def subli(A,B):
	return map(operator.sub,A,B)

#for i in range(len(Ocoords)):
#	for j in range(len(Ocoords)):
#		rij[i][j] = subli(Ocoords[i],Ocoords[j])

#print rij[0]

k1 = [2 * math.pi / a,2 * math.pi / a /math.sqrt(3),0]
k2 = [0,-4 * math.pi / a /math.sqrt(3),0]
k3 = [-2 * math.pi / a,2 * math.pi / a /math.sqrt(3),0]
k = [k1,k2,k3]

#print subli(Ocoords[0],Ocoords[1])
#print len(Ocoords)
#print math.cos(np.dot(k[0],subli(Ocoords[0],Ocoords[1])))+math.cos(np.dot(k[1],subli(Ocoords[0],Ocoords[1])))+math.cos(np.dot(k[2],subli(Ocoords[0],Ocoords[1])))
#print math.cos(np.dot(k[0],subli(Ocoords[1],Ocoords[0])))+math.cos(np.dot(k[1],subli(Ocoords[1],Ocoords[0])))+math.cos(np.dot(k[2],subli(Ocoords[1],Ocoords[0])))

def STval(layer):
	st = 0
	for i in range(NL*(layer-1),NL*layer):
		for j in range(NL*(layer-1),NL*layer):
			st += math.cos(np.dot(k[0],subli(Ocoords[i],Ocoords[j]))) + math.cos(np.dot(k[1],subli(Ocoords[i],Ocoords[j]))) + math.cos(np.dot(k[2],subli(Ocoords[i],Ocoords[j])))
	return st/3/NL**2

with open(sys.argv[2], 'w') as output:
	for layer in range(0,int(len(Ocoords)/NL)):
#		print str(layer+1) + '    ' + str(STval(layer))
		output.write(str(layer+1) + '    ' + str(STval(layer)) + '\n')

output.close()	
