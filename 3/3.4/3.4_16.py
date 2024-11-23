from itertools import combinations


def main():
	suit = input()
	rank_exc = input()
	suits = ["бубен", "пик", "треф", "червей"]
	ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
	suit_map = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
	required_suit = suit_map[suit]
	deck = [f"{r} {s}" for s in suits for r in ranks if r != rank_exc]
	valid_combinations = [comb for comb in combinations(deck, 3) if any(required_suit in card for card in comb)]
	sorted_combinations = sorted([", ".join(sorted(comb)) for comb in valid_combinations])
	print(*sorted_combinations[:10], sep='\n')


if __name__ == "__main__":
	main()
