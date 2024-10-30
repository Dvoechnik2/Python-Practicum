def main():
	a = []
	s = input()
	while s != '':
		if s[-3:] != '@@@':
			if s[:2] == '##':
				a.append(s[2:])
			else:
				a.append(s)
		s = input()
	print(*a, sep='\n')


if __name__ == "__main__":
	main()
