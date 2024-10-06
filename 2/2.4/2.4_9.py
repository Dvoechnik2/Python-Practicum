def main():
	n = int(input())
	l = ''
	for i in range(n):
		a = input()
		m = -1
		for x in a:
			m = max(m, int(x))
		l += str(m)
	print(l)


if __name__ == "__main__":
	main()
