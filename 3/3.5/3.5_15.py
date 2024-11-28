import json
from sys import stdin


def main():
	responses = []
	for num in stdin:
		responses.append(num.strip())
	patterns = []
	points = []
	with open("scoring.json", 'r') as f:
		data = json.load(f)
	for group_of_test in data:
		point_per_test = group_of_test['points'] // len(group_of_test['tests'])
		for test in group_of_test['tests']:
			patterns.append(test['pattern'])
			points.append(point_per_test)
	score = 0
	for i in range(len(responses)):
		if responses[i] == patterns[i]:
			score += points[i]
	print(score)


if __name__ == "__main__":
	main()
