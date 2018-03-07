import json

fs_src = open("./holders.txt", "rt")
fs_tgt = open("./bills.js", "wt")

bills = list()

while True:
    line = fs_src.readline()
    #print(line)
    if not line or len(line) == 0:
        break
    fields = line.split(" ")
    if len(fields) < 3:
        continue 
    bill = {"idx": fields[0], "addr": fields[1], "bal": fields[2]}
    bills.append(bill)

print(bills)
json.dump(bills, fs_tgt)

fs_src.close()
fs_tgt.close()

