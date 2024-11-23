def main():
	s = input().split()
	s = [f'{i + 1}. {s[i]}' for i in range(len(s))]
	print(*s, sep='\n')


if __name__ == "__main__":
	main()
