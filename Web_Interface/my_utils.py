import numpy
import regex
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

#VOCAB = ascii_uppercase +digits + punctuation + " \t\n" # old model
VOCAB = ascii_uppercase +ascii_lowercase +digits + "&$-,.%=/: \t\n"

small_vocab = ascii_uppercase +ascii_lowercase +digits + punctuation+" "

def prRed(skk): print("\033[91m{}\033[00m" .format(skk), end="")
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk), end="")
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk), end="")
def prBlue(skk): print("\033[34m{}\033[00m" .format(skk), end="")
def prPurple(skk): print("\033[95m{}\033[00m" .format(skk), end="")
def prWhite(skk): print("\033[37m{}\033[00m" .format(skk), end="")

def color_print(text, text_class):
    for c, n in zip(text, text_class):
        if n == 1:
            prRed(c)
        elif n == 2:
            prGreen(c)
        elif n == 3:
            prBlue(c)
        elif n == 4:
            prYellow(c)
        else:
            prWhite(c)
    print()

def preprocess(string):
    new_string = ""
    for chr in string:
        if chr in VOCAB:
            new_string += chr
    return new_string

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
    res = {"company": [], "date": [], "address": [], "total": [get_total(text)]}
    curr, prv, ptr, ln = pred[0][0], 0, 1, len(text)
    while ptr<ln:
        while ptr<ln and pred[ptr][0]==curr:
            ptr+=1
        sample = text[prv:ptr]
        if curr==1:res["company"]+=[sample]
        if curr==2:res["date"]+=[sample]
        if curr==3:res["address"]+=[sample]
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
    final_res["address"] = postprocess(res["address"][0])

    final_res["total"] = postprocess(res["total"][0])
    #print("final_res: ",final_res)
    return final_res


'''
def pred_to_dict_orig(text, pred, prob):
    res = {"company": ("", 0), "date": ("", 0), "address": ("", 0), "total": ("", 0)}
    keys = list(res.keys())

    seps = [0] + (numpy.nonzero(numpy.diff(pred))[0] + 1).tolist() + [len(pred)]
    for i in range(len(seps) - 1):
        pred_class = pred[seps[i]] - 1
        if pred_class == -1:
            continue

        new_key = keys[pred_class]
        new_prob = prob[seps[i] : seps[i + 1]].max()
        if new_prob > res[new_key][1]:
            res[new_key] = (text[seps[i] : seps[i + 1]], new_prob)

    return {k: regex.sub(r"[\t\n]", " ", v[0].strip()) for k, v in res.items()}
'''
