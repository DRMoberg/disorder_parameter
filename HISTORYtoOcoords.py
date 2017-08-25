from __future__ import division

import numpy as np
import sys
from itertools import chain, islice
import math

histfile = sys.argv[1]
hsplit = histfile.split('.')
outp = "Ocoords."+hsplit[1]

linebody = open(sys.argv[1]).readlines()
open('noheader.txt', 'w').writelines(linebody[4:])

output = open(outp, 'w')

if (len(sys.argv) != 2):
    print "usage: python executable.py HISTORY_file"
    sys.exit()

searchH = 'HW'

with open('noheader.txt', 'r') as filestream:
	with output as f2:

		while True:
		    lines_gen = list(islice(filestream,2))
		    if not lines_gen:
		        break
		    counter = 0
		    for line in lines_gen:
			if (counter == 0):
				if searchH in line:
					break
				else:
					Ocheck = 1

			if (counter == 1):
				f2.write(line)

			counter = counter + 1

filestream.close()
f2.close()
