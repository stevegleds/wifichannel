import pandas as pd
import json

jsonfile = "sample.json"
cleanjsonfile = "cleansample.json"
csvfile = "sample.csv"
count = 0
print(jsonfile)

def is_json(myjson):
    try:
        # print(json.loads(myjson))
        return True
    except ValueError :
        return False

with open(jsonfile, 'r') as json:
    with open(cleanjsonfile, 'w') as cleanjson:
        print(f"this should be json content:{json}")
        count =  0
        for entry in json:
            count += 1
            try:
                print(count)
                print(f"Entry number {count} ")
                commandresultstart = entry.find("CommandResult") + 16
                # print(entry[commandresultstart:commandresultstart+10])
                commandresultend = entry.find("CommandName") - 13
                # print(entry[commandresultend:commandresultend+10])
                entry = entry[:commandresultstart] + entry[commandresultstart:commandresultend].replace('"','') + entry[commandresultend:]
                # print("new entry is:", entry)
                cleanjson.write(entry)
            except "not json" as js_error:
                print(f"entry {count} failed my json test")
                
# dfjson = pd.read_json(cleanjsonfile)
with open(cleanjsonfile, 'r') as myjson:
    jsondata = json.loads(myjson)
print(f"{dfjson}")
df = pd.DataFrame()
with open(jsonfile) as json:
    with open(csvfile, 'w') as csv:
        count += 1
        print(count)
        for entry in json:
            try:
                df.append = pd.read_json("sample.json", lines=True)
            except:
                pass
# print(f"{df}")
# df.to_csv("sample.csv")