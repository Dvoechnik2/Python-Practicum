def main():
	n = int(input())
	maxname = ''
	maxs = 0
	for i in range(n):
		name = input()
		summ = 0
		s = input()
		for x in s:
			summ += int(x)
		if summ >= maxs:
			maxname = name
			maxs = summ
	print(maxname)

if __name__ == "__main__":
	main()
