import argparse
import torch
from my_data import MyDataset, VOCAB, color_print
from my_models import MyModel0
from my_utils import pred_to_dict, preprocess
import json

'''
def test():
    model = MyModel0(len(VOCAB), 16, args.hidden_size).to(args.device)
    # dataset = MyDataset(None, args.device, test_path="data/test_dict.pth")

    model.load_state_dict(torch.load("model.pth"))

    model.eval()
    with torch.no_grad():
        for key in dataset.test_dict.keys():
            text_tensor = dataset.get_test_data(key)

            oupt = model(text_tensor)
            prob = torch.nn.functional.softmax(oupt, dim=2)
            prob, pred = torch.max(prob, dim=2)

            prob = prob.squeeze().cpu().numpy()
            pred = pred.squeeze().cpu().numpy()

            real_text = dataset.test_dict[key]
            result = pred_to_dict(real_text, pred, prob)

            with open("results/" + key + ".json", "w", encoding="utf-8") as json_opened:
                json.dump(result, json_opened, indent=4)

            print(key)
'''

def inference(text):
    text[0] = preprocess(text[0])
    device = torch.device("cpu")
    hidden_size=256
    model = MyModel0(len(VOCAB), 16, hidden_size).to(device)
    model.load_state_dict(torch.load("model_cuda_latest.pth", map_location=torch.device('cpu')))

    #text = ["shubham bisht, something ahppen"]
    text_tensor = torch.zeros(len(text[0]), 1, dtype=torch.long)
    text_tensor[:, 0] = torch.LongTensor([VOCAB.find(c) for c in text[0].upper()])
    #print(text_tensor)
    inp = text_tensor.to(device)

    oupt = model(inp)
    prob = torch.nn.functional.softmax(oupt, dim=2)
    prob, pred = torch.max(prob, dim=2)

    color_print(text[0], pred)
    json = pred_to_dict(text[0], pred, prob)
    print("\n###########################\n")
    print(json)

    # with open("results/" + key + ".json", "w", encoding="utf-8") as json_opened:
    #     json.dump(result, json_opened, indent=4)

    return json

def tesseract_img(imgcv):
    text = pytesseract.image_to_string(imgcv,config="--psm 3") #default 3
    #1    Automatic page segmentation with OSD.
    #3    Fully automatic page segmentation, but no OSD. (Default)
    return inference([text])

def main(path_to_image, result_path = "temp"):
    imgcv = cv2.imread(path_to_image)
    json_data = tesseract_img(imgcv)
    with open('results/{}.json'.format(result_path), 'w') as fp:
        json.dump(json_data, fp)
    #print(json)
    return "Job done!"

if __name__ == "__main__":
    img_path = input("Enter path to image:")
    res_path = input("Enter path to store results:")
    main(img_path, res_path)
