def main():
    s = input().split()
    stack = []
    for x in s:
        if x.isdigit() or (x[0] == '-' and len(x) > 1):
            stack.append(int(x))
        else:
            b = stack.pop()
            a = stack.pop()
            if x == '+':
                stack.append(a + b)
            elif x == '-':
                stack.append(a - b)
            elif x == '*':
                stack.append(a * b)
    print(stack[0])

if __name__ == "__main__":
    main()

