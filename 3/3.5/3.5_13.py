import json
from sys import stdin


def main():
	fi = input()
	with open(fi, 'r', encoding="UTF-8") as f:
		data = json.load(f)
	for line in stdin:
		key, value = line.strip().split(' == ')
		data[key] = value
	with open(fi, 'w', encoding="UTF-8") as f:
		json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
	main()
