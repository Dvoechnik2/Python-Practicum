def sis(n ,b):
	s = 0
	while n != 0:
		s += n % b
		n //= b
	return s


def main():
	n = int(input())
	smax = -1
	bmax = -1
	for b in range(2, 11):
		s = sis(n, b)
		if s > smax:
			smax = s
			bmax = b
	print(bmax)



if __name__ == "__main__":
	main()
