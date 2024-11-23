import itertools


def main():
	expr = input()
	pere = set()
	for x in expr:
		if 65 <= ord(x) <= 90:
			pere.add(x)
	print(*sorted(pere), 'F')
	values = itertools.product([0, 1], repeat=len(pere))
	for v in values:
		exec(', '.join(sorted(pere)) + '= v')
		f = int(eval(expr))
		print(*v, f)


if __name__ == "__main__":
	main()
