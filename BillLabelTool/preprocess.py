import os
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
VOCAB = ascii_uppercase +ascii_lowercase +digits + "&$-,.%=/: \t\n"

files = os.listdir("train_data")

for file in files:
    if file[0]==".": continue
    with open("train_data/"+file, "r") as f:
        text = f.read()
    new_text = ""
    for x in text:
        if x in VOCAB:
            new_text += x

    new_text = new_text.replace("\n",";\n")

    f = open("preprocessed_data/"+file,"w")
    f.write(new_text)
    f.close()
