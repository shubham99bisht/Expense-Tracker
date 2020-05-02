from fuzzywuzzy import fuzz
import warnings
warnings.filterwarnings("ignore")
from Item_Labels import grocery, food, clothing, misc

def check_item_category(item):
    # item = input("Enter Item name: ")
    cat, pr = None, 0

    grocery_ratio = 0
    for key in grocery:
        ratio = fuzz.partial_ratio(item.lower(), key.lower())
        grocery_ratio = max(grocery_ratio, ratio)
    # print("Grocery ratio: ",grocery_ratio)
    if pr<grocery_ratio:
        cat = "Grocery"
        pr=grocery_ratio

    food_ratio = 0
    for key in food:
        ratio = fuzz.partial_ratio(item.lower(), key.lower())
        food_ratio = max(food_ratio, ratio)
    # print("Food ratio: ",food_ratio)
    if pr<food_ratio:
        cat = "Food"
        pr=food_ratio

    clothing_ratio = 0
    for key in clothing:
        ratio = fuzz.partial_ratio(item.lower(), key.lower())
        clothing_ratio = max(clothing_ratio, ratio)
    # print("Clothing ratio: ",clothing_ratio)
    if pr<clothing_ratio:
        cat = "Clothing"
        pr=clothing_ratio

    misc_ratio = 0
    for key in misc:
        ratio = fuzz.partial_ratio(item.lower(), key.lower())
        misc_ratio = max(misc_ratio, ratio)
    # print("Misc Ratio: ", misc_ratio)
    if pr<misc_ratio:
        cat = "Misc"
        pr=misc_ratio

    return cat

    # print("\t\t\n Item Category: {} \t Confidence: {}".format(cat, pr))

    # x = input("\nEnter another item? Press 1 to continue")