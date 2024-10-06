def main():
	n = int(input())
	k = 1
	c = 1
	while c <= n:
		for i in range(k):
			if c > n:
				break
			print(c, end=' ')
			c += 1
		print()
		k += 1


if __name__ == "__main__":
	main()
