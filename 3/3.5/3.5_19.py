def main():
	key = int(input())
	message = ''
	with open('public.txt', 'r') as f:
		data = f.read()
		for s in data:
			if 65 <= ord(s) <= 90:
				message += chr(65 + ((ord(s) - 65 + key) % 26))
			elif 97 <= ord(s) <= 122:
				message += chr(97 + ((ord(s) - 97 + key) % 26))
			else:
				message += s
	with open('public.txt', 'w') as f:
		f.write(message)


if __name__ == "__main__":
	main()
