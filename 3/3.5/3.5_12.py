def dig(number):
    evens = 0
    odds = 0
    number = str(number)
    for digit in number:
        if digit.isdigit():
            if int(digit) % 2 == 0:
                evens += 1
            else:
                odds += 1
    return evens, odds


def main():
    input_file = input()
    even_file = input()
    odd_file = input()
    eq_file = input()
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    even_lines = []
    odd_lines = []
    eq_lines = []
    for line in lines:
        numbers = line.split()
        even_group = []
        odd_group = []
        eq_group = []
        for num in numbers:
            evens, odds = dig(num)
            if evens > odds:
                even_group.append(num)
            elif odds > evens:
                odd_group.append(num)
            else:
                eq_group.append(num)
        even_lines.append(" ".join(even_group))
        odd_lines.append(" ".join(odd_group))
        eq_lines.append(" ".join(eq_group))
    with open(even_file, "a", encoding="utf-8") as ef:
        ef.write("\n".join(even_lines) + "\n")
    with open(odd_file, "a", encoding="utf-8") as of:
        of.write("\n".join(odd_lines) + "\n")
    with open(eq_file, "a", encoding="utf-8") as qf:
        qf.write("\n".join(eq_lines) + "\n")


if __name__ == "__main__":
    main()
