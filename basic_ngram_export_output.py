import utilities
import math

n = 2
with_space = False
# with_space = True

en_basic_corpus = utilities.extract_basic_corpus(utilities.EN_TRAINING_CORPUS_PATH, with_space)
en_basic_ngram_dict = utilities.extract_basic_ngram_char(en_basic_corpus, n)

fr_basic_corpus = utilities.extract_basic_corpus(utilities.FR_TRAINING_CORPUS_PATH, with_space)
fr_basic_ngram_dict = utilities.extract_basic_ngram_char(fr_basic_corpus, n)

vi_basic_corpus = utilities.extract_basic_corpus(utilities.OT_TRAINING_CORPUS_PATH, with_space)
vi_basic_ngram_dict = utilities.extract_basic_ngram_char(vi_basic_corpus, n)

test_lines = utilities.read_test_sentences(utilities.TEST_SENTENCES_PATH)
test_lines_original = utilities.read_test_sentences_original(utilities.TEST_SENTENCES_PATH)

en_basic_ngram_dict_uni = utilities.cal_ngram_char_prob(en_basic_ngram_dict, 1)
fr_basic_ngram_dict_uni = utilities.cal_ngram_char_prob(fr_basic_ngram_dict, 1)
vi_basic_ngram_dict_uni = utilities.cal_ngram_char_prob(vi_basic_ngram_dict, 1)

en_basic_ngram_dict_bi = utilities.cal_ngram_char_prob(en_basic_ngram_dict, 2)
fr_basic_ngram_dict_bi = utilities.cal_ngram_char_prob(fr_basic_ngram_dict, 2)
vi_basic_ngram_dict_bi = utilities.cal_ngram_char_prob(vi_basic_ngram_dict, 2)

for index in range(0, len(test_lines)):
	with open("output_files/out" + str(index + 1) + ".txt", "w") as output_file:
		output_file.write(test_lines_original[index] + "\n")
		prob_en = 0
		prob_fr = 0
		prob_vi = 0
		# UNIGRAM
		output_file.write("UNIGRAM MODEL: \n\n")
		for c in test_lines[index]:
			prob_fr += math.log(fr_basic_ngram_dict_uni[c]["total_count"], 10)
			prob_en += math.log(en_basic_ngram_dict_uni[c]["total_count"], 10)
			prob_vi += math.log(vi_basic_ngram_dict_uni[c]["total_count"], 10)
			output_file.write("UNIGRAM: " + c + "\n")
			output_file.write("FRENCH: P(" + c + ") = " + str(fr_basic_ngram_dict_uni[c]["total_count"]))
			output_file.write("  log prob of sentence so far: " + str(prob_fr) + "\n")
			output_file.write("ENGLISH: P(" + c + ") = " + str(en_basic_ngram_dict_uni[c]["total_count"]))
			output_file.write("  log prob of sentence so far: " + str(prob_en) + "\n")
			output_file.write("OTHER: P(" + c + ") = " + str(vi_basic_ngram_dict_uni[c]["total_count"]))
			output_file.write("  log prob of sentence so far: " + str(prob_vi) + "\n\n")

		output_file.write("According to the unigram model, the sentence is in ")
		if prob_en > prob_fr and prob_en > prob_vi:
			output_file.write("English\n\n")
		elif prob_fr > prob_en and prob_fr > prob_vi:
			output_file.write("French\n\n")
		else:
			output_file.write("Other\n\n")

		# BIGRAM
		output_file.write("----------------\n")
		prob_en = 0
		prob_fr = 0
		prob_vi = 0
		output_file.write("BIGRAM MODEL: \n\n")
		for i in range(0, len(test_lines[index])):
			key = test_lines[index][i:i + 2]
			if len(key) == 2:
				succ = key[0:1]
				pred = key[1:2]
				prob_fr += math.log(fr_basic_ngram_dict_bi[key]["total_count"], 10)
				prob_en += math.log(en_basic_ngram_dict_bi[key]["total_count"], 10)
				prob_vi += math.log(vi_basic_ngram_dict_bi[key]["total_count"], 10)
				output_file.write("BIGRAM: " + key + "\n")
				output_file.write("FRENCH: P(" + succ + "|" + pred + ") = " + str(fr_basic_ngram_dict_bi[key]["total_count"]))
				output_file.write("  log prob of sentence so far: " + str(prob_fr) + "\n")
				output_file.write("ENGLISH: P(" + succ + "|" + pred + ") = " + str(en_basic_ngram_dict_bi[key]["total_count"]))
				output_file.write("  log prob of sentence so far: " + str(prob_en) + "\n")
				output_file.write("OTHER: P(" + succ + "|" + pred + ") = " + str(vi_basic_ngram_dict_bi[key]["total_count"]))
				output_file.write("  log prob of sentence so far: " + str(prob_vi) + "\n\n")

		output_file.write("According to the unigram model, the sentence is in ")
		if prob_en > prob_fr and prob_en > prob_vi:
			output_file.write("English\n\n")
		elif prob_fr > prob_en and prob_fr > prob_vi:
			output_file.write("French\n\n")
		else:
			output_file.write("Other\n\n")