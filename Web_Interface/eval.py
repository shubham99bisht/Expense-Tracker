import torch
from my_models import MyModel0
from my_utils import pred_to_dict, VOCAB, color_print, preprocess
import json
import cv2
import pytesseract


def inference(text):
    text[0] = preprocess(text[0])
    device = torch.device("cpu")
    hidden_size=256
    #model = MyModel0(len(VOCAB), 16, hidden_size).to(device) #old model
    model = MyModel0(len(VOCAB), 16, hidden_size).to(device)
    model.load_state_dict(torch.load("model.pth", map_location=torch.device('cpu')))

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
    return json

def tesseract_img(imgcv):
    text = pytesseract.image_to_string(imgcv,config="--psm 3") #default 3
    #1    Automatic page segmentation with OSD.
    #3    Fully automatic page segmentation, but no OSD. (Default)
    return inference([text])

def main(path_to_image, result_path = "temp"):
    return {'company':'McD', 'address':'badlapur', 'date':'05/6/2020', 'items':'burgers, drinks, etc.', 'total':'550'}
    imgcv = cv2.imread(path_to_image)
    json_data = tesseract_img(imgcv)
    # with open('results/{}.json'.format(result_path), 'w') as fp:
        # json.dump(json_data, fp)
    return str(json)
