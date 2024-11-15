import random as r
f = open("felszam.txt","r")
kerdesek = {}
s=[]
for line in f:
    s.append(line.strip())
for i in range(0,len(s)-1,2):
    kerdesek[s[i]] = s[i+1].split()
f.close()
print(f"2. Feladat\nFeladatok száma: {len(kerdesek)}")
matek = {'1':0 , '2':0 , '3' : 0}
for valasz in kerdesek.values():
    if valasz[2] == "matematika" and valasz[1] in list(matek.keys()): matek[valasz[1]]+=1
print(f"3. Feladat\nAz adatfaljban {matek['1'] + matek['2'] + matek['3']} matematika feladat van, 1 pontot er {matek['1']} feladat, 2 pontot er {matek['2']} feladat, 3 pontot er {matek['3']} feladat.")
print(f"4. Feladat\nAz adatfaljban a legkisebb szamertek {min(kerdesek.values(),key = lambda lista : lista[1])[1]}, a legnagyobb szamertek {max(kerdesek.values(),key = lambda lista : lista[1])[1]}")
targyak = []
for targy in kerdesek.values():
    if targy[2] not in targyak:
        targyak.append(targy[2])
print("5. Feladat\n"+"Az összes témakör:" , ", ".join(targyak))
print(f"6.Feladat")
tema = input("Milyen temakorbol szeretne kerdest kapni?") or "tortenelem"
temak = {}
for i in range(len(kerdesek)):
    if list(kerdesek.values())[i][2] == tema:
        temak[list(kerdesek.keys())[i]] = list(kerdesek.values())[i]
rkerdes = r.choice(list(temak.keys()))
valasz = input(rkerdes)
if temak[rkerdes][0] == valasz.strip(): print(f"A valasz {temak[rkerdes][1]} pontot er.")
else: print(f"A valasz 0 pontot er.\nA helyes válasz: {temak[rkerdes][0]}")
k = open("tesztfel.txt","w")
print("7. Feladat")
f=0
tesztkerdes = {}
for i in range(10):
    index_ = r.randrange(len(kerdesek))
    if list(kerdesek.keys())[index_] not in tesztkerdes.keys():
        tesztkerdes[list(kerdesek.keys())[index_]] = list(kerdesek.values())[index_]
        k.write(str(list(kerdesek.values())[index_][1]) +" "+ str(list(kerdesek.values())[index_][0])+ " " + list(kerdesek.keys())[index_]+"\n")
        f+=int(list(kerdesek.values())[index_][1])
k.write("A feladatsorra osszesen " +  str(f)+ " pont adhato.")
k.close()





