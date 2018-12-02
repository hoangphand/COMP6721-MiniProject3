import re
import string

with open("en_10k.txt", "r") as input_file:
	lines = input_file.readlines()
	with open("en10k.txt", "w") as output_file:
		for line in lines:
			new_line = line.split("\t")[1]
			for punctuation in string.punctuation:
				new_line = new_line.replace(punctuation, " ")
			sentence = ''.join(c for c in new_line if c.isalpha() or c == " ")
			words = sentence.split()
			for word in words:
				output_file.write(word + " ")
			output_file.write("\n")