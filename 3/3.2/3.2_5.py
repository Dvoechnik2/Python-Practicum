def main():
	n = int(input())
	m = int(input())
	d = set()
	k = 0
	for i in range(n + m):
		kid = input()
		if kid in d:
			k += 1
		d.add(kid)

	if len(d) - k:
		print(len(d) - k)
	else:
		print('Таких нет')


if __name__ == "__main__":
	main()
