def main():
	file_name = input()
	with open(file_name, 'r') as f:
		data = f.readlines()[-int(input()):]
	print(*data, sep='')


if __name__ == "__main__":
	main()
