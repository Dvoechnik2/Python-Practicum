def main():
	n = int(input())
	print('А Б В')
	for a in range(1, n - 1):
		for b in range(1, n - a):
			c = n - a - b
			if c > 0:
				print(a, b, c)


if __name__ == "__main__":
	main()
