import utilities

n = 1
with_space = False
# with_space = True

en_basic_corpus = utilities.extract_basic_corpus(utilities.EN_TRAINING_CORPUS_PATH, with_space)
en_basic_ngram_dict = utilities.extract_ngram_char(en_basic_corpus, n)

fr_basic_corpus = utilities.extract_basic_corpus(utilities.FR_TRAINING_CORPUS_PATH, with_space)
fr_basic_ngram_dict = utilities.extract_ngram_char(fr_basic_corpus, n)

# print(en_basic_bigram_dict[n])
# print(utilities.cal_ngram_char_prob(en_basic_bigram_dict, n))
# print(en_basic_corpus)

test_lines = utilities.read_test_sentences(utilities.TEST_SENTENCES_PATH)

en_basic_ngram_dict[n] = utilities.cal_ngram_char_prob(en_basic_ngram_dict, n)
fr_basic_ngram_dict[n] = utilities.cal_ngram_char_prob(fr_basic_ngram_dict, n)

for line in test_lines:
	# EN
	prob_en = utilities.cal_lang_char_prob(en_basic_ngram_dict[n], n, line)
	# FR
	prob_fr = utilities.cal_lang_char_prob(fr_basic_ngram_dict[n], n, line)

	if prob_en > prob_fr:
		print(line + " (EN)")
	else:
		print(line + " (FR)")

utilities.dump_models(en_basic_ngram_dict, fr_basic_ngram_dict, None, n)
