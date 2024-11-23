from itertools import count, islice


def main():
	n = int(input())
	m = int(input())
	nums = islice(count(1), n * m)
	width = len(str(n * m))
	for i in range(n):
		row = [f"{next(nums):>{width}}" for _ in range(m)]
		print(*row)


if __name__ == "__main__":
	main()
