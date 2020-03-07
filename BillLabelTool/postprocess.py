import json, os

max_data = len(os.listdir("results"))+1

for i in range(1,max_data):
    with open("original_data/{}.txt".format(i),"r") as f:
        text = f.read()
    with open("results/{}.json".format(i),"r") as f:
        data = f.read()
    data = json.loads(data)

    gt = [0 for i in range(len(text))] # 0  = "Others" Category

    vendor = data["vendor"][0]  # "vendor":1
    index = text.find(vendor)
    if index!=-1:
        length = len(vendor)
        gt[index:index+length] = [1]*length

    address = data["address"][0] # "address":2
    address = address.replace(";","\n")
    index = text.find(address)
    if index!=-1:
        length = len(address)
        gt[index:index+length] = [2]*length

    date = data["date"][0] # "date":3
    index = text.find(date)
    if index!=-1:
        length = len(date)
        gt[index:index+length] = [3]*length

    billid = data["billid"][0] # "billid":4
    index = text.find(billid)
    if index!=-1:
        length = len(billid)
        gt[index:index+length] = [4]*length

    total = data["total"][0] # "total":5
    index = text.find(total)
    if index!=-1:
        length = len(total)
        gt[index:index+length] = [5]*length

    total_items = int(data["total_item"][0])
    for x in range(1, total_items+1):
        name = "item_"+str(x)
        item = data[name][0]
        index = text.find(item)
        length = len(item)
        gt[index:index+length] = [6]*length

    gt = "".join(str(x) for x in gt)
    f = open("ground_truth/{}.txt".format(i), "w")
    f.write(gt)
