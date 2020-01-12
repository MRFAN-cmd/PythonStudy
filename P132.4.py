import csv

movies=[["トップガン","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]

with open("P132_4.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f,delimiter=",")
    for z in movies:
        w.writerow(z)
