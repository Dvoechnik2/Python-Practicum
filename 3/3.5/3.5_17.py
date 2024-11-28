from lib2to3.fixes.fix_input import context


def main():
    hidden_message = []
    with open("secret.txt", 'r', encoding='utf-8') as file:
        content = file.read()
    for char in content:
        code = ord(char)
        if code < 128:
            hidden_message.append(char)
        else:
            hidden_message.append(chr(code & 0xFF))
    print(''.join(hidden_message))


if __name__ == "__main__":
    main()
