import random, numpy, regex, re
from difflib import SequenceMatcher
from fuzzywuzzy import fuzz
from date_regex import get_date

from string import ascii_uppercase, digits, ascii_lowercase
VOCAB = ascii_uppercase +ascii_lowercase +digits + "&$-,.%=/: \t\n"
small_vocab = ascii_uppercase +ascii_lowercase +digits + " $,\t&-.:"

#"others":0,
#"vendor":1,
#"address":2,
#"date":3,   X
#"billid":4, X
#"total":5,  X
#"items":6


##############################################################################
# Functions in this file:
# 1. preprocess
# 2. postprocess
# 3. get_total
# 4. get_date
# 5. pred_to_dict
# -------------------------------
# 6. robust_padding
# 7. random_string
##############################################################################


def preprocess(string):
    new_string = ""
    for chr in string:
        if chr in VOCAB:
            new_string += chr
    return new_string

def postprocess(string):
    string = string.replace("\n"," ")
    string = string.replace("\t"," ")
    new_string = ""
    for chr in string:
        if chr in small_vocab:
            new_string += chr
    return new_string

def get_total(text):
    keywords = ["total", "subtotal", "charge", "amount"]
    suspects = []
    lines = text.split("\n")

    amt_vocab = ascii_lowercase + ascii_uppercase + digits + " ,."
    for line in lines:
        new_string = ""
        for chr in line:
            if chr in amt_vocab: new_string += chr

        temp = False
        for key in keywords:
            ratio = fuzz.partial_ratio(new_string.lower(), key)
            if ratio >=70: temp = True

        if temp: suspects += [new_string]

    suspects = suspects[::-1]
    print("\nSuspects for Total Amount: \n",suspects)
    amount = []
    for string in suspects:
        li = string.strip().split()
        for word in li:
            try:
                word = float(word)
                amount += [word]
            except: pass
    return str(max(amount)) if amount else "NIL"

'''
def get_date(text):
    dates=set()
    lines = text.split("\n")
    for data in lines:
        if 'w.e.f' in data.lower():
            continue
        temp = re.findall(regEx, data)
        for i in temp: dates.add(i)

    print(dates, type(dates))
    dates = list(dates)
    print("\nSuspected values for Date: ", dates)
    return dates[0] if dates else "Not Found"
'''

def pred_to_dict(text, pred, prob):
    # res = {"company": [], "date": [], "address": [], "total": [get_total(text)]}
    # res = {"company": [""],  "address":[""],"date": get_date(text), "billid":[""],"total": get_total(text),"items":[""]}
    res = {"company": [""],  "address":[""],"items":[""]}
    curr, prv, ptr, ln = pred[0][0], 0, 1, len(text)
    while ptr<ln:
        while ptr<ln and pred[ptr][0]==curr:
            ptr+=1
        sample = text[prv:ptr]
        if curr==1:res["company"]+=[sample]
        if curr==2:res["address"]+=[sample]
        if curr==6:res["items"]+=[sample]

        if ptr<ln: curr = pred[ptr][0]
        prv = ptr
        ptr +=1
    final_res = {"Date": get_date(text),"Amount": get_total(text)}
    res["company"].sort(key=lambda x: len(x), reverse=True)
    final_res["Company"] = postprocess(res["company"][0])
    if final_res["Company"]=="": final_res["Company"]="Not Found"

    res["address"].sort(key=lambda x: len(x), reverse=True)
    final_res["Address"] = postprocess(res["address"][0])
    if final_res["Address"]=="": final_res["Address"]="Not Found"

    final_res["Items"] = ", ".join(str(x) for x in res["items"])

    return final_res


###############################################################################
# For training data generation
def robust_padding(texts, labels):
    maxlen = max(len(t) for t in texts)

    for i, text in enumerate(texts):
        if len(text) == maxlen:
            continue

        pad_before = random.randint(0, maxlen - len(text))
        pad_after = maxlen - pad_before - len(text)

        texts[i] = random_string(pad_before) + text + random_string(pad_after)
        labels[i] = numpy.pad(
            labels[i], (pad_before, pad_after), "constant", constant_values=0
        )

def random_string(n):
    if n == 0: return ""
    else: return " "*n
