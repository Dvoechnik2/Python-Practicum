def main():
	n = int(input())
	names = [input().strip() for _ in range(n)]
	games = [f"{names[i]} - {names[j]}" for i in range(n) for j in range(i + 1, n)]
	print(*games, sep="\n")


if __name__ == "__main__":
	main()
