def main():
	k = 1
	n = int(input())
	m = int(input())
	le = len(str(n * m))
	for i in range(n):
		for j in range(m):
			print(' ' * (le - len(str(k))) + str(k), end=' ')
			k += 1
		print()


if __name__ == "__main__":
	main()
