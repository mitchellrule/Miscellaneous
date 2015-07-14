from time import sleep


spaces = 20

while True:
	print " " * spaces, "*" * (41 - (2 * spaces))
	spaces -= 1
	if (spaces == 0):
		spaces = 20
	sleep(0.01)	