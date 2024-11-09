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

print(f"6.Feladat")
tema = input("Milyen temakorbol szeretne kerdest kapni?") or "tortenelem"
temak = {}
for i in range(len(kerdesek)):
    if valaszok[i][2] == tema:
        temak[kerdesek[i]] = valaszok[i]
rkerdes = r.choice(list(temak.keys()))
valasz = input(rkerdes)
if temak[rkerdes][0] == valasz.strip(): 
    print(f"A valasz {temak[rkerdes][1]} pontot er.")
else:
    print(f"A valasz 0 pontot er.\nA helyes válasz: {temak[rkerdes][0]}")

k = open("tesztfel.txt","w")
print("7. Feladat")
f=0
tesztkerdes = {}
for i in range(10):
    index_ = r.randrange(len(kerdesek))
    if kerdesek[index_] not in tesztkerdes.keys():
        tesztkerdes[kerdesek[index_]] = valaszok[index_]
        k.write(str(valaszok[index_][1]) +" "+ str(valaszok[index_][0])+ " " + kerdesek[index_]+"\n")
        f+=int(valaszok[index_][1])
k.write("A feladatsorra osszesen " +  str(f)+ " pont adhato.")
k.close()





