from sys import stdin


def main():
    for line in stdin:
        line = line.rstrip()
        if line.startswith("#") or not line:
            continue
        c = line.split("#")[0].rstrip()
        if c:
            print(c)


if __name__ == "__main__":
    main()

