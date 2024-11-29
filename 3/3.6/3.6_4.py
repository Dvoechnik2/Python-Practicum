from itertools import product


def main():
    n = int(input())
    letters = []
    for _ in range(n):
        letters.append(input().split('-'))
    words = {''.join(word) for word in product(*letters)}
    sorted_words = sorted(words)
    for word in sorted_words:
        print(word)


if __name__ == '__main__':
    main()

