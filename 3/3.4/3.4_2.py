def main():
	a = input().split(', ')
	b = input().split(', ')
	m = min(len(a), len(b))
	p = [f"{a[i]} - {b[i]}" for i in range(m)]
	print(*p, sep='\n')


if __name__ == "__main__":
	main()
