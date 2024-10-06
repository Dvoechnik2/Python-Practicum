def main():
	n = int(input())
	s = 0
	for i in range(n):
		c = input()
		for x in c:
			s += int(x)
	print(s)


if __name__ == "__main__":
	main()