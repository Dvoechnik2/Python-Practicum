from itertools import permutations


def main():
	n = int(input())
	athletes = [input().strip() for _ in range(n)]
	perm = sorted(permutations(athletes))
	for p in perm:
		print(", ".join(p))


if __name__ == "__main__":
	main()
