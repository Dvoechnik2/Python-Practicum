def main():
	expr = input()
	print('a b c f')
	for a in range(2):
		for b in range(2):
			for c in range(2):
				f = int(eval(expr))
				print(a, b, c, f)


if __name__ == "__main__":
	main()
