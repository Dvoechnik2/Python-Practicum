from sys import stdin


def main():
	s = 0
	for line in stdin:
		s += sum(map(int, line.strip().split()))
	print(s)


if __name__ == "__main__":
	main()
