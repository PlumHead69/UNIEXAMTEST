import random as r
f = open("felszam.txt","r")
kerdesek = {}

for line in f:
    line2 = f.readline().strip().split()
    kerdesek[line.strip()] = [int(line2[0]), int(line2[1]), line2[2]]




