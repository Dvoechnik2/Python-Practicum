import itertools


def main():
    suit_map = {"буби": "бубен", "пики": "пик", "трефы": "треф", "черви": "червей"}
    suits = ["бубен", "пик", "треф", "червей"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    required_suit = suit_map[input()]
    ranks.remove(input())
    pre_comb = input()
    all_comb = tuple(itertools.permutations(itertools.product(ranks, suits), r=3))
    all_comb = (", ".join(" ".join(c) for c in sorted(comb)) for comb in all_comb)
    rez = []
    for comb in sorted(set(all_comb)):
        if required_suit in comb:
            rez += [comb]
    ind = rez.index(pre_comb) + 1
    print(rez[ind])


if __name__ == "__main__":
    main()
