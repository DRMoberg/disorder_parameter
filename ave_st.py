from __future__ import division

import numpy as np
import sys
from itertools import chain, islice
import math
import operator

if (len(sys.argv) != 3):
    print "usage: python executable.py st_tot.txt output.txt"
    sys.exit()

layers = 24
tot = 0
sums = []

with open(sys.argv[1], 'r') as inp:
	with open(sys.argv[2],'w') as outp:

		while True:
	    	lines_gen = list(islice(inp,layers))
	    	if not lines_gen:
	        	break
	    	for lines in lines_gen:
				numfl = map(float, numstr)
				tot = tot + 1
				sums[lines] += numfl

			for i in range(0,len(sums)):
				outp.write(sums[i]/)

inp.close()
outp.close()
