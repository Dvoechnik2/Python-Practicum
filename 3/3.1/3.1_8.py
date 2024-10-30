def main():
	n = int(input())
	for i in range(n):
		s = input()
		if 'зайка' in s:
			print(s.find('зайка') + 1)
		else:
			print('Заек нет =(')


if __name__ == "__main__":
	main()
