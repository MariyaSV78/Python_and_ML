
if __name__ == "__main__":
	kata = "The right format"
	print("-" * (42 - len(kata)) + kata, end="") 
	# "{:->42}".format(phrase)