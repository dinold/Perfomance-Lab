import sys
import json

with open(sys.argv[1]) as f:
    data = json.load(f)
with open(sys.argv[2]) as value:
    result = json.load(value)

def writeRec(datas):
    for item in datas["values"]:
        for znach in result["values"]:
            if item["id"] == znach["id"]:
                item["value"] = znach["value"]
                break
        if "values" in item:
            writeRec(item)

for item in data["tests"]:
    for znach in result["values"]:
        if item["id"] == znach["id"]:
            item["value"] = znach["value"]
            break
    if "values" in item:
        writeRec(item)

with open('report.json', 'w') as outfile:
    json.dump(data,outfile, indent = 4)


