def main():
	n = int(input())
	workers = []
	flag = False
	for i in range(n):
		name = input()
		workers.append(name)
	for worker in sorted(set(workers)):
		if workers.count(worker) > 1:
			flag = True
			print(f'{worker} - {workers.count(worker)}')
	if not flag:
		print('Однофамильцев нет')


if __name__ == "__main__":
	main()
