import random as r

random_szamok = []
SZAM= int(input("Adjon meg egy szamot 1 es 100 kozott!") or 14)


for i in range(0,20):
    rnum = r.randint(1,100)
    random_szamok.append((rnum,abs(rnum-SZAM)))

legkozelebbiszam = min(random_szamok,key=lambda lista:lista[1])[1]

legkozelebbiszamok = []

for i in range(len(random_szamok)):
    if random_szamok[i][1] == legkozelebbiszam:
        legkozelebbiszamok.append(i+1)

s = [x[0] for x in random_szamok]
print(random_szamok)
if len(legkozelebbiszamok)>1:
    #a
    print(f"a: {legkozelebbiszamok[0]}")
    #b
    print(f"b: {legkozelebbiszamok[-1]}")
    #c
    print(f"c: {legkozelebbiszamok}")
else:
    print(legkozelebbiszamok[0])