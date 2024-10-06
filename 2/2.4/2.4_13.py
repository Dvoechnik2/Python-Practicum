def main():
	n = int(input())
	m = int(input())
	le = len(str(n * m))
	for i in range(1, n + 1):
		k = i
		for j in range(m):
			print(' ' * (le - len(str(k))) + str(k), end=' ')
			k += n
		print()


if __name__ == "__main__":
	main()
