with open("naplo.txt","r") as f:
    datas = [line.strip().split() for line in f]

missings = 0
diary = []

for data in datas:
    if data[0] == "#":
        curdate = (int(data[1]),int(data[2]))
    else:  
        diary.append((curdate,data[0],data[1],data[2]))
        missings+=1
#2
print(missings)

#3
I=0
X=0

for d in diary:
    for missing in d[3]:
        if missing=="I":
            I+=1
        if missing == "X":
            X+=1
print((X,I))

#4

def hetnapja(honap,nap):
    napnev = ("vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat")
    napszam = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
    napsorszam = (napszam[honap-1]+nap) % 7
    hetnapja = napnev[napsorszam]
    return hetnapja

#5

HONAP = 2
NAP = 3
print(hetnapja(HONAP,NAP))

#6
NAP_NEV = "szerda"
ORA_SORSZAM = 3

i=0
for d in diary:
   if hetnapja(d[0][0],d[0][1]) == "szerda":
       if d[3][2] == "X" or d[3][2] == "I":
           i+=1
print(i)

#6

names =[]
for d in diary:
    names.append((d[1],d[2]))
names_set = set(names)
names_set = list(names_set)

names_with_missings = []

for i in range(len(names_set)):
    misses = 0
    for d in diary:
        if (d[1],d[2]) == names_set[i]:
            for missings in d[3]:
                if missings == "X" or missings == "I":
                    misses+=1
    names_with_missings.append((i,misses))

most_missies = max(names_with_missings,key = lambda lista:lista[1])[1]

for name in names_with_missings:
    if name[1] == most_missies:
        print(names_set[name[0]])