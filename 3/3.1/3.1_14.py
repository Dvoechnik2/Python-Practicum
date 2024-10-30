def main():
	a = list(map(int, input().split()))
	p = int(input())
	print(*[x ** p for x in a])


if __name__ == "__main__":
	main()
