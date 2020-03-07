import json,os, numpy as np, torch

max_data = len(os.listdir("ground_truth"))+1

data = []

for i in range(1,max_data):
    with open("original_data/{}.txt".format(i),"r") as f:
        text = f.read()
    with open("ground_truth/{}.txt".format(i),"r") as f:
        gt = list(map(int,list(f.read())))
    gt_np = np.array(gt, dtype=np.int32)

    temp = (str(i),(text,gt_np))
    #print(temp)
    data += [(temp)]

torch.save(data,"final_data.pth")
