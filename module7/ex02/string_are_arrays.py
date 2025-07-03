#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 2:
	print("none")
else:
	res = re.findall('z', sys.argv[1])
	if len(res) == 0:
		print("none")
	else:
		i = 0
		while i != len(res):
			print("z", end="")
			i += 1
