def format_data(data):
	if data < 10:
		data = f'0{data}'
	return(data)


if __name__ == "__main__":
	kata = (2019, 9, 25, 3, 30)
	list = []
	for i in range (1,5):
		d = format_data(kata[i])
		list.insert(i, d)
	print(f"{list[0]}/{list[1]}/{kata[0]} {list[2]}:{list[3]}")
