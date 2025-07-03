#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
	print("none")
else:
	key = input("What was the parameter? ")
	if str(key) != str(sys.argv[1]):
		print("Nope, sorry...")
	else:
		print("Good job!")