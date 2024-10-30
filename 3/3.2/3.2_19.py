def main():
	n = int(input())
	toys = {}
	for i in range(n):
		name, items = input().split(": ")
		items = set(items.split(", "))
		for toy in items:
			toys[toy] = toys.get(toy, 0) + 1
	unique_toys = sorted(toy for toy, count in toys.items() if count == 1)
	print(*unique_toys, sep="\n")


if __name__ == "__main__":
	main()
