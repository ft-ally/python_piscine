#!/usr/bin/env python3
import sys
import re

if len(sys.argv) < 2:
	print("none")
else:
	arg = sys.argv[1:]
	for i in arg:
		if (i.find("ism") == -1):
			print(i + "ism")
		