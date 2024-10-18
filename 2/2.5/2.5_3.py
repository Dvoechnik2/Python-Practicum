def main():
    n = int(input())
    m = int(input())
    d = int(input())
    for i in range(n, m + 1, d):
        print(i, end=' - ')
    for i in range(m, n - 1, -d):
        if i != n:
            print(i, end=' - ')
        else:
            print(i)


if __name__ == '__main__':
    main()