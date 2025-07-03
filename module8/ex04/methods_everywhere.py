#!/usr/bin/env python3
import sys

class Shrink():
	def shrink_it(self, string):
		new = slice(0, 8)
		print(string[new])

class Enlarge():
	def enlarge_it(self, string):
		i = len(string)
		z_str = ""
		while i < 8:
			z_str += 'Z'
			i += 1
		print(string + z_str)

if len(sys.argv) < 2:
	print("none") 
else:
	args = sys.argv[1:]
	for arg in args:
		if len(arg) >= 8:
			s = Shrink()
			s.shrink_it(arg)
		elif len(arg) <= 8:
			e = Enlarge()
			e.enlarge_it(arg)
		else:
			print(arg)
		