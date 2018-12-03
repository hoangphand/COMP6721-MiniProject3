from __future__ import division
import string
import math
import utilities

n = 1
case_sensitive = True
# case_sensitive = False
delta = 0.5

def cal_lang_prob(word_count, test, delta = 0.5):
	prob = 0
	list_words = test.split()
	no_distinct_words = len(word_count) - 1
	total_words = word_count["total_count"]

	for word in list_words:
		if word not in word_count:
			prob += math.log((delta) / (total_words + no_distinct_words * delta) , 10)
		else:
			prob += math.log((word_count[word]["total_count"] + delta) / (total_words + no_distinct_words * delta) , 10)

	return prob

en_basic_corpus = utilities.extract_corpus_experimental(utilities.EN_TRAINING_CORPUS_PATH, case_sensitive)
en_word_count = utilities.extract_word_count_from_corpus(en_basic_corpus)

fr_basic_corpus = utilities.extract_corpus_experimental(utilities.FR_TRAINING_CORPUS_PATH, case_sensitive)
fr_word_count = utilities.extract_word_count_from_corpus(fr_basic_corpus)

vi_basic_corpus = utilities.extract_corpus_experimental(utilities.OT_TRAINING_CORPUS_PATH, case_sensitive)
vi_word_count = utilities.extract_word_count_from_corpus(vi_basic_corpus)

test_lines = utilities.read_test_sentences(utilities.TEST_SENTENCES_PATH, case_sensitive)

en_test_lines = utilities.read_test_sentences(utilities.EN_BIG_TEST_SENTENCES_PATH, case_sensitive)
fr_test_lines = utilities.read_test_sentences(utilities.FR_BIG_TEST_SENTENCES_PATH, case_sensitive)
vi_test_lines = utilities.read_test_sentences(utilities.VI_BIG_TEST_SENTENCES_PATH, case_sensitive)

delta = 0.1

en_count = 0
en_fr_count = 0
en_vi_count = 0

for line in en_test_lines:
	prob_en = cal_lang_prob(en_word_count, line, delta)
	prob_fr = cal_lang_prob(fr_word_count, line, delta)	
	prob_vi = cal_lang_prob(vi_word_count, line, delta)

	length = len(line.split())

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
for line in fr_test_lines:
	prob_en = cal_lang_prob(en_word_count, line, delta)
	prob_fr = cal_lang_prob(fr_word_count, line, delta)	
	prob_vi = cal_lang_prob(vi_word_count, line, delta)

	length = len(line.split())

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
for line in vi_test_lines:
	prob_en = cal_lang_prob(en_word_count, line, delta)
	prob_fr = cal_lang_prob(fr_word_count, line, delta)	
	prob_vi = cal_lang_prob(vi_word_count, line, delta)

	length = len(line.split())

	if prob_en > prob_fr and prob_en > prob_vi:
		vi_en_count += 1
	elif prob_fr > prob_en and prob_fr > prob_vi:
		vi_fr_count += 1
	else:
		vi_count += 1

print("VI: " + str(vi_count / 100))
print("VI_FR: " + str(vi_fr_count))
print("VI_EN: " + str(vi_en_count))