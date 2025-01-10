
def main():
	with open("/home/ironspud/workspace/github.com/Zach-H-Alexander/bookbot/books/frankenstein.txt") as f:
		file_contents = f.read().lower()
		
		words = file_contents.split()
		word_count = len(words)
		letter_count = {}
		for word in words:
			for letter in word:
				if letter in letter_count:
					letter_count[letter] += 1
				else:
					letter_count[letter] = 1
		print(letter_count)	
	print(word_count)
main()
