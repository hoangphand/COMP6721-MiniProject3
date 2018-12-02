# -*- coding: utf-8 -*-
import re
import string

INTAB = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđẠẢÃÀÁÂẬẦẤẨẪĂẮẰẶẲẴÓÒỌÕỎÔỘỔỖỒỐƠỜỚỢỞỠÉÈẺẸẼÊẾỀỆỂỄÚÙỤỦŨƯỰỮỬỪỨÍÌỊỈĨÝỲỶỴỸĐ"
INTAB = [ch.encode('utf8') for ch in unicode(INTAB, 'utf8')]


OUTTAB = "a" * 17 + "o" * 17 + "e" * 11 + "u" * 11 + "i" * 5 + "y" * 5 + "d" + \
         "A" * 17 + "O" * 17 + "E" * 11 + "U" * 11 + "I" * 5 + "Y" * 5 + "D"

r = re.compile("|".join(INTAB))
replaces_dict = dict(zip(INTAB, OUTTAB))

def no_accent_vietnamese(utf8_str):
    return r.sub(lambda m: replaces_dict[m.group(0)], utf8_str)

with open("vi_10k.txt", "r") as input_file:
	lines = input_file.readlines()
	with open("vi10k.txt", "w") as output_file:
		for line in lines:
			new_line = no_accent_vietnamese(line.split("\t")[1])
			for punctuation in string.punctuation:
				new_line = new_line.replace(punctuation, " ")
			sentence = ''.join(c for c in new_line if c.isalpha() or c == " ")
			words = sentence.split()
			for word in words:
				output_file.write(word + " ")
			output_file.write("\n")