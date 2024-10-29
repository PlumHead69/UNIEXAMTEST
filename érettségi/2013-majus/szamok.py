import random as r
f = open("felszam.txt","r")
kerdesek = []
valaszok = []
i=0
for line in f:
    if i%2 == 0: kerdesek.append(line.strip())
    else: valaszok.append(line.split())
    i+=1
f.close()

print(f"2. Feladat\nFeladatok száma: {len(kerdesek)}")
matek = {'1':0 , '2':0 , '3' : 0}

for valasz in valaszok:
    if valasz[2] == "matematika" and valasz[1] in list(matek.keys()):
        matek[valasz[1]]+=1
print(f"3. Feladat\nAz adatfaljban {matek['1'] + matek['2'] + matek['3']} matematika feladat van, 1 pontot er {matek['1']} feladat, 2 pontot er {matek['2']} feladat, 3 pontot er {matek['3']} feladat.")
print(f"4. Feladat\nAz adatfaljban a legkisebb szamertek {min(valaszok,key = lambda lista : lista[1])[1]}, a legnagyobb szamertek {max(valaszok,key = lambda lista : lista[1])[1]}")
targyak = []
for targy in valaszok:
    if targy[2] not in targyak:
        targyak.append(targy[2])
print("5. Feladat\n"+"Az összes témakör: " , ", ".join(targyak))
print(input("Milyen temakorbol szeretne kerdest kapni?") or "tortenelem" )














