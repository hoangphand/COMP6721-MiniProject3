import utilities

n = 2
with_space = False
# with_space = True

en_basic_corpus = utilities.extract_basic_corpus(utilities.EN_TRAINING_CORPUS_PATH, with_space)
en_basic_ngram_dict = utilities.extract_ngram_char(en_basic_corpus, n)

fr_basic_corpus = utilities.extract_basic_corpus(utilities.FR_TRAINING_CORPUS_PATH, with_space)
fr_basic_ngram_dict = utilities.extract_ngram_char(fr_basic_corpus, n)

vi_basic_corpus = utilities.extract_basic_corpus(utilities.OT_TRAINING_CORPUS_PATH, with_space)
vi_basic_ngram_dict = utilities.extract_ngram_char(vi_basic_corpus, n)

test_lines = utilities.read_test_sentences(utilities.TEST_SENTENCES_PATH)

en_basic_ngram_dict[n] = utilities.cal_ngram_char_prob(en_basic_ngram_dict, n)
fr_basic_ngram_dict[n] = utilities.cal_ngram_char_prob(fr_basic_ngram_dict, n)
vi_basic_ngram_dict[n] = utilities.cal_ngram_char_prob(vi_basic_ngram_dict, n)

for line in test_lines:
	# EN
	prob_en = utilities.cal_lang_char_prob(en_basic_ngram_dict[n], n, line)
	# FR
	prob_fr = utilities.cal_lang_char_prob(fr_basic_ngram_dict[n], n, line)
	# VI
	prob_vi = utilities.cal_lang_char_prob(vi_basic_ngram_dict[n], n, line)

	if prob_en > prob_fr and prob_en > prob_vi:
		print(line + " (EN)")
	elif prob_fr > prob_en and prob_fr > prob_vi:
		print(line + " (FR)")
	else:
		print(line + " (VI)")

if n == 1 or n == 2:
	utilities.dump_models(en_basic_ngram_dict, fr_basic_ngram_dict, None, n)
