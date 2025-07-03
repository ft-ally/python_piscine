#!/usr/bin/env python3
import sys

class Down:
	def downcase_it(str):
		print(str.lower())
		
if len(sys.argv) < 2:
	print("none")
else:
	args = sys.argv[1:]
	for arg in args:
		Down.downcase_it(arg)
