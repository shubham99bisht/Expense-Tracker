import random
from difflib import SequenceMatcher
from string import ascii_uppercase, digits, ascii_lowercase
VOCAB = ascii_uppercase +ascii_lowercase +digits + "&$-,.%=/: \t\n"

import numpy
import regex

def postprocess(string):
    new_string = ""
    for chr in string:
        if chr in small_vocab:
            new_string += chr
    return new_string

from string import ascii_uppercase, digits, punctuation, ascii_lowercase
def get_total(text):
    keywords = ["total", "subtotal", "charge"]
    suspects = []
    lines = text.split("\n")
    #print(lines)
    for line in lines:
        while "\t" in line: line.remove("\t")
        temp = [x for x in keywords if x in line.lower()]
        if len(temp)>=1:
            suspects += [line]
    #print(suspects)
    suspects = suspects[::-1]
    #suspects.sort(key = lambda x: len(x), reverse = True)
    nums = list(digits)
    for x in suspects:
        temp = [1 if y in x else 0 for y in nums]
        #print(x,temp)
        if any(temp):
            return x
    return "NIL"

def pred_to_dict(text, pred, prob):
    # res = {"company": [], "date": [], "address": [], "total": [get_total(text)]}
    res = {"company": [""],  "address":[""],"date": [""], "billid":[""],"total": [""],"items":[""]}
    curr, prv, ptr, ln = pred[0][0], 0, 1, len(text)
    while ptr<ln:
        while ptr<ln and pred[ptr][0]==curr:
            ptr+=1
        sample = text[prv:ptr]
        if curr==1:res["company"]+=[sample]
        if curr==2:res["address"]+=[sample]
        if curr==3:res["date"]+=[sample]
        if curr==4:res["billid"]+=[sample]
        if curr==5:res["total"]+=[sample]
        if curr==6:res["items"]+=[sample]
        #if curr==4: total
        if ptr<ln: curr = pred[ptr][0]
        prv = ptr
        ptr +=1
    final_res = {}
    res["company"].sort(key=lambda x: len(x), reverse=True)
    final_res["company"] = postprocess(res["company"][0])

    res["date"].sort(key=lambda x: len(x), reverse=True)
    final_res["date"] = res["date"][0]

    res["address"].sort(key=lambda x: len(x), reverse=True)
    final_res["address"] = res["address"][0]

    res["billid"].sort(key=lambda x: len(x), reverse=True)
    final_res["billid"] = res["billid"][0]

    final_res["total"] = ''.join(filter(lambda i: i.isdigit(), res["total"][0]))

    final_res["items"] = ",".join(str(x) for x in res["items"])
    #print("final_res: ",final_res)
    return final_res

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
    if n == 0:
        return ""
    else:
        return " "*n

def preprocess(string):
    new_string = ""
    for chr in string:
        if chr in VOCAB:
            new_string += chr
    return new_string
