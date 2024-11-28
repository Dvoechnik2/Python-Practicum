from sys import stdin


def main():
	words = []
	palindrome = []
	for line in stdin:
		words.extend(line.strip().split(' '))
	for word in words:
		if word.lower() == word[::-1].lower():
			palindrome.append(word)
	palindrome = sorted(set(palindrome))
	print(*palindrome, sep='\n')


if __name__ == "__main__":
	main()