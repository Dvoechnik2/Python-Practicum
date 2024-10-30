def main():
	n = int(input())
	m = int(input())
	k1 = set()
	k2 = set()
	for i in range(n):
		k1 = k1 | set(input().split())
	for j in range(m):
		k2 = k2 | set(input().split())
	d = k1 & k2
	if d:
		print(len(d))
	else:
		print('Таких нет')


if __name__ == "__main__":
	main()
