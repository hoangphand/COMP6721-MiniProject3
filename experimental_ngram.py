import utilities

n = 2
case_sensitive = True
# case_sensitive = False

en_corpus = utilities.extract_corpus_experimental(utilities.EN_TRAINING_CORPUS_PATH, case_sensitive)
en_ngram_count = utilities.extract_experimental_ngram_char(en_corpus, n, case_sensitive)

fr_corpus = utilities.extract_corpus_experimental(utilities.FR_TRAINING_CORPUS_PATH, case_sensitive)
fr_ngram_count = utilities.extract_experimental_ngram_char(fr_corpus, n, case_sensitive)

vi_corpus = utilities.extract_corpus_experimental(utilities.OT_TRAINING_CORPUS_PATH, case_sensitive)
vi_ngram_count = utilities.extract_experimental_ngram_char(vi_corpus, n, case_sensitive)

test_lines = utilities.read_test_sentences(utilities.TEST_SENTENCES_PATH, case_sensitive)
test_lines_original = utilities.read_test_sentences_original(utilities.TEST_SENTENCES_PATH)

en_ngram_prob_n = utilities.cal_ngram_char_prob(en_ngram_count, n)
fr_ngram_prob_n = utilities.cal_ngram_char_prob(fr_ngram_count, n)
vi_ngram_prob_n = utilities.cal_ngram_char_prob(vi_ngram_count, n)

for index in range(0, len(test_lines)):
	# EN
	prob_en = utilities.cal_lang_char_prob(en_ngram_prob_n, en_ngram_count, n, test_lines[index])
	# FR
	prob_fr = utilities.cal_lang_char_prob(fr_ngram_prob_n, fr_ngram_count, n, test_lines[index])
	# VI
	prob_vi = utilities.cal_lang_char_prob(vi_ngram_prob_n, vi_ngram_count, n, test_lines[index])

	if prob_en > prob_fr and prob_en > prob_vi:
		print(test_lines[index] + " (EN)")
	elif prob_fr > prob_en and prob_fr > prob_vi:
		print(test_lines[index] + " (FR)")
	else:
		print(test_lines[index] + " (VI)")