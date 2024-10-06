def main():
	n = int(input())
	k = 0
	for i in range(n):
		s = input()
		if s[::-1] == s:
			k += 1
	print(k)


if __name__ == "__main__":
	main()
