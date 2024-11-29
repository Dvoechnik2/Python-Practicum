import json
from sys import stdin


def main():
    nums = set()
    d = dict()
    for num in stdin:
        nums.add(int(num))
    for i in range(0, 10):
        for num in nums:
            if str(i) in str(num):
                if str(i) not in d:
                    d[str(i)] = set()
                d[str(i)].add(num)
    for i in range(0, 10):
        if str(i) in d:
            d[str(i)] = sorted(list(d[str(i)]))
    with open("result.json", "w") as f:
        json.dump(d, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
