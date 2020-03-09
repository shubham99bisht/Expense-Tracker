import torch
from my_data import VOCAB, color_print
from my_models import MyModel0
from my_utils import pred_to_dict, preprocess
import json, cv2, pytesseract


def inference(text):
    text[0] = preprocess(text[0])
    device = torch.device("cpu")
    hidden_size=256
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

    # for x

    # with open("results/" + key + ".json", "w", encoding="utf-8") as json_opened:
    #     json.dump(result, json_opened, indent=4)

    return json

def tesseract_img(imgcv):
    text = pytesseract.image_to_string(imgcv,config="--psm 3") #default 3
    #1    Automatic page segmentation with OSD.
    #3    Fully automatic page segmentation, but no OSD. (Default)
    return inference([text])

def main(path_to_image):
    imgcv = cv2.imread(path_to_image)
    json_data = tesseract_img(imgcv)
    #with open('results/{}.json'.format(result_path), 'w') as fp:
        #json.dump(json_data, fp)
    #print(json)

if __name__ == "__main__":
    img_path = input("Enter path to image:")
    #res_path = input("Enter path to store results:")
    main(img_path)
