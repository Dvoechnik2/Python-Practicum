def main():
    a = int(input())
    line = input()
    b = int(input())
    if len(line) % 2 == 0 and ' ' in line:
        print(a + b)
    elif len(line) % 2 == 0 and ' ' not in line:
        print(a - b)
    elif len(line) % 2 != 0 and ' ' in line:
        print(a * b)
    else:
        print(a // b)


if __name__ == '__main__':
    main()