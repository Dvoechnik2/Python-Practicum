def main():
    d = dict()
    while (s := input()):
        for word in s.split():
            if len(word) not in d:
                d[len(word)] = [word.upper()]
            else:
                d[len(word)].append(word.upper())
    for key, value in d.items():
        print(f'{key}: ' + '; '.join(sorted(set(value), reverse=True)))


if __name__ == '__main__':
    main()