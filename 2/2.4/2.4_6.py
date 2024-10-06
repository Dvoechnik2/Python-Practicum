from math import gcd


def main():
	n = int(input())
	a = int(input())
	b = int(input())
	c = gcd(a, b)
	for i in range(n - 2):
		c = gcd(c, int(input()))
	print(c)



if __name__ == "__main__":
	main()
