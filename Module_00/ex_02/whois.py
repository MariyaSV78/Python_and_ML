import sys

if __name__ == "__main__":
	# print(len(sys.argv))
	if len(sys.argv) == 2:
		if ((sys.argv[1]).isnumeric()):
			if int(sys.argv[1]) == 0:
				print ("I'm Zero")
			elif int(sys.argv[1]) % 2 == 0:
				print ("I'm Even")
			else:
				print ("I'm Odd")
		else:
			print ("AssertionError: argument is not an integer")
	elif len(sys.argv) > 2:
			print ("AssertionError: more than one argument are provided")
	else:
		print ("Usage: enter the number")



