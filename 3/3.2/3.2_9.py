def main():
	dict = {}
	line = input()
	while line != '':
		for x in line.split():
			if x in dict:
				dict[x] += 1
			else:
				dict[x] = 1
		line = input()
	for key, value in dict.items():
		print(key, value)


if __name__ == "__main__":
	main()
