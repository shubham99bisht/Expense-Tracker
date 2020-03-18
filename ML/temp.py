# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

# regex = r"(\s|,|-)(20(0|1|2)\d)"
regex = r"\b(0?[1-9]|[12][0-9]|3[01])\b(\s|,|-|\/)\b(0?[1-9]|[12][0-9]|3[01])\b(\s|,|-|\/)\b(20(0|1|2)\d)\b"
date2 = r"\b((Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)|((0|1|2)\d))\b(\s|,|-|\/|.)(\s|,|-|\/|.)?\b((20(0|1|2)\d)|((0|1|2)\d))\b"

test_str = (" dateEntries = '''\n"
	" Total 2025.19\n\n"
	" 04-20-2009;\n"
	" 04/20/09;\n"
	" 4/20/09;\n"
	"4/3/09;\n"
	"Mar 20, 2009;\n"
	"March 20, 2009;\n"
	"Mar. 20, 2009;\n"
	"Mar 20 2009;\n"
	"20 Mar 2009;\n"
	"20 March 2009;\n"
	"2 Mar. 2009;\n"
	"20 March, 2009;\n"
	"Mar 20th, 2009;\n"
	"Mar 21st, 2009;\n"
	"Mar 22nd, 2009;\n"
	"Feb 2009;\n"
	"Sep 2009;\n"
	"Oct 2010;\n"
	"6/2008;\n"
	"12/2009;\n"
	"2009;\n"
	"January, 2020'''\n")

matches = re.finditer(date2, test_str)
for m in matches:
    print(m.group())

temps = re.findall(date2, test_str)
print(temps)
