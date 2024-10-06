def main():
	n = int(input())
	m = int(input())
	le = len(str(n * m))
	for i in range(n):
		for j in range(m):
			if j % 2 != 0:
				k = j * n + (n - i)
			else:
				k = j * n + (i + 1)
			print(' ' * (le - len(str(k))) + str(k), end=' ')
		print()


if __name__ == "__main__":
	main()
