def main():
	a = list(map(int, input().split()))
	for i in range(len(a)):
		elem = bin(a[i])[2:]
		a[i] = {'digits': len(elem),
				'units': elem.count('1'),
				'zeros': elem.count('0'),
				}
	print(a)


if __name__ == "__main__":
	main()
