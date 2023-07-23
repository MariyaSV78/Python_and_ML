import sys
if __name__ == "__main__":
	if len(sys.argv) == 3 and isinstance(sys.argv[1], str) and sys.argv[2].isdigit():
		words = (sys.argv[1]).split()
		print([word for word in words if len(word) >= int(sys.argv[2])])
	else:
		print("ERROR")


# import sys
# if __name__ == "__main__":
# 	if len(sys.argv) == 3 and isinstance(sys.argv[1], str) and sys.argv[2].isdigit():
# 		words = (sys.argv[1]).split()
# 		new_list = []
# 		for word in words:
# 			if len(word) >= int(sys.argv[2]):
# 				new_list = new_list.append(word)
# 		print(new_list)
# 	else:
# 		print("ERROR")
