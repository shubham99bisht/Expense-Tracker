import json

for i in range(1,2):
    #op = open("ground_truth/{}.txt".format(i),"w")
    with open("data/{}.txt".format(i),"r") as f:
        text = f.read()
    print(text)
    while "\n" in text:
        text = text.replace("\n"," ")
    with open("results/{}.json".format(i),"r") as f:
        json = json.loads(f.read())
    print(text)
    print(json, type(json))
