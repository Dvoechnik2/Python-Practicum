def main():
	translit_table = {
		'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
		'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e',
		'Ё': 'E', 'ё': 'e', 'Ж': 'Zh', 'ж': 'zh', 'З': 'Z', 'з': 'z',
		'И': 'I', 'и': 'i', 'Й': 'I', 'й': 'i', 'К': 'K', 'к': 'k',
		'Л': 'L', 'л': 'l', 'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n',
		'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
		'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u',
		'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh', 'Ц': 'Tc', 'ц': 'tc',
		'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch',
		'Ы': 'Y', 'ы': 'y', 'Э': 'E', 'э': 'e', 'Ю': 'Iu', 'ю': 'iu',
		'Я': 'Ia', 'я': 'ia', 'Ъ': '', 'ъ': '', 'Ь': '', 'ь': ''
	}
	with open('cyrillic.txt', 'r', encoding='utf-8') as infile:
		text = infile.read()
		trans = []
		for x in text:
			trans.append(translit_table.get(x, x))
		trans = ''.join(trans)
		with open('transliteration.txt', 'w', encoding='utf-8') as outfile:
			outfile.write(trans)


if __name__ == "__main__":
	main()
