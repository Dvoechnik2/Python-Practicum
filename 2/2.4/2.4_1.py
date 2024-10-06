def main():
	n = int(input())
	for i in range(1, n + 1):
		for j in range(i, i * n + 1, i):
			print(j, end=" ")
		print()


if __name__ == "__main__":
	main()
