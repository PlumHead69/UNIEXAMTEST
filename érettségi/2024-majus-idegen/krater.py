import math as m
with open("felszin_tpont.txt") as f:
    datas = [line.split() for line in f]

kraterek = []

for krater in datas:
    if len(krater)==5:
        nev = krater[3] + " " + krater[4]
        kraterek.append((float(krater[0]),float(krater[1]),float(krater[2]),nev))
    elif len(krater)==6:
        nev = krater[3] + " " + krater[4] + " " + krater[5]
        kraterek.append((float(krater[0]),float(krater[1]),float(krater[2]),nev))
    elif len(krater)==7:
        nev = krater[3] + " " + krater[4] + " " + krater[5] + " " + krater[6]
        kraterek.append((float(krater[0]),float(krater[1]),float(krater[2]),nev))

#2
print(f"2. feladat\nA kráterek száma: {len(kraterek)}")

#3

print(f"\n3. feladat")
KRATER_NEV = input("Kérem egy kráter nevét: ") or "Thomas Gold"
valasztott = [item for item in kraterek if item[3] == KRATER_NEV]
print(f"A(z) {KRATER_NEV} középpontja X={valasztott[0][0]} Y={valasztott[0][1]} sugara R={valasztott[0][2]}.")

#4

max_r=max(kraterek, key=lambda lista:lista[2])[2]
max_r_lista = [item[3] for item in kraterek if item[2]==max_r]

print(f"\n4. feladat\nA legnagyobb kráter neve és sugara: {max_r_lista[0]} {max_r}")


#5

def tavolsag(x1,y1,x2,y2):
     return m.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

#6

print(f"\n6. feladat")
KOZOS_PONT=input("Kérem egy kráter nevét: ") or "Jacques Cassini"

kozos_pont_krater = [item for item in kraterek if item[3]==KOZOS_PONT]

nincs_kozos_pont = []
for krater in kraterek:
    if krater[3]!=KOZOS_PONT and (krater[2]+kozos_pont_krater[0][2])<tavolsag(kozos_pont_krater[0][0],kozos_pont_krater[0][1],krater[0],krater[1]):
        nincs_kozos_pont.append(krater[3])

print(f"Nincs közös része: {', '.join(nincs_kozos_pont)}")


#7

print(f"\n7. feladat")

for nagy in kraterek:
    for kicsi in kraterek:
        if tavolsag(kicsi[0],kicsi[1],nagy[0],nagy[1])<(nagy[2]-kicsi[2]):
            print(f"A(z) {nagy[3]} kréter tartalmazza a(z) {kicsi[3]} krátert.")

#8

k = open("terulet.txt","w")

for krater in kraterek:
    k.write(str(round(krater[2]**2*3.14,2))+"\t"+krater[3]+"\n")


k.close()