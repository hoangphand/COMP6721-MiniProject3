import utilities

n = 1

en_basic_corpus = utilities.extract_basic_corpus(utilities.EN_TRAINING_CORPUS_1_PATH)
en_basic_corpus += " " + utilities.extract_basic_corpus(utilities.EN_TRAINING_CORPUS_2_PATH)
en_basic_unigram_dict = utilities.extract_basic_ngram(en_basic_corpus, n)

fr_basic_corpus = utilities.extract_basic_corpus(utilities.FR_TRAINING_CORPUS_1_PATH)
fr_basic_corpus += " " + utilities.extract_basic_corpus(utilities.FR_TRAINING_CORPUS_2_PATH)
fr_basic_unigram_dict = utilities.extract_basic_ngram(fr_basic_corpus, n)

# print(basic_unigram_dict)

test_lines = utilities.read_test_sentences(utilities.TEST_SENTENCES_PATH)

for line in test_lines:
	# EN
	prob_en = utilities.cal_ngram_prob(en_basic_unigram_dict, n, line)
	# print("en prob: " + str(prob_en))
	# FR
	prob_fr = utilities.cal_ngram_prob(fr_basic_unigram_dict, n, line)
	# print("fr prob: " + str(prob_fr))

	if prob_en > prob_fr:
		print(line + " (EN)")
	else:
		print(line + " (FR)")
	# print(len(line))