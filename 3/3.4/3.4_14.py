from itertools import permutations


def main():
	n = int(input())
	athletes = sorted([input().strip() for _ in range(n)])
	perm = permutations(athletes, 3)

	for p in perm:
		print(", ".join(p))


if __name__ == "__main__":
	main()
