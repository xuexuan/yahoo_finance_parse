import json
from datetime import date
def filter(month):
    res_dict = {}
    with open("symbol.json") as json_res:
        symbole_stock = json.load(json_res)
        for key in symbole_stock:
            print(key)
            if  len(symbole_stock[key]) != 0 and month in symbole_stock[key]["Ex-Dividend Date"]:
                if "N/A" not in symbole_stock[key]["Forward Annual Dividend Yield"] and float(symbole_stock[key]["Forward Annual Dividend Yield"].strip("%")) > 4.5:
                        res_dict[key+".HK"] = symbole_stock[key]
    return res_dict        

if __name__=="__main__":
    list = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for month in list:
        res_dict = filter(month)
        sortedkeys = sorted(res_dict, key=lambda x: float((res_dict[x]['Forward Annual Dividend Yield'].strip("%"))), reverse=True)
        new_dict = {}
        for obj in sortedkeys:
            new_dict[obj]= res_dict[obj]
        with open(month + "_"+str(date.today()) + ".json","w") as f:
            json.dump(new_dict,f)