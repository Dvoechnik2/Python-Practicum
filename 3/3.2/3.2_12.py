def main():
	n = int(input())
	b = {input() for _ in range(n)}
	m = int(input())

	for i in range(m):
		s = int(input())
		b -= {input() for _ in range(s)}

	r = sorted(b)
	print('\n'.join(r) if r else "Готовить нечего")


if __name__ == "__main__":
	main()
