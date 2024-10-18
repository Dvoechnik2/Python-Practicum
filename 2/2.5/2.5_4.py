def main():
    n = int(input())
    m = int(input())
    a = [int(input()) for _ in range(n)]
    maxelem = -float('inf')
    for i in range(1, n):
        if abs(a[i] - a[i-1]) < m:
            maxelem = max(maxelem, a[i])
    print(maxelem)


if __name__ == '__main__':
    main()