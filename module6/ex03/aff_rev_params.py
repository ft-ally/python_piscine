#!/usr/bin/env python3
import sys

if len(sys.argv) <= 3:
	print ("none")
else:
	argc = len(sys.argv) - 1
	while argc :
		print(sys.argv[argc])
		argc -= 1