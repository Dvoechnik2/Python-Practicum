def main():
	m = int(input())
	porridges = [input() for _ in range(m)]
	n = int(input())
	print(*[porridges[i % m] for i in range(n)], sep='\n')


if __name__ == "__main__":
	main()
