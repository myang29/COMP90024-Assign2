import json
import csv
with open("../harvester/result_try1.json", "r") as f:
    for line in f:
        line = line.rstrip()
        if line[-1] == ',':
            line = line[:-1]
        print(line)
        twit = json.loads(line)
        print (twit['retweeted'])
        print (type(twit['retweeted']))
        break


with open("wrath_word.csv",'r') as f:
    file = csv.reader(f)
    wrath_word = set(list(file)[0])
print (wrath_word)