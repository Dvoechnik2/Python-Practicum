def main():
	s = input().lower()
	s = s.replace(' ','')
	print("YES" if s == s[::-1] else "NO")


if __name__ == "__main__":
	main()
