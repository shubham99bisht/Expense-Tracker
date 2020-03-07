import os

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


data = os.listdir("ground_truth")
x = 1
skip = 0
for i in data:
    print(i)
    if x==0: break
    if x==2 and skip!=5:
        skip += 1
        continue
    skip = 0
    with open("original_data/{}".format(i),"r") as f:
        text = list(f.read())
    with open("ground_truth/{}".format(i),"r") as f:
        text_class = list(map(int,list(f.read())))
    color_print(text, text_class)
    x = int(input("Want to see more?\n\t0 to exit\n\tPress 1 for next\n\tPress 2 to skip 5 images"))
