import sys
import math

# highest frequency words
freq = []
while (len(freq) < 300):
    n = 0.0
    with open("Cifu-v1.txt", encoding="utf-8") as fi:
        first_line = fi.readline()
        for line in fi:
            fields=line.split()
            if len(fields[0]) == 1: # 1 for monosyllabic, 2 for disyllabic 
                if fields[0] not in freq:
                    if float(fields[3]) > n:
                        n = float(fields[3])
                        word = fields[0]
        freq.append(word)

# lowest density words
ND = []
while (len(ND) < 300):
    n = 100000000000000.0
    with open("Cifu-v1.txt", encoding="utf-8") as fi:
        first_line = fi.readline()
        for line in fi:
            fields=line.split("\t")
            if len(fields[0]) == 2:
                if fields[0] not in ND:
                    if float(fields[16]) < n:
                        n = float(fields[16])
                        word = fields[0]
        ND.append(word)

n=0
for x in range(300):
    if freq[x] in ND:
        print(freq[x])
        n=n+1
print(n)


