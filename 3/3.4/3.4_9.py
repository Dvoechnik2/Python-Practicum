def main():
	n = int(input())
	table = [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
	for row in table:
		print(*row)


if __name__ == "__main__":
	main()
