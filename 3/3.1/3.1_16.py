def main():
	le = int(input())
	n = int(input())
	for i in range(n):
		s = input()
		if le - len(s) <= 3:
			print(s[:le - 2] + '...')
			break
		else:
			print(s)
		le -= len(s)


if __name__ == "__main__":
	main()
