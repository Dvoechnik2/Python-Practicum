def p(x):
	if x == 1:
		return 0
	for i in range(2, int(x ** 0.5) + 1):
		if x % i == 0:
			return 0
	return 1


def main():
	n = int(input())
	k = 0
	for j in range(n):
		k += p(int(input()))
	print(k)


if __name__ == "__main__":
	main()
