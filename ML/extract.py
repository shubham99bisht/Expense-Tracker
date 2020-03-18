import operator 
import sys
import re
import os
# import pandas as pd 
import json

def get_date(items):
	#format d/m/y & d-m-y is support
    dates=set()
    # print(items)
    for data in items:
        if 'W.E.F' in data:
            continue
        f1 = re.findall(r'\d{1,2}\d[\-|\/|\.]\d{1,2}\d[\-|\/|\.]\d{4}',data)
        f2 = re.findall(r'\d{4}\d[\-|\/|\.]\d{1,2}\d[\-|\/|\.]\d{1,2}',data)
        f3 = re.findall(r'\d{2}\d[\-|\/|\.]\d{1,2}\d[\-|\/|\.]\d{1,2}',data)
        f4 = re.findall(r'\d{1,2}\d[\-|\/|\.]\d{1,2}\d[\-|\/|\.]\d{2}',data)
        f5 = re.findall(r'(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2},\s+\d{4}',data)
        f6 = re.findall(r'\d{1,2}[\,|\/|\-](Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)[\,|\/|\-]\d{4}',data)
        f7 = re.findall(r'\d{1,2}[\,|\/|\-](Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)[\,|\/|\-]\d{2}',data)

        for i in f1:
            dates.add(i)
        for i in f2:
            dates.add(i)
        for i in f3:
            dates.add(i)
        for i in f4:
            dates.add(i)
        for i in f5:
            dates.add(i)
        for i in f6:
            dates.add(i)
        for i in f7:
            dates.add(i)
    dates = list(dates)
    return_me = dates[0] if dates else None
    return {
        'date' : return_me
    }

def get_time(data):
    time = set()

    for items in data:
        time_12 = re.findall(r'([0]?([1-9]|1[012])[:|-][0-5]?[0-9]?[:|-]?[0-5]?[0-9]\ ?([AaPp][Mm]|\ )?)', items)
        time_24 = re.findall(r'^(2[0-3]|[01]?[0-9])[:|-]([0-5]*[0-9])[:|-]?([0-5]?[0-9])\ ?$', items) 

        for i in time_12:
            time.add(i)
        for i in time_24:
            time.add(i)

    time = list(time)
    return_me = time[0] if time else None
    return{
        'time' : return_me
    }    

def get_total_amount(data):
    total_amount = set()
    for x in data:
        # print(x)
        if 'total' in x.lower().strip().strip('\n').split():
            total_amount.add(x)
        if 'net' in x.lower().strip().strip('\n').split():
            if 'total' in x.lower().strip().strip('\n').split():
                total_amount.add(x)
            if 'amount' in x.lower().strip().strip('\n').split():
                total_amount.add(x)
    for x in total_amount:
        if 'sub' in x.lower().strip().strip('\n').split():
            total_amount.remove(x)
    tlt_amt = ' '.join(list(total_amount))
    # amt_set = set()
    # linesplit=list(total_amount).split("TOTAL")[-1]
    p = re.compile(r'\d+[\.|\,|\s]?\d+')
    elem = p.findall(tlt_amt)
    return_me = max(elem) if elem else None
    return {
        'total_amount' : return_me
    }

def get_invoice_no(data):
    closest = None
    min = 2000000
    for i in data:
        if 'bill' in i.lower().strip().split() or 'invoice' in i.lower().strip().split() :
            individual = i.lower()
            f1 = re.findall(r'[A-Za-z]*.[0-9]{1,50}',i)
            bill_ind = individual.find('bill')
            if(bill_ind == -1):
                bill_ind = individual.find('invoice')
            for regs in f1:
                regs = regs.lower().strip()
                try:
                    ind = individual.find(regs)
                except:
                    continue
                
                if(ind>=bill_ind):
                    diff = ind - bill_ind
                else:
                    diff = bill_ind - ind
                if diff<min:
                    min = diff
                    closest = regs
    return {
        'invoice_no' : closest
        }

def get_address(data):
    with open('utils/cities.txt','r') as f:
        cities = f.readlines()
    cities = [i[3:-3].lower().strip().strip('\n') for i in cities][1:]
    idx = -1
    for j in cities:
        for i in data[:10]:
            comp = i.lower().strip().strip('\n').split()
            if j in comp:
                idx = data.index(i)
                break
    ret_me = data[max(0,idx-2):idx+1]
    if ret_me == []:
        ret_me = [i.lower().strip().strip('\n') for i in data[1:5]]
    return {
        'address' : ' '.join(ret_me)
    }

def get_store_name(data):
    existing_stores = os.listdir('Training Data Set')
    existing_stores.append('PHOENIX MALL')
    stores = [i.lower().strip('\n') for i in existing_stores]
    ret_me = []
    idx = 0
    for i in data[:5]:
        comp = i.lower().strip().strip('\n').split()
        for word in comp:    
            if word in stores:
                ret_me = word
                break
    if ret_me == []:
        # print("here")
        ret_me = [i.lower().strip().strip('\n') for i in data[1:2]]
        ret_me = ' '.join(ret_me)
    return {
        'store_name' : ret_me
    }

def get_items(data):
    for i in range(len(data)):
        cur = data[i].lower().strip().split()
        if('item' in cur or 'product' in cur or 'qty' in cur):
            item_ind = i+1
            break
    else:
        item_ind = 9
    for i in range(len(data)):
        cur = data[i].lower().strip().split()
        if('subtotal' in cur or 'total' in cur):
            subtot_ind = i+1
            break
    else:
        subtot_ind = -10
    return {
        'items' : data[item_ind:subtot_ind+1]
    }


