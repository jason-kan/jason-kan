import sys
import math
with open("Cifu-v1.txt", encoding="utf-8") as fi:
    first_line = fi.readline()
    for line in fi:
        fields=line.split()
        if fields[0] == sys.argv[1]:
         print("The word "+fields[0])
         print("The number counted in child-directed corpus is " + fields[2] + "  (" + fields[3] + " per million tokens)")
         print("The number counted in child spoken corpus is " + fields[8] + "  (" + fields[9] + " per million tokens)")
         print("The number counted in adult spoken corpus is " + fields[4] + "  (" + fields[5] + " per million tokens)")


