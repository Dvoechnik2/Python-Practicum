def main():
	s = input()
	le = 1
	for i in range(1, len(s)):
		if s[i] == s[i - 1]:
			le += 1
		else:
			print(s[i - 1], le)
			le = 1
	print(s[-1], le)


if __name__ == "__main__":
	main()
