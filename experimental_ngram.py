import utilities

n = 3
case_sensitive = True
# case_sensitive = False

en_basic_corpus = utilities.extract_corpus_experimental(utilities.EN_TRAINING_CORPUS_PATH, case_sensitive)
en_basic_ngram_dict = utilities.extract_experimental_ngram_char(en_basic_corpus, n, case_sensitive)

fr_basic_corpus = utilities.extract_corpus_experimental(utilities.FR_TRAINING_CORPUS_PATH, case_sensitive)
fr_basic_ngram_dict = utilities.extract_experimental_ngram_char(fr_basic_corpus, n, case_sensitive)

vi_basic_corpus = utilities.extract_corpus_experimental(utilities.OT_TRAINING_CORPUS_PATH, case_sensitive)
vi_basic_ngram_dict = utilities.extract_experimental_ngram_char(vi_basic_corpus, n, case_sensitive)

test_lines = utilities.read_test_sentences(utilities.TEST_SENTENCES_PATH, case_sensitive)
test_lines_original = utilities.read_test_sentences_original(utilities.TEST_SENTENCES_PATH)

en_basic_ngram_dict[n] = utilities.cal_ngram_char_prob(en_basic_ngram_dict, n)
fr_basic_ngram_dict[n] = utilities.cal_ngram_char_prob(fr_basic_ngram_dict, n)
vi_basic_ngram_dict[n] = utilities.cal_ngram_char_prob(vi_basic_ngram_dict, n)

for index in range(0, len(test_lines)):
	# EN
	prob_en = utilities.cal_lang_char_prob(en_basic_ngram_dict[n], n, test_lines[index])
	# FR
	prob_fr = utilities.cal_lang_char_prob(fr_basic_ngram_dict[n], n, test_lines[index])
	# VI
	prob_vi = utilities.cal_lang_char_prob(vi_basic_ngram_dict[n], n, test_lines[index])

	if prob_en > prob_fr and prob_en > prob_vi:
		print(test_lines[index] + " (EN)")
	elif prob_fr > prob_en and prob_fr > prob_vi:
		print(test_lines[index] + " (FR)")
	else:
		print(test_lines[index] + " (VI)")