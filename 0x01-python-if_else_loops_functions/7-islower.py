#!/usr/bin/python3
def islower(c):
	c = ord(c)
	if c >= 97 and c <= 122:
		print("{:c} is lower".format(c))
		return True
	else:
		print("{:c} is upper".format(c))
		return False
