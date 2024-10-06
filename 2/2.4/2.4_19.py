def main():
	n = int(input())
	le = len(str(n // 2 + 1))
	for i in range(n):
		for j in range(n):
			k = str(1 + min(i, j, n - i - 1, n - j - 1))
			k = ' ' * (le - len(k)) + k
			print(k, end=' ')
		print()



if __name__ == "__main__":
	main()
