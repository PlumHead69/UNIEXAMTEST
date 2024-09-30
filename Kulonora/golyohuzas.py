"""def Szinvalogatas(colors):
    
    allcolors = []

    for color in colors:
        if color not in allcolors:
            allcolors.append(color)

    return allcolors


def Darab(allcolors,colors):

    allnums = []
    counter = 0

    for allcolor in allcolors:
        for color in colors:
            if color == allcolor:
                counter+=1
        allnums.append(counter)
        counter = 0    

    return allnums"""

"""

f = open("golyohuzas.txt", "r", encoding = "utf-8") 

colors = []

for line in f:
    colors.append(line.strip())

f.close()


allcolors = Szinvalogatas(colors)
print(f"A zsákban található golyók: {', '.join(allcolors)}")

allnums = Darab(allcolors,colors)

for i in range(len(allnums)):
    print(f"{allcolors[i]} : {allnums[i]}")"""


allcolors = {}

f = open("golyohuzas.txt", "r" , encoding="utf-8")


for line in f:
    s = line.strip()
    if s in allcolors:
        allcolors[s] += 1
    else:
        allcolors[s] = 1

f.close()

print(allcolors)
#szotarak bejarasa 

#bejaras csak a kulcsokon
for s in allcolors:
    print(s)

for kulcs in allcolors.keys():
    print(kulcs)

#bejaras csak az ertekeken
for ertek in allcolors.values():
    print(ertek)

print(f"A legnagyobb darabszam: {max(allcolors.values())}")

#bejaras kulcs ertek parokon

for kulcs, ertek in allcolors.items():
    if ertek == max(allcolors.values()):
        print(kulcs)

