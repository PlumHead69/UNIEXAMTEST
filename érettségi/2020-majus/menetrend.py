with open("vonat.txt") as f:
    datas = [line.strip().split() for line in f]


vonatok = [(int(item[0]),int(item[1]),int(item[2]),int(item[3]),item[4]) for item in datas]

#2

allomasok_szama = []
vonatok_szama = []

for vonat in vonatok:
    if vonat[0] not in vonatok_szama:
        vonatok_szama.append(vonat[0])
    elif vonat[1] not in allomasok_szama:
        allomasok_szama.append(vonat[1])
    

print(f"2. feladat\nAz állomások száma: {len(allomasok_szama)+1}\nA vonatok száma: {len(vonatok_szama)}")

#3

















