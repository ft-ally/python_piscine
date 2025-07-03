#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
	print("none")
else:
	array = []
	start = int(sys.argv[1])
	end = int(sys.argv[2])
	if start >= end:
		print("error: first number is equal to or more than second number")
	else:
		res = range(start, end + 1)
		for number in res:
			array.append(number)
		print(array)