from __future__ import division
import utilities
import math

n = 2
delta = 0.5

en_basic_corpus = utilities.extract_basic_corpus(utilities.EN_TRAINING_CORPUS_PATH)
en_basic_ngram_count = utilities.extract_basic_ngram_char(en_basic_corpus, n)

fr_basic_corpus = utilities.extract_basic_corpus(utilities.FR_TRAINING_CORPUS_PATH)
fr_basic_ngram_count = utilities.extract_basic_ngram_char(fr_basic_corpus, n)

vi_basic_corpus = utilities.extract_basic_corpus(utilities.OT_TRAINING_CORPUS_PATH)
vi_basic_ngram_count = utilities.extract_basic_ngram_char(vi_basic_corpus, n)

test_lines = utilities.read_test_sentences_strip(utilities.TEST_SENTENCES_PATH)
test_lines_original = utilities.read_test_sentences_original(utilities.TEST_SENTENCES_PATH)

en_basic_ngram_prob_uni = utilities.cal_ngram_char_prob(en_basic_ngram_count, 1)
fr_basic_ngram_prob_uni = utilities.cal_ngram_char_prob(fr_basic_ngram_count, 1)
vi_basic_ngram_prob_uni = utilities.cal_ngram_char_prob(vi_basic_ngram_count, 1)

en_basic_ngram_prob_bi = utilities.cal_ngram_char_prob(en_basic_ngram_count, 2)
fr_basic_ngram_prob_bi = utilities.cal_ngram_char_prob(fr_basic_ngram_count, 2)
vi_basic_ngram_prob_bi = utilities.cal_ngram_char_prob(vi_basic_ngram_count, 2)

for index in range(0, len(test_lines)):
	with open("output_files/out" + str(index + 1) + ".txt", "w") as output_file:
		output_file.write(test_lines_original[index] + "\n")
		prob_en = 0
		prob_fr = 0
		prob_vi = 0
		v1 = 26
		# UNIGRAM
		output_file.write("UNIGRAM MODEL: \n\n")
		for c in test_lines[index]:
			if c in fr_basic_ngram_prob_uni:
				prob_c_fr = fr_basic_ngram_prob_uni[c]["total_count"]
			else:
				prob_c_fr = delta / (fr_basic_ngram_count[1]["total_count"] + delta * v1)

			prob_fr += math.log(prob_c_fr, 10)

			if c in en_basic_ngram_prob_uni:
				prob_c_en = en_basic_ngram_prob_uni[c]["total_count"]
			else:
				prob_c_en = delta / (en_basic_ngram_count[1]["total_count"] + delta * v1)

			prob_en += math.log(prob_c_en, 10)

			if c in vi_basic_ngram_prob_uni:
				prob_c_vi = vi_basic_ngram_prob_uni[c]["total_count"]
			else:
				prob_c_vi = delta / (vi_basic_ngram_count[1]["total_count"] + delta * v1)

			prob_vi += math.log(prob_c_vi, 10)

			output_file.write("UNIGRAM: " + c + "\n")
			output_file.write("FRENCH: P(" + c + ") = " + str(prob_c_fr))
			output_file.write("  log prob of sentence so far: " + str(prob_fr) + "\n")
			output_file.write("ENGLISH: P(" + c + ") = " + str(prob_c_en))
			output_file.write("  log prob of sentence so far: " + str(prob_en) + "\n")
			output_file.write("OTHER: P(" + c + ") = " + str(prob_c_vi))
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
		v2 = 26 * 26
		output_file.write("BIGRAM MODEL: \n\n")
		for i in range(0, len(test_lines[index])):
			key = test_lines[index][i:i + 2]
			if len(key) == 2:
				pred = key[0:1]
				succ = key[1:2]

				if key in fr_basic_ngram_prob_bi:
					prob_key_fr = fr_basic_ngram_prob_bi[key]["total_count"]
				else:
					if pred in fr_basic_ngram_count[1]:
						prob_key_fr = delta / (fr_basic_ngram_count[1][pred]["total_count"] + delta * v2)
					else:
						prob_key_fr = delta / (delta + delta * v2)

				prob_fr += math.log(prob_key_fr, 10)

				if key in en_basic_ngram_prob_bi:
					prob_key_en = en_basic_ngram_prob_bi[key]["total_count"]
				else:
					if pred in en_basic_ngram_count[1]:
						prob_key_en = delta / (en_basic_ngram_count[1][pred]["total_count"] + delta * v2)
					else:
						prob_key_en = delta / (delta + delta * v2)

				prob_en += math.log(prob_key_en, 10)
				
				if key in vi_basic_ngram_prob_bi:
					prob_key_vi = vi_basic_ngram_prob_bi[key]["total_count"]
				else:
					if pred in vi_basic_ngram_count[1]:
						prob_key_vi = delta / (vi_basic_ngram_count[1][pred]["total_count"] + delta * v2)
					else:
						prob_key_vi = delta / (delta + delta * v2)

				prob_vi += math.log(prob_key_vi, 10)

				output_file.write("BIGRAM: " + key + "\n")
				output_file.write("FRENCH: P(" + succ + "|" + pred + ") = " + str(prob_key_fr))
				output_file.write("  log prob of sentence so far: " + str(prob_fr) + "\n")
				output_file.write("ENGLISH: P(" + succ + "|" + pred + ") = " + str(prob_key_en))
				output_file.write("  log prob of sentence so far: " + str(prob_en) + "\n")
				output_file.write("OTHER: P(" + succ + "|" + pred + ") = " + str(prob_key_vi))
				output_file.write("  log prob of sentence so far: " + str(prob_vi) + "\n\n")

		output_file.write("According to the unigram model, the sentence is in ")
		if prob_en > prob_fr and prob_en > prob_vi:
			output_file.write("English\n\n")
		elif prob_fr > prob_en and prob_fr > prob_vi:
			output_file.write("French\n\n")
		else:
			output_file.write("Other\n\n")