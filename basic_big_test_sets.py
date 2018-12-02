from __future__ import division
import utilities

n = 5
print("N: " + str(n))

en_basic_corpus = utilities.extract_basic_corpus(utilities.EN_TRAINING_CORPUS_PATH)
en_basic_ngram_count = utilities.extract_basic_ngram_char(en_basic_corpus, n)

fr_basic_corpus = utilities.extract_basic_corpus(utilities.FR_TRAINING_CORPUS_PATH)
fr_basic_ngram_count = utilities.extract_basic_ngram_char(fr_basic_corpus, n)

vi_basic_corpus = utilities.extract_basic_corpus(utilities.OT_TRAINING_CORPUS_PATH)
vi_basic_ngram_count = utilities.extract_basic_ngram_char(vi_basic_corpus, n)


en_test_lines = utilities.read_test_sentences_basic(utilities.EN_BIG_TEST_SENTENCES_PATH)
fr_test_lines = utilities.read_test_sentences_basic(utilities.FR_BIG_TEST_SENTENCES_PATH)
vi_test_lines = utilities.read_test_sentences_basic(utilities.VI_BIG_TEST_SENTENCES_PATH)

en_basic_ngram_prob = utilities.cal_ngram_char_prob(en_basic_ngram_count, n)
fr_basic_ngram_prob = utilities.cal_ngram_char_prob(fr_basic_ngram_count, n)
vi_basic_ngram_prob = utilities.cal_ngram_char_prob(vi_basic_ngram_count, n)

en_count = 0
en_fr_count = 0
en_vi_count = 0
for index in range(0, len(en_test_lines)):
	# EN
	prob_en = utilities.cal_lang_char_prob(en_basic_ngram_prob, en_basic_ngram_count, n, en_test_lines[index])
	# FR
	prob_fr = utilities.cal_lang_char_prob(fr_basic_ngram_prob, fr_basic_ngram_count, n, en_test_lines[index])
	# VI
	prob_vi = utilities.cal_lang_char_prob(vi_basic_ngram_prob, vi_basic_ngram_count, n, en_test_lines[index])

	if prob_en > prob_fr and prob_en > prob_vi:
		en_count += 1
	elif prob_fr > prob_en and prob_fr > prob_vi:
		en_fr_count += 1
	else:
		en_vi_count += 1

print("EN: " + str(en_count / 100))
print("EN_FR: " + str(en_fr_count))
print("EN_VI: " + str(en_vi_count))

fr_count = 0
fr_en_count = 0
fr_vi_count = 0
for index in range(0, len(en_test_lines)):
	# EN
	prob_en = utilities.cal_lang_char_prob(en_basic_ngram_prob, en_basic_ngram_count, n, fr_test_lines[index])
	# FR
	prob_fr = utilities.cal_lang_char_prob(fr_basic_ngram_prob, fr_basic_ngram_count, n, fr_test_lines[index])
	# VI
	prob_vi = utilities.cal_lang_char_prob(vi_basic_ngram_prob, vi_basic_ngram_count, n, fr_test_lines[index])

	if prob_en > prob_fr and prob_en > prob_vi:
		fr_en_count += 1
	elif prob_fr > prob_en and prob_fr > prob_vi:
		fr_count += 1
	else:
		fr_vi_count += 1

print("FR: " + str(fr_count / 100))
print("FR_EN: " + str(fr_en_count))
print("FR_VI: " + str(fr_vi_count))

vi_count = 0
vi_en_count = 0
vi_fr_count = 0
for index in range(0, len(en_test_lines)):
	# EN
	prob_en = utilities.cal_lang_char_prob(en_basic_ngram_prob, en_basic_ngram_count, n, vi_test_lines[index])
	# FR
	prob_fr = utilities.cal_lang_char_prob(fr_basic_ngram_prob, fr_basic_ngram_count, n, vi_test_lines[index])
	# VI
	prob_vi = utilities.cal_lang_char_prob(vi_basic_ngram_prob, vi_basic_ngram_count, n, vi_test_lines[index])

	if prob_en > prob_fr and prob_en > prob_vi:
		vi_en_count += 1
	elif prob_fr > prob_en and prob_fr > prob_vi:
		vi_fr_count += 1
	else:
		vi_count += 1

print("VI: " + str(vi_count / 100))
print("VI_FR: " + str(vi_fr_count))
print("VI_EN: " + str(vi_en_count))