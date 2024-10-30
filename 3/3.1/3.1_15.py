from math import gcd


def main():
	a = list(map(int, input().split()))
	p = a[0]
	for x in a:
		p = gcd(p, x)
	print(p)


if __name__ == "__main__":
	main()
