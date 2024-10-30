def main():
	a = [input() for i in range(int(input()))]
	s = input().lower()
	print(*[x for x in a if s in x.lower()], sep='\n')


if __name__ == "__main__":
	main()
