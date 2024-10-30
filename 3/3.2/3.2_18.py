def main():
	n = int(input())
	dict = {}
	for _ in range(n):
		x, y = map(int, input().split(" "))
		d = (x // 10, y // 10)
		if d not in dict:
			dict[d] = 0
		dict[d] += 1
	print(max(dict.values()))


if __name__ == "__main__":
	main()
