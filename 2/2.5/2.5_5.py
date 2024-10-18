def main():
    n = int(input())
    min_average = float("inf")
    for i in range(n):
        line = input()
        k = 0
        s = 0
        while line != 'end':
            s += int(line)
            k += 1
            line = input()
        min_average = min(s / k, min_average)
    print('{:.2f}'.format(min_average))


if __name__ == '__main__':
    main()