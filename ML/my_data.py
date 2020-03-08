import numpy, regex, torch, json, os, random
from os import path
from string import ascii_uppercase, digits,ascii_lowercase
from torch.utils import data

from my_utils import robust_padding

VOCAB = ascii_uppercase +ascii_lowercase +digits + "&$-,.%=/: \t\n"


class MyDataset(data.Dataset):
    def __init__(
        self, dict_path="data/data_dict.pth", device="cpu", val_size=76, test_path=None
    ):
        if dict_path is None:
            self.val_dict = {}
            self.train_dict = {}
        else:
            #data_items = list(torch.load(dict_path).items())
            data_items = torch.load(dict_path)
            random.shuffle(data_items)

            self.val_dict = dict(data_items[:val_size])
            self.train_dict = dict(data_items[val_size:])

        if test_path is None:
            self.test_dict = {}
        else:
            self.test_dict = torch.load(test_path)

        self.device = device

    def get_test_data(self, key):
        text = self.test_dict[key]
        text_tensor = torch.zeros(len(text), 1, dtype=torch.long)
        text_tensor[:, 0] = torch.LongTensor([VOCAB.find(c) for c in text])

        return text_tensor.to(self.device)

    def get_train_data(self, batch_size=8):
        samples = random.sample(self.train_dict.keys(), batch_size)

        texts = [self.train_dict[k][0] for k in samples]
        labels = [self.train_dict[k][1] for k in samples]

        robust_padding(texts, labels)

        maxlen = max(len(t) for t in texts)

        text_tensor = torch.zeros(maxlen, batch_size, dtype=torch.long)
        for i, text in enumerate(texts):
            text_tensor[:, i] = torch.LongTensor([VOCAB.find(c) for c in text])

        truth_tensor = torch.zeros(maxlen, batch_size, dtype=torch.long)
        for i, label in enumerate(labels):
            truth_tensor[:, i] = torch.LongTensor(label)

        return text_tensor.to(self.device), truth_tensor.to(self.device)

    def get_val_data(self, batch_size=8, device="cpu"):
        keys = random.sample(self.val_dict.keys(), batch_size)

        texts = [self.val_dict[k][0] for k in keys]
        labels = [self.val_dict[k][1] for k in keys]

        maxlen = max(len(s) for s in texts)
        texts = [s.ljust(maxlen, " ") for s in texts]
        labels = [
            numpy.pad(a, (0, maxlen - len(a)), mode="constant", constant_values=0)
            for a in labels
        ]

        text_tensor = torch.zeros(maxlen, batch_size, dtype=torch.long)
        for i, text in enumerate(texts):
            text_tensor[:, i] = torch.LongTensor([VOCAB.find(c) for c in text])

        truth_tensor = torch.zeros(maxlen, batch_size, dtype=torch.long)
        for i, label in enumerate(labels):
            truth_tensor[:, i] = torch.LongTensor(label)

        return keys, text_tensor.to(self.device), truth_tensor.to(self.device)



def prRed(skk): print("\033[91m{}\033[00m" .format(skk), end="")
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk), end="")
def prYellow(skk): print("\033[93m{}\033[00m" .format(skk), end="")
def prBlue(skk): print("\033[34m{}\033[00m" .format(skk), end="")
def prPurple(skk): print("\033[95m{}\033[00m" .format(skk), end="")
def prWhite(skk): print("\033[37m{}\033[00m" .format(skk), end="")
def prBlack(skk): print("\033[7m{}\033[00m" .format(skk), end="")

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
        elif n == 5:
            prPurple(c)
        elif n == 6:
            prBlack(c)
        else:
            prWhite(c)
    print()
