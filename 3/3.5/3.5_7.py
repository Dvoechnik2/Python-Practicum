def main():
    file_name = input("Введите имя файла: ").strip()
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read()  # Считываем весь файл как строку
    numbers = [float(num) for num in data.split()]
    print(len(numbers))
    print(sum(1 for num in numbers if num > 0))
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers))
    print(round(sum(numbers) / len(numbers), 2) if len(numbers) > 0 else 0)


if __name__ == "__main__":
    main()

