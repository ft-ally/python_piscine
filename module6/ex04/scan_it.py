#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
	print("none")
else:
	key = sys.argv[1]
	res = re.findall(key, sys.argv[2])
	if len(res) == 0:
		print("none")
	else:
		print(len(res))
