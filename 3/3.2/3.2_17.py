def main():
    d = {}
    line = input()
    while line != '':
        name1, name2 = line.split()
        if name1 in d:
            d[name1].append(name2)
        else:
            d[name1] = [name2]
        if name2 in d:
            d[name2].append(name1)
        else:
            d[name2] = [name1]
        line = input()
    for name in sorted(d):
        friends = d[name]
        s = set()
        for friend in friends:
            s.update(d[friend])
        s.discard(name)
        s.difference_update(friends)
        print(f'{name}:', ', '.join(sorted(s)))


if __name__ == "__main__":
    main()
