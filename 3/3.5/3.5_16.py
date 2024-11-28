from sys import stdin


def main():
    query = input().strip()
    query = ' '.join(query.lower().split())
    filenames = []
    for file in stdin:
        filenames.append(file.strip())
    matching_files = []
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            normalized_content = ' '.join(content.lower().split())
            if query in normalized_content:
                matching_files.append(filename)
    if matching_files:
        print('\n'.join(matching_files))
    else:
        print("404. Not Found")


if __name__ == "__main__":
    main()

