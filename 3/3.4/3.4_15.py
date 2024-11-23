from itertools import permutations


def main():
	buys = []
	n = int(input())
	for _ in range(n):
		buys.extend(input().split(', '))
	buys = sorted(buys)
	buys = permutations(buys, 3)

	for buy in buys:
		print(*buy)


if __name__ == "__main__":
	main()
