def main():
    file1 = input()
    file2 = input()
    out = input()
    with open(file1, 'r', encoding='utf-8') as file1:
        words1 = set(file1.read().split())
    with open(file2, 'r', encoding='utf-8') as file2:
        words2 = set(file2.read().split())
    unique_words = (words1.symmetric_difference(words2))
    sorted_unique_words = sorted(unique_words)
    with open(out, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(sorted_unique_words))

if __name__ == "__main__":
    main()

