def main():
	a = set()
	n = int(input())
	for i in range(n):
		a = a | set(input().split(' '))
	print(*a, sep='\n')


if __name__ == "__main__":
	main()
