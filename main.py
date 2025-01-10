
def main():
	import string
	with open("/home/ironspud/workspace/github.com/Zach-H-Alexander/bookbot/books/frankenstein.txt") as f:
		file_contents = f.read().lower()
		
		words = file_contents.split()
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
	def sort_letters():
		for letter in letter_count:
			letter_list.append({"LETTER": letter, "COUNT": letter_count[letter]})
	sort_letters()
	def sort_on(dict):
		return dict["COUNT"]
	letter_list.sort(reverse=True, key=sort_on)

	def print_report():
		print("--Begin Report--")
		print(f"{word_count} in doc")
		for letter_dict in letter_list:
			character =  letter_dict['LETTER']
			times = letter_dict['COUNT']
			print(f"The {character} appears {times} times!")
		print("--End Report--")

	print_report()

main()
