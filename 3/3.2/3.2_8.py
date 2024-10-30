def main():
	n = int(input())
	poriges = {}
	for i in range(n):
		kid, *kashi = input().split(' ')
		for por in kashi:
			if por in poriges:
				poriges[por].append(kid)
			else:
				poriges[por] = [kid]
	k = input()
	if k in poriges:
		print(*sorted(poriges[k]), sep='\n')
	else:
		print('Таких нет')


if __name__ == "__main__":
	main()
