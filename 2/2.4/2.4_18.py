def main():
	a = []
	n = int(input())
	k = 1
	c = 1
	while c <= n:
		s = ''
		for i in range(k):
			if c > n:
				break
			s += str(c) + ' '
			c += 1
		a.append(s.rstrip())
		k += 1
	maxl = len(a[-1])
	for x in a:
		print(' ' * ((maxl - len(x)) // 2) + x)


if __name__ == "__main__":
	main()
