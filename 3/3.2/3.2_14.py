def main():
	n = int(input())
	p = {input().strip() for _ in range(n)}
	m = int(input())
	r = []

	for _ in range(m):
		b = input().strip()
		k = int(input())
		ingr = {input().strip() for _ in range(k)}
		if ingr.issubset(p):
			r.append(b)

	if r:
		print("\n".join(sorted(r)))
	else:
		print("Готовить нечего")


if __name__ == "__main__":
	main()
