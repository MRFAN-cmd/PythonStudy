import csv

with open("st.csv","r") as f:
    r=csv.reader(f,delimiter=",")
    for a in r:
        print(",".join(a))
        print("||")
    
