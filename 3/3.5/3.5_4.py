from sys import stdin


def main():
	z = []
	for line in stdin:
		z.append(line.strip())
	word = z[-1].lower()
	for x in z[:-1]:
		if word in x.lower():
			print(x)


if __name__ == "__main__":
	main()
