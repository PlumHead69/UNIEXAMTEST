with open("felajanlas.txt") as file:
    spots = int(file.readline())
    data = [line.strip().split() for line in file]

offers = [(int(item[0]),int(item[1]),item[2]) for item in data]

#2
print(f"2. feladat\nA felajánlások száma: {len(offers)}\n")

#3

both = [str(i+1) for i in range(len(offers)) if offers[i][0]>offers[i][1]]

print(f"3. feladat\nA bejárat mindkét oldalán ültetők: {' '.join(both)}")

#4
print(f"\n4. feladat")
AGYAS = int(input("Adja meg az ágyás sorszámát!") or 100)

places = []

for i in range(len(offers)):
    if offers[i][0]<offers[i][1]:
        if offers[i][0]<=AGYAS<=offers[i][1]:
            places.append((i,offers[i][2]))
    else:
        if offers[i][0]<=AGYAS or offers[i][1]>AGYAS:
            places.append((i,offers[i][2]))

print(f"A felajánlók száma: {len(places)}")

if len(places)!=0:
    print(f"A virágágyás színe, ha csak az első ültet: {places[0][1]}")

    colors = [x[1] for x in places]
    colors = set(colors)
    print(f"A virágágyás színei: {' '.join(colors)}")

#5

print(f"\n5. feladat")

def both_sides(offer):
    places = []
    if offer[0]>offer[1]:
        for i in range(offer[0],spots+1):
            places.append(i)
        for i in range(1,offer[1]+1):
            places.append(i)
    else:
        for i in range(offer[0],offer[1]+1):
            places.append(i)
    return places



ultetesek = {}
ultetesek2 = {}
for i in range(1,spots+1):
    ultetesek[i]=0
    ultetesek2[i]=0


for offer in offers:
    check = both_sides(offer)
    for k in check:
        ultetesek[k]+=1

missed = list(ultetesek.values()).count(0)
all_offers = sum(ultetesek.values())

if all_offers==spots and missed==0:
    print(f"Minden ágyás beültetésére van jelentkező.")
elif all_offers>=spots and missed>0:
    print(f"Átszervezéssel megoldható a beültetés.")
elif all_offers<spots:
    print(f"A beültetés nem oldható meg.")


#6

k = open("szinek.txt","w")

for i in range(len(offers)):
    check = both_sides(offers[i])
    for c in check:
        if ultetesek2[c]==0:
            ultetesek2[c]=(offers[i][2],i+1)


for item,value in ultetesek2.items():
    if value!=0:
        k.write(value[0] +" "+str(value[1])+"\n")
    else:
        k.write("#"+" "+str(value)+"\n")

k.close()