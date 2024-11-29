def main():
    n = int(input())
    for _ in range(n):
        m = ''
        # a, s, b = input().split('%')
        s = '012345678'
        a = 7
        b = 3
        m = s[:a + 1][::-1][::3][:2][::-1]

        # for x in range(a, max(a - 3 * b, -1), -3):
        #     m = s[x] + m
        print(m)


if __name__ == '__main__':
    main()
