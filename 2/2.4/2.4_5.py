def main():
	n = int(input())
	k = 0
	for i in range(n):
		s = input()
		c = False
		while s != 'ВСЁ':
			c += ('зайка' in s)
			s = input()
		if c:
			k += 1
	print(k)


if __name__ == "__main__":
	main()
