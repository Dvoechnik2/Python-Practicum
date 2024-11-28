def main():
	# Вводим имена файлов
	input_file = input().strip()
	output_file = input().strip()
	with open(input_file, 'r', encoding='utf-8') as infile:
		lines = infile.readlines()
	cleaned_lines = []
	for line in lines:
		line = line.strip()
		line = line.replace('\t', '')
		line = ' '.join(line.split())
		if line:
			cleaned_lines.append(line)
	final_text = []
	for i, line in enumerate(cleaned_lines):
		if line or (i > 0 and cleaned_lines[i - 1]):
			final_text.append(line)
	with open(output_file, 'w', encoding='utf-8') as outfile:
		outfile.write('\n'.join(final_text))


if __name__ == "__main__":
	main()