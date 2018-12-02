from __future__ import division
import re
import string
import math
from string import ascii_lowercase
from string import ascii_uppercase
import copy

FR_TRAINING_CORPUS_PATH = "training_text/trainFR.txt"
EN_TRAINING_CORPUS_PATH = "training_text/trainEN.txt"
OT_TRAINING_CORPUS_PATH = "training_text/trainOT.txt"
TEST_SENTENCES_PATH = "test_sentences.txt"
EN_BIG_TEST_SENTENCES_PATH = "big_test_sets/en10k.txt"
FR_BIG_TEST_SENTENCES_PATH = "big_test_sets/fr10k.txt"
VI_BIG_TEST_SENTENCES_PATH = "big_test_sets/vi10k.txt"
DUMP_UNI_LANG_MODEL_EN = "dump_models/unigramEN.txt"
DUMP_UNI_LANG_MODEL_FR = "dump_models/unigramFR.txt"
DUMP_UNI_LANG_MODEL_OT = "dump_models/unigramOT.txt"
DUMP_BI_LANG_MODEL_EN = "dump_models/bigramEN.txt"
DUMP_BI_LANG_MODEL_FR = "dump_models/bigramFR.txt"
DUMP_BI_LANG_MODEL_OT = "dump_models/bigramOT.txt"
DELTA = 0.5

def extract_basic_corpus(corpus_path):
	with open(corpus_path, "r") as input_file:
		original_content = input_file.read()

	corpus = original_content.lower()

	corpus = corpus.replace(" ", "").replace("\r", "")

	return corpus

def extract_corpus_experimental(corpus_path, case_sensitive = False):
	with open(corpus_path, "r") as input_file:
		corpus = input_file.read()

	if case_sensitive is False:
		corpus = corpus.lower()

	return corpus

def extract_basic_ngram_char(corpus, n):
	if n == 1:
		ngram_1 = {"total_count": 0}
		for char in ascii_lowercase:
			ngram_1[char] = {"total_count": 0}

		for i in range(0, len(corpus)):
			element = corpus[i:i + 1]
			if element.isalpha():
				ngram_1["total_count"] += 1
				ngram_1[element]["total_count"] += 1

		return [{}, ngram_1]
	else:
		ngram_n_1 = {"total_count": 0}
		ngram_n = {"total_count": 0}

		# N - 1
		for i in range(0, len(corpus)):
			element = corpus[i:i + n - 1]
			if len(element) == n - 1:
				ngram_n_1["total_count"] += 1

				if element in ngram_n_1:
					ngram_n_1[element]["total_count"] += 1
				else:
					ngram_n_1[element] = {"total_count": 1}

		# N
		for i in range(0, len(corpus)):
			element = corpus[i:i + n]
			if len(element) == n:
				ngram_n["total_count"] += 1

				if element in ngram_n:
					ngram_n[element]["total_count"] += 1
				else:
					ngram_n[element] = {"total_count": 1}

		ngram = []
		for i in range(0, n - 1):
			ngram.append({})

		ngram.append(ngram_n_1)
		ngram.append(ngram_n)
	
		return ngram

def extract_experimental_ngram_char(corpus, n, case_sensitive = False):
	if n == 1:
		ngram_1 = {"total_count": 0}
		total_count_1 = 0

		for i in range(0, len(corpus)):
			key = corpus[i:i + 1]
			if key in ngram_1:
				ngram_1["total_count"] += 1
				ngram_1[key]["total_count"] += 1
			else:
				ngram_1[key] = {"total_count": 0}

		return [{}, ngram_1]
	else:
		ngram_n_1 = {"total_count": 0}
		ngram_n = {"total_count": 0}

		# N - 1
		for i in range(0, len(corpus)):
			key = corpus[i:i + n - 1]
			if len(key) == n - 1:
				ngram_n_1["total_count"] += 1

				if key in ngram_n_1:
					ngram_n_1[key]["total_count"] += 1
				else:
					ngram_n_1[key] = {"total_count": 1}

		# N
		for i in range(0, len(corpus)):
			key = corpus[i:i + n]
			if len(key) == n:
				ngram_n["total_count"] += 1

				if key in ngram_n:
					ngram_n[key]["total_count"] += 1
				else:
					ngram_n[key] = {"total_count": 1}

		ngram = []
		for i in range(0, n - 1):
			ngram.append({})

		ngram.append(ngram_n_1)
		ngram.append(ngram_n)
	
		return ngram

def cal_ngram_char_prob(ngram, n, delta = DELTA):
	ngram_n = copy.deepcopy(ngram[n])
	size_ngram = math.pow(26, n)

	if n == 1:
		for key in ngram_n:
			if key != "total_count":
				key_count = ngram_n[key]["total_count"]
				ngram_n[key]["total_count"] = (key_count + delta) / (ngram_n["total_count"] + delta * size_ngram)
	else:
		ngram_prev = copy.deepcopy(ngram[n - 1])

		for key in ngram_n:
			if key != "total_count":
				prev_key = key[0:len(key) - 1]
				key_count = ngram_n[key]["total_count"]
				total_count_prev = ngram_prev[prev_key]["total_count"]
				ngram_n[key]["total_count"] = (key_count + delta) / (total_count_prev + delta * size_ngram)

	return ngram_n

def read_test_sentences_original(path):
	lines = []
	stripped_lines = []

	with open(path, "r") as input_file:
		lines = input_file.readlines()

	for line in lines:
		line = line.rstrip()
		stripped_lines.append(line)

	return stripped_lines

def read_test_sentences_basic(path):
	lines = []
	processed_lines = []

	with open(path, "r") as input_file:
		lines = input_file.readlines()

	for line in lines:
		line = line.rstrip()
		line = line.lower()
		line = ''.join(c for c in line if not c.isdigit())

		for punctuation in string.punctuation:
			line = line.replace(punctuation, "")

		line = line.replace(" ", "")

		processed_lines.append(line)

	return processed_lines

def read_test_sentences(path, case_sensitive = False):
	lines = []
	processed_lines = []

	with open(path, "r") as input_file:
		lines = input_file.readlines()

	for line in lines:
		line = line.rstrip()
		if case_sensitive is False:
			line = line.lower()
		line = ''.join(c for c in line if not c.isdigit())

		for punctuation in string.punctuation:
			line = line.replace(punctuation, " ")

		list_words = line.split()

		line = ""
		for word in list_words:
			line += word + " "

		processed_lines.append(line)

	return processed_lines

def cal_lang_char_prob(ngram_prob, ngram_count, n, test, delta = DELTA):
	prob = 0
	size_ngram = math.pow(26, n)

	for i in range(0, len(test)):
		key = test[i:i + n]
		if len(key) == n and key.replace(" ", "").isalpha():
			if key in ngram_prob:
				prob += math.log(ngram_prob[key]["total_count"], 10)
			else:
				prev_key = key[0:len(key) - 1]
				if prev_key in ngram_count:
					smoothing = (delta) / (ngram_count[prev_key]["total_count"] + delta * size_ngram)
				else:
					smoothing = (delta) / (delta + delta * size_ngram)

				prob += math.log(smoothing, 10)

	return prob

def dump_models(ngram_en, ngram_fr, ngram_ot, n):
	if n == 1:
		with open(DUMP_UNI_LANG_MODEL_EN, "w") as output_file:
			for key, value in sorted(ngram_en[1].items()):
				if key != "total_count":
					output_file.write("(" + key + ") = " + str(ngram_en[1][key]["total_count"]))
					output_file.write("\n")
		with open(DUMP_UNI_LANG_MODEL_FR, "w") as output_file:
			for key, value in sorted(ngram_fr[1].items()):
				if key != "total_count":
					output_file.write("(" + key + ") = " + str(ngram_fr[1][key]["total_count"]))
					output_file.write("\n")
		if ngram_ot is not None:
			with open(DUMP_UNI_LANG_MODEL_OT, "w") as output_file:
				for key, value in sorted(ngram_ot[1].items()):
					if key != "total_count":
						output_file.write("(" + key + ") = " + str(ngram_ot[1][key]["total_count"]))
						output_file.write("\n")
	else:
		with open(DUMP_BI_LANG_MODEL_EN, "w") as output_file:
			for key, value in sorted(ngram_en[n].items()):
				if key != "total_count":
					succ = key[0:1]
					pred = key[1:2]
					output_file.write("(" + succ + "|" + pred + ") = " + str(ngram_en[n][key]["total_count"]))
					output_file.write("\n")
		with open(DUMP_BI_LANG_MODEL_FR, "w") as output_file:
			for key, value in sorted(ngram_fr[n].items()):
				if key != "total_count":
					succ = key[0:1]
					pred = key[1:2]
					output_file.write("(" + succ + "|" + pred + ") = " + str(ngram_fr[n][key]["total_count"]))
					output_file.write("\n")
		if ngram_ot is not None:
			with open(DUMP_BI_LANG_MODEL_OT, "w") as output_file:
				for key, value in sorted(ngram_ot[n].items()):
					if key != "total_count":
						succ = key[0:1]
						pred = key[1:2]
						output_file.write("(" + succ + "|" + pred + ") = " + str(ngram_ot[n][key]["total_count"]))
						output_file.write("\n")

def extract_word_count_from_corpus(corpus):
	list_words = corpus.split()
	word_count = {"total_count": len(list_words)}

	for word in list_words:
		if word not in word_count:
			word_count[word] = {"total_count": 1}
		else:
			word_count[word]["total_count"] += 1

	return word_count