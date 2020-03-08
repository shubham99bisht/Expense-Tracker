import random
from difflib import SequenceMatcher
from string import ascii_uppercase, digits

import numpy
import regex


def pred_to_dict(text, pred, prob):
    res = {"company": ("", 0),  "address": ("", 0),"date": ("", 0), "billid":("",0),"total": ("", 0),"items":("",0)}
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
