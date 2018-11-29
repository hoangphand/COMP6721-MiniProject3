import string

FR_ORIGINAL_CORPUS_PATH = "original_training_text/trainFR.txt"
EN_ORIGINAL_CORPUS_PATH = "original_training_text/trainEN.txt"
OT_ORIGINAL_CORPUS_PATH = "original_training_text/trainOT.txt"

FR_CORPUS_PATH = "training_text/trainFR.txt"
EN_CORPUS_PATH = "training_text/trainEN.txt"
OT_CORPUS_PATH = "training_text/trainOT.txt"

with open(EN_ORIGINAL_CORPUS_PATH, "r") as input_file:
	en_original_content = input_file.read()

with open(FR_ORIGINAL_CORPUS_PATH, "r") as input_file:
	fr_original_content = input_file.read()

with open(OT_ORIGINAL_CORPUS_PATH, "r") as input_file:
	vi_original_content = input_file.read()

en_corpus = en_original_content
fr_corpus = fr_original_content
vi_corpus = vi_original_content

# LOWER CASE
# corpus = original_content.lower()
# corpus = corpus.replace("\n", " ")

for punctuation in string.punctuation:
	en_corpus = en_corpus.replace(punctuation, " ")
	fr_corpus = fr_corpus.replace(punctuation, " ")
	vi_corpus = vi_corpus.replace(punctuation, " ")

en_list_of_words = en_corpus.split()
fr_list_of_words = fr_corpus.split()
vi_list_of_words = vi_corpus.split()

with open(EN_CORPUS_PATH, "w") as output_file:
	for word in en_list_of_words:
		word = ''.join(c for c in word if not c.isdigit())
		if word.isalpha():
			output_file.write(word + " ")

with open(FR_CORPUS_PATH, "w") as output_file:
	for word in fr_list_of_words:
		word = ''.join(c for c in word if not c.isdigit())
		if word.isalpha():
			output_file.write(word + " ")

with open(OT_CORPUS_PATH, "w") as output_file:
	for word in vi_list_of_words:
		word = ''.join(c for c in word if not c.isdigit())
		if word.isalpha():
			output_file.write(word + " ")