def main():
	s = []
	n = int(input())
	for _ in range(n):
		s.extend(input().split(', '))
	s = sorted(s)
	s = [f'{i + 1}. {s[i]}' for i in range(len(s))]
	print(*s, sep='\n')


if __name__ == "__main__":
	main()
