def main():
	lenth = int(input())
	a = []
	n = int(input())
	for i in range(n):
		s = input()
		if len(s) > lenth:
			a.append(s[:lenth-3] + '...')
		else:
			a.append(s)
	print(*a, sep='\n')


if __name__ == "__main__":
	main()
