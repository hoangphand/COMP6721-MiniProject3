import utilities

n = 2

en_basic_corpus = utilities.extract_basic_corpus(utilities.EN_TRAINING_CORPUS_PATH)
en_basic_ngram_dict = utilities.extract_basic_ngram_char(en_basic_corpus, n)

fr_basic_corpus = utilities.extract_basic_corpus(utilities.FR_TRAINING_CORPUS_PATH)
fr_basic_ngram_dict = utilities.extract_basic_ngram_char(fr_basic_corpus, n)

vi_basic_corpus = utilities.extract_basic_corpus(utilities.OT_TRAINING_CORPUS_PATH)
vi_basic_ngram_dict = utilities.extract_basic_ngram_char(vi_basic_corpus, n)

test_lines = utilities.read_test_sentences_strip(utilities.TEST_SENTENCES_PATH)
test_lines_original = utilities.read_test_sentences_original(utilities.TEST_SENTENCES_PATH)

en_basic_ngram_dict[n] = utilities.cal_ngram_char_prob(en_basic_ngram_dict, n)
fr_basic_ngram_dict[n] = utilities.cal_ngram_char_prob(fr_basic_ngram_dict, n)
vi_basic_ngram_dict[n] = utilities.cal_ngram_char_prob(vi_basic_ngram_dict, n)

with open("output.txt", "w") as output_file:
	for index in range(0, len(test_lines)):
		# EN
		prob_en = utilities.cal_lang_char_prob(en_basic_ngram_dict[n], n, test_lines[index])
		# FR
		prob_fr = utilities.cal_lang_char_prob(fr_basic_ngram_dict[n], n, test_lines[index])
		# VI
		prob_vi = utilities.cal_lang_char_prob(vi_basic_ngram_dict[n], n, test_lines[index])

		if prob_en > prob_fr and prob_en > prob_vi:
			output_file.write(test_lines_original[index] + " (EN)\n")
			print(test_lines[index] + " (EN)")
		elif prob_fr > prob_en and prob_fr > prob_vi:
			output_file.write(test_lines_original[index] + " (FR)\n")
			print(test_lines[index] + " (FR)")
		else:
			output_file.write(test_lines_original[index] + " (VI)\n")
			print(test_lines[index] + " (VI)")

if n == 1 or n == 2:
	utilities.dump_models(en_basic_ngram_dict, fr_basic_ngram_dict, vi_basic_ngram_dict, n)

