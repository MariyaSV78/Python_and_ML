import sys
import string

def  text_analyzer(text=None):
	"""
		This function counts the number of upper characters, lower characters,
		punctuation and spaces in a given text.
	"""
	
	# if len(text) == 0:
	# 	print("What is the text to analyze?")
	# 	text = input (">> ")
	if text is None:
		print("What is the text to analyze?")
		text = input (">> ")
	text = str(text)
	if text.isnumeric():
		print("AssertionError: argument is not a string")
		return
	char_count = len(text)
	upper_count = lower_count = punct_count = space_count = 0
	for c in text:
		if c.isupper():
			upper_count += 1
		if c.islower():
			lower_count += 1
		if c.isspace():
			space_count += 1
		if c in string.punctuation:
			punct_count += 1



	print(f"The text contains {char_count} character(s):")
	print(f"- {upper_count} upper letter(s)")
	print(f"- {lower_count} lower letter(s)")
	print(f"- {punct_count} punctuation mark(s)")
	print(f"- {space_count} space(s)")


if __name__ == "__main__":
	if len(sys.argv) == 1:
		text_analyzer()
	else: 
		text = sys.argv[1]
		text_analyzer(text)