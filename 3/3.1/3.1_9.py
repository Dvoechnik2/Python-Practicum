def main():
	a = []
	s = input()
	while s != '':
		if s[0] != '#':
			if '#' in s:
				s = s.split(' # ')
				a.append(s[0])
			else:
				a.append(s)
		s = input()
	print(*a, sep='\n')


if __name__ == "__main__":
	main()
