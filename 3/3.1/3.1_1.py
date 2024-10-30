def main():
	n = int(input())
	flag = True
	for  i in range(n):
		s = input()
		flag *= 1072 <= ord(s[0]) <= 1075
	if flag:
		print('YES')
	else:
		print('NO')



if __name__ == "__main__":
	main()
