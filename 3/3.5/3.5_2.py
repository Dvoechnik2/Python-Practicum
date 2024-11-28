from sys import stdin


def main():
	s = []
	e = []
	for line in stdin:
		s.append(int(line.split()[1]))
		e.append(int(line.split()[2]))
	print(round((sum(e) / len(e)) - (sum(s) / len(s))))


if __name__ == "__main__":
	main()
