def main():
	n = int(input())
	m = int(input())
	d = set()

	for i in range(n + m):
		kid = input()
		if kid in d:
			d.remove(kid)
		else:
			d.add(kid)

	if len(d):
		print(*sorted(list(d)), sep='\n')
	else:
		print('Таких нет')


if __name__ == "__main__":
	main()
