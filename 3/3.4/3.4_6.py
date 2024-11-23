def main():
	m = input()
	suits = ['пик', 'треф', 'бубен', 'червей']
	ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
	deck = [f"{r} {s}" for r in ranks for s in suits if s != m]
	print('\n'.join(deck))


if __name__ == "__main__":
	main()
