def main():
	s = input().split()
	for i in range(1, len(s) + 1):
		print(*s[:i])


if __name__ == "__main__":
	main()
