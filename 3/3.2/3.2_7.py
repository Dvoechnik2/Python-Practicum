def main():
	alf = {
		'A': '.-', 'B': '-...', 'C': '-.-.',
		'D': '-..', 'E': '.', 'F': '..-.',
		'G': '--.', 'H': '....', 'I': '..',
		'J': '.---', 'K': '-.-', 'L': '.-..',
		'M': '--', 'N': '-.', 'O': '---',
		'P': '.--.', 'Q': '--.-', 'R': '.-.',
		'S': '...', 'T': '-', 'U': '..-',
		'V': '...-', 'W': '.--', 'X': '-..-',
		'Y': '-.--', 'Z': '--..',
		'0': '-----', '1': '.----', '2': '..---',
		'3': '...--', '4': '....-', '5': '.....',
		'6': '-....', '7': '--...', '8': '---..',
		'9': '----.'
	}

	line = input()
	for x in line.split():
		if x != ' ':
			for y in x.upper():
				print(alf[y], end=' ')
		print()

if __name__ == "__main__":
	main()
