def main():
	n = int(input())
	print(f'А Б В')
	for i in range(1, n - 1):
		for j in range(1, n - 1):
			for z in range(1, n - 1):
				if i + j + z == n:
					print(i, j, z)


if __name__ == "__main__":
	main()
