import os
import math


def main():
    direction = os.path.dirname(__file__)
    file = input()
    file_size = os.path.getsize(direction + "/" + file)
    GOST = ["Б", "КБ", "МБ", "ГБ"]
    ind = 0
    while file_size >= 1024 and ind < len(GOST) - 1:
        file_size = math.ceil(file_size / 1024)
        ind += 1
    print(str(file_size) + GOST[ind])


if __name__ == "__main__":
    main()