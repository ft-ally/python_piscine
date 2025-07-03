#!/usr/bin/env python3

class Greet():
	def greetings(self, name=""):
		if name == "":
			print("Hello, noble stranger")
		elif name.isalpha() == True:
			print(f"Hello, {name}.")
		else:
			print("Error! It was not a name.")
g = Greet()
g.greetings('Jojo')
g.greetings()
g.greetings('12')
