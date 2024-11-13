def ertek(darabszam):
    if darabszam == 1:
        return 500
    elif darabszam == 2:
        return 950
    elif darabszam >= 3:
        return 950+(darabszam-2)*400

def cikkek(vasarlas):
    rendezett = []
    voltmar = []
    for item in vasarlasok[vasarlas]:
        items = []
        if item in voltmar:
            continue
        for nextitem in vasarlasok[vasarlas]:
            if nextitem == item:
                items.append(nextitem)
        voltmar.append(item)
        rendezett.append(items)
    return rendezett
f = open("penztar.txt", "r")

osszitem = []

for item in f:
    osszitem.append(str(item).strip())

vasarlasok = []
vasarlas = []
for item in osszitem:
    if item != "F":  
        vasarlas.append(item)
    else:
        vasarlasok.append(vasarlas)
        vasarlas = []

f.close()

print("2. Feladat")
counter=0
for item in osszitem:
    if item == "F":
        counter+=1
print(f"A fizetések száma: {counter}\n")

print("3. Feladat")
counter2 = 0
for i in range(len(osszitem)):
    if osszitem[i] == "F":
        break
    else: counter2+=1
print(f"Az első vásárló {counter2} darab árucikket vásárolt.\n")

print("4. Feladat")
sorszam = int(input("Adja meg egy vásárlás sorszámát! ") or 2)
arucikk = input("Adja meg egy árucikk nevét! ") or "kefe"
darabszam = int(input("Adja meg a vásárolt darabszámot! ") or 2)

print("\n5. Feldat")
hanyadik = []
#mikor fordul elo eloszor
for i in range(len(vasarlasok)):
    if arucikk in vasarlasok[i]:
        hanyadik.append(i)
print(f"Az első vásárlás sorszáma: {hanyadik[0]+1}")
print(f"Az utolsó vásárlás sorszáma: {hanyadik[-1]+1}")
print(f"{len(hanyadik)}vásárlás során vettek belőle.\n")

print("6. Feladat")
print(f"{darabszam} darab vételekor fizetendő: {ertek(darabszam)}")

print("7. Feladat")
voltmar = []
for item in vasarlasok[sorszam-1]:
    items = []
    if item in voltmar:
        continue
    for nextitem in vasarlasok[sorszam-1]:
        if nextitem == item:
            items.append(nextitem)
    voltmar.append(item)
    #print(f"{len(items)} {items[0]}")

print(cikkek(sorszam-1))
print("8. Feladat")

k = open("osszeg.txt","w")

for egyember in vasarlasok:
    ertekek = 0
    fasz = cikkek(egyember)
    for fasz2 in fasz:
        erteke = ertek(fasz2)
        ertekek+= erteke
print(ertekek)





k.close()











