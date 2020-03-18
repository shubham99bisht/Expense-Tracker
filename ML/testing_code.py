import os, random
from my_utils import get_total, get_date

folder = "original_data"
files = os.listdir(folder)
random.shuffle(files)

for file in files:
    print("\n File no.", file)
    with open(folder+"/"+file,"r") as f:
        data = f.read()
    print(data)

    total = get_total(data)
    print("\n Returned total value:", total, type(total))

    date = get_date(data)
    print("\n Returned date value:", date, type(date))

    if input("\n\nContinue? y/n")=="n":
        break
