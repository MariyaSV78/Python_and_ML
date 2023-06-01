import sys

if __name__ == "__main__":
	if len(sys.argv) == 3:
		if sys.argv[1].isnumeric() and sys.argv[2].isnumeric():
			A = int(sys.argv[1])
			B = int(sys.argv[2])
			print ("Sum:	   ", A + B)
			print ("Difference:", A - B)
			print ("Product:   ", A * B)
			if B == 0:
				print ("Quotient:   ERROR (division by zero)")
				print ("Remainder:  ERROR (modulo by zero")
			else:
				print("Quotient:  ", A / B  )
				print("Remainder: ", A % B  )
		else:
			print ("AssertionError: only integers")
	elif len(sys.argv) == 1:
		print ("Usage: python operations.py <number1> <number2>")
	else:
		print ("AssertionError: too many arguments")