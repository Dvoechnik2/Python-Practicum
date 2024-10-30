def main():
	alf = [0] * 34
	s = input()
	t = ord('а')
	while s != 'ФИНИШ':
		for x in s:
			if x != ' ':
				i = ord(x.lower()) - t
				alf[i] += 1
		s = input()
	print(chr(alf.index(max(alf)) + t))


if __name__ == "__main__":
	main()
