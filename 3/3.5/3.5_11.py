import json


def main():
	input_file = input()
	output_file = input()
	with open(input_file, 'r', encoding='utf-8') as f:
		data = f.read()
	numbers = [int(num) for num in data.split()]
	stats = {
		"count": len(numbers),
		"positive_count": sum(1 for num in numbers if num > 0),
		"min": min(numbers),
		"max": max(numbers),
		"sum": sum(numbers),
		"average": round(sum(numbers) / len(numbers), 2) if len(numbers) > 0 else 0
	}
	with open(output_file, 'w', encoding='utf-8') as f:
		json.dump(stats, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
	main()
