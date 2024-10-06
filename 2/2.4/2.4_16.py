def main():
	n = int(input())
	le2 = int(input())
	for i in range(1, n + 1):
		if i > 1:
			print('-' * (n - 1 + le2 * n))
		a = []
		k = i
		for j in range(n):
			le = le2 - len(str(k))
			a.append(' ' * (le // 2) + str(k) + (le - (le // 2)) * ' ')
			k += i
		print('|'.join(a))


if __name__ == "__main__":
	main()
