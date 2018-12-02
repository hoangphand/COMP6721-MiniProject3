from __future__ import division
import string
import math
import utilities

n = 1
case_sensitive = True
case_sensitive = False
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

for line in test_lines:
	prob_en = cal_lang_prob(en_word_count, line, delta)
	prob_fr = cal_lang_prob(fr_word_count, line, delta)	
	prob_vi = cal_lang_prob(vi_word_count, line, delta)

# 	prob_en = 0
# 	prob_fr = 0
# 	prob_vi = 0

# 	line = line.lower()
# 	for punctuation in string.punctuation:
# 		line = line.replace(punctuation, " ")
# 	# no_distinct_words = len(dict_words)

# 	words = line.split()
# 	for index in range(0, len(words)):
# 		if words[index] not in en_word_count:
# 			prob_word_en = (delta) / (en_total_words + len(en_word_count) * delta)
# 		else:
# 			prob_word_en = (en_word_count[words[index]] + delta) / (en_total_words + len(en_word_count) * delta)

# 		if words[index] not in fr_word_count:
# 			prob_word_fr = (delta) / (fr_total_words + len(fr_word_count) * delta)
# 		else:
# 			prob_word_fr = (fr_word_count[words[index]] + delta) / (fr_total_words + len(fr_word_count) * delta)

# 		if words[index] not in vi_word_count:
# 			prob_word_vi = (delta) / (vi_total_words + len(vi_word_count) * delta)
# 		else:
# 			prob_word_vi = (vi_word_count[words[index]] + delta) / (vi_total_words + len(vi_word_count) * delta)

# 		prob_en += math.log(prob_word_en, 10)
# 		prob_fr += math.log(prob_word_fr, 10)
# 		prob_vi += math.log(prob_word_vi, 10)
# 		# print(words[index])
# 		# print("- in EN: " + str(prob_word_en) + ", prob so far: " + str(prob_en))
# 		# print("- in FR: " + str(prob_word_fr) + ", prob so far: " + str(prob_fr))
# 		# print("- in VI: " + str(prob_word_vi) + ", prob so far: " + str(prob_vi))

	if prob_en > prob_fr and prob_en > prob_vi:
		print(line + " (EN)")
	elif prob_fr > prob_en and prob_fr > prob_vi:
		print(line + " (FR)")
	else:
		print(line + " (VI)")