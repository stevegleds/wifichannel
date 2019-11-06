logfile = "sample.log"
jsonfile = "sample.json"
findtext = "<CMD>WIFISCAN"
result = []
def clean(entry):
    entry = entry.replace('\\', '')
    return entry


with open(logfile) as log:
    with open(jsonfile, 'w') as json:
        for entry in log:
            if findtext in entry:
                print(entry)
                # clean(entry)
                entry = entry.replace('\\', '')
                start = entry.find("{")
                json_entry = entry[start:]
                print(f"{json_entry}")
                json.write(json_entry)
            