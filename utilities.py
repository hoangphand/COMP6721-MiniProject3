from __future__ import division
import re
import string
import math
from string import ascii_lowercase
import copy

FR_TRAINING_CORPUS_PATH = "training_text/trainFR.txt"
EN_TRAINING_CORPUS_PATH = "training_text/trainEN.txt"
OT_TRAINING_CORPUS_PATH = "training_text/trainOT.txt"
TEST_SENTENCES_PATH = "test_sentences.txt"
DUMP_UNI_LANG_MODEL_EN = "dump_models/unigramEN.txt"
DUMP_UNI_LANG_MODEL_FR = "dump_models/unigramFR.txt"
DUMP_UNI_LANG_MODEL_OT = "dump_models/unigramOT.txt"
DUMP_BI_LANG_MODEL_EN = "dump_models/bigramEN.txt"
DUMP_BI_LANG_MODEL_FR = "dump_models/bigramFR.txt"
DUMP_BI_LANG_MODEL_OT = "dump_models/bigramOT.txt"

def extract_basic_corpus(corpus_path, is_with_space = True):
	with open(corpus_path, "r") as input_file:
		original_content = input_file.read()

	corpus = original_content.lower()

	if is_with_space is False:
		corpus = corpus.replace(" ", "").replace("\n", "").replace("\r", "")

	for punctuation in string.punctuation:
		corpus = corpus.replace(punctuation, "")	

	return corpus

def extract_ngram_char(corpus, n):
	ngram = [{}]
	ngram_1 = {"total_count": 0}
	total_count_1 = 0

	for char in ascii_lowercase:
		ngram_1[char] = {"total_count": 0}

	for i in range(0, len(corpus)):
		element = corpus[i:i + 1]
		if element.isalpha():
			ngram_1["total_count"] += 1
			ngram_1[element]["total_count"] += 1

	ngram.append(ngram_1)

	if n > 1:
		i = 2
		while i <= n:
			ngram_n = {"total_count": 0}

			for key in ngram[i - 1]:
				if key != "total_count":
					for char in ascii_lowercase:
						ngram_n[key + char] = {"total_count": 0}

			for j in range(0, len(corpus)):
				element = corpus[j:j + i]
				if element.isalpha() and len(element) == i:
					ngram_n["total_count"] += 1
					ngram_n[element]["total_count"] += 1

			ngram.append(ngram_n)
			i = i + 1
	
	return ngram

def cal_ngram_char_prob(ngram, n, delta = 0.5):
	ngram_n = copy.deepcopy(ngram[n])
	# count for non-zero total_count keys
	size_ngram = 0
	for key in ngram_n:
		if key != "total_count" and ngram_n[key]["total_count"] != 0:
			size_ngram += 1

	if n == 1:
		for key in ngram_n:
			if key != "total_count":
				ngram_n[key]["total_count"] = (ngram_n[key]["total_count"] + delta) / (ngram_n["total_count"] + delta * size_ngram)
	else:
		ngram_prev = copy.deepcopy(ngram[n - 1])

		for key in ngram_n:
			if key != "total_count":
				prev_key = key[0:len(key) - 1]
				total_count = ngram_prev[prev_key]["total_count"]
				ngram_n[key]["total_count"] = (ngram_n[key]["total_count"] + delta) / (total_count + delta * size_ngram)

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

def read_test_sentences(path):
	lines = []
	processed_lines = []

	with open(path, "r") as input_file:
		lines = input_file.readlines()

	for line in lines:
		line = line.rstrip()
		line = line.lower()
		for punctuation in string.punctuation:
			line = line.replace(punctuation, "")

		line = line.replace(" ", "")

		processed_lines.append(line)

	return processed_lines

def cal_lang_char_prob(ngram, n, test):
	prob = 0

	for i in range(0, len(test)):
		element = test[i:i + n]
		if len(element) == n:
			prob += math.log(ngram[element]["total_count"], 10)

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
