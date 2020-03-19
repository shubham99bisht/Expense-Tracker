import re

# 04-20-2009; 04/20/2009; 4/20/09;
date1 = r"\b(0?[1-9]|[12][0-9]|3[01])\b(\s|,|-|\/|.)(\s|,|-|\/|.)?\b(0?[1-9]|[12][0-9]|3[01])\b(\s|,|-|\/|.)(\s|,|-|\/|.)?\b((20(0|1|2)\d)|((0|1|2)\d))\b"

# Monthname Date, Year; Mar 20, 2009;
date2 = r"\b(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\b(\s|,|-|\/|.)(\s|,|-|\/|.)?\b(0?[1-9]|[12][0-9]|3[01])(st|nd|th)?\b(\s|,|-|\/|.)(\s|,|-|\/|.)?\b((20(0|1|2)\d)|((0|1|2)\d))\b"

# Date Monthname, Year;  20 March, 2009;
date3 = r"\b(0?[1-9]|[12][0-9]|3[01])(st|nd|th)?\b(\s|,|-|\/|.)(\s|,|-|\/|.)?\b(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\b(\s|,|-|\/|.)(\s|,|-|\/|.)?\b((20(0|1|2)\d)|((0|1|2)\d))\b"

# Month, Year; Feb 2009; 12/2009;
date4 = r"\b(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\b(\s|,|-|\/|.)(\s|,|-|\/|.)?\b((20(0|1|2)\d)|((0|1|2)\d))\b"



test_str = "04-20-2009; 04/20/09; 4/20/09; 4/3/2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009; 20 Mar 2009; 20 March 2009; 2 Mar. 2009; 20 March, 2009; Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009; Feb 2009; Sep 2009; Oct 2010; 6/2008; 12/2009; 2009; 2010"

li = []

matches = re.finditer(date1, test_str)
for m in matches:
    li += [m.group()]

matches = re.finditer(date2, test_str)
for m in matches:
    li += [m.group()]

matches = re.finditer(date3, test_str)
for m in matches:
    li += [m.group()]

matches = re.finditer(date4, test_str)
for m in matches:
    li += [m.group()]

for x in li:
	print(x)