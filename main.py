def sort_on(dict):
        return dict["COUNT"]
        letter_list.sort(reverse=True, key=sort_on)

def main():
	import string
	path = input("Enter the file location of your book: ")

	#Open file, process and lowercase all of it.
	with open(path) as f:
		file_contents = f.read().lower()
		words = file_contents.split()

	# Count Letters
	word_count = len(words)
	letter_count = {}
	letter_list = []
	for word in words: 
		for letter in word:
			if letter.isalpha():
				if letter in letter_count:
					letter_count[letter] += 1
				else:
					letter_count[letter] = 1

	# Letter counts to List of Dictionaries
	for letter in letter_count:
		letter_list.append({"LETTER": letter, "COUNT": letter_count[letter]})

	
	print(f"--Begin Report for {path}--")
	print(f"There are {word_count} words in this book!")
	for letter_dict in letter_list:
		character =  letter_dict['LETTER']
		times = letter_dict['COUNT']
		print(f"The {character} character was found {times} times!")
	print("--End Report--")

main ()


