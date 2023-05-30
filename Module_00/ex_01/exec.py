import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('args', nargs = '*', default='Enter arguments')
	args = parser.parse_args()
	i = 0
	while i < len(args.args):
		print(args.args[i].swapcase()[::-1], end = ' ')
		i = i + 1

