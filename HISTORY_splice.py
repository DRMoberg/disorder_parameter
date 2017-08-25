from __future__ import division

import sys
from itertools import chain, islice, count
import math

natoms = 2160			# num of atoms in system
nlines = (2*natoms)+4		# num of lines per frame

if (len(sys.argv) != 2):
	print "usage: python executable.py input_file.xyz"
	sys.exit()

file_large = sys.argv[1]

flen = sum(1 for line in open(file_large))	# lines in file
print flen
nframes = flen/nlines	# frames in file

# Divides and writes smaller chunks into their own files

def chunks(iterable, n):
	"chunks(ABCDE,2) => AB CD E"
	iterable = iter(iterable)
	while True:
		# store one line in memory,
		# chain it to an iterator on the rest of the chunk
		yield chain([next(iterable)], islice(iterable, n-1))

with open(file_large) as bigfile:
	for i, lines in enumerate(chunks(bigfile, nlines)):
		file_split = '{}.{}'.format('history', str(i))
		with open(file_split, 'w') as f:
			f.writelines(lines)
