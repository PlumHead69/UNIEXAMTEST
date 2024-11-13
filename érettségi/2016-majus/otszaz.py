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
s = []
for item in osszitem:
    if item != "F":  
        s.append(item)
    else:
        vasarlasok.append(s)
        s = []

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
print(f"{len(hanyadik)} vásárlás során vettek belőle.\n")

print("6. Feladat")
print(f"{darabszam} darab vételekor fizetendő: {ertek(darabszam)}\n")

print("7. Feladat")
#{}
aruk = cikkek(sorszam-1)
for aru in aruk:
    print(f"{len(aru)} {aru[0]}")


print("8. Feladat")

k = open("osszeg.txt","w")
kosarak = []
for i in range(len(vasarlasok)):
    f = 0
    for item in cikkek(i):
        f+=(ertek(len(item)))
    k.write(str(i+1) + " : "+str(f) + "\n")



k.close()











