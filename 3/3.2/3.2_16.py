def main():
	s = set()
	line = input()
	while line != '':
		line = line.split()
		for i in range(len(line)):
			if line[i] == 'зайка':
				if i > 0:
					s.add(line[i - 1])
				if i < len(line) - 1:
					s.add(line[i + 1])
		line = input()
	print(*s, sep='\n')


if __name__ == "__main__":
	main()
