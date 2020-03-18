import re

'''
connectors = (\s|,|-|\/|.)
year = \b((20(0|1|2)\d)|((0|1|2)\d))\b
month_names = (Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)
month_numeric = (0?[1-9]|10|11|12)
date = \b(0?[1-9]|[12][0-9]|3[01])(st|nd)?\b
'''

# 04-20-2009; 04/20/2009; 4/20/09;
date1 = r"\b(0?[1-9]|[12][0-9]|3[01])\b(\s|,|-|\/|.)(\s|,|-|\/|.)?\b(0?[1-9]|[12][0-9]|3[01])\b(\s|,|-|\/|.)(\s|,|-|\/|.)?\b((20(0|1|2)\d)|((0|1|2)\d))\b"

# Monthname Date, Year; Mar 20, 2009;
date2 = r"\b(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\b(\s|,|-|\/|.)(\s|,|-|\/|.)?\b(0?[1-9]|[12][0-9]|3[01])(st|nd|th)?\b(\s|,|-|\/|.)(\s|,|-|\/|.)?\b((20(0|1|2)\d)|((0|1|2)\d))\b"

# Date Monthname, Year;  20 March, 2009;
date3 = r"\b(0?[1-9]|[12][0-9]|3[01])(st|nd|th)?\b(\s|,|-|\/|.)(\s|,|-|\/|.)?\b(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\b(\s|,|-|\/|.)(\s|,|-|\/|.)?\b((20(0|1|2)\d)|((0|1|2)\d))\b"

# Month, Year; Feb 2009; 12/2009;
date4 = r"\b((Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)|((0|1|2)\d))\b(\s|,|-|\/|.)(\s|,|-|\/|.)?\b((20(0|1|2)\d)|((0|1|2)\d))\b"

dateEntries = '''


Feb 2009;
Sep 2009;
Oct 2010;
6/2008;
12/2009;
2009;
January, 2020'''



connectors = "(\s|,|-)"
year = "(20(0|1|2)\d)"

# re1 =  "r'" + connectors + year + "'"
re1 = connectors + year
print(re1)
temps = re.findall(re1, dateEntries)
print(temps)
