with open("rendel.txt","r") as file:
    datas = [line.strip().split() for line in file]

reklamok = []
for data in datas:
    item = (int(data[0]), data[1], int(data[2]))
    reklamok.append(item)

#2

print(f"2. feladat\nA rendelések száma: {len(reklamok)}")

#3

print(f"\n3. feladat")
ORDER_NUM = int(input("Kérem, adjon meg egy napot: ") or 9)
c=0
for reklam in reklamok:
    if reklam[0] == ORDER_NUM:
        c+=1
print(f"A rendelések száma az adott napon: {c}")

#4


days=[i for i in range(1,31)]

for reklam in reklamok:
    if reklam[1]=="NR" and reklam[0] in days:
        days.remove(reklam[0])
print(f"\n4. feladat")
if len(days)!=0:
    print(f"{len(days)} nap nem volt a reklámban nem érintett városból rendelés")
else:
    print(f"Minden nap volt rendelés a reklámban nem érintett városból")


#5

print(f"\n5. feladat")
HIGHEST = max(reklamok, key=lambda lista:lista[2])[2]

for i in range(len(reklamok)):
    if reklamok[i][2] == HIGHEST:
        print(f"A legnagyobb darabszám: {HIGHEST}, a rendelés napja: {reklamok[i][0]} ")
        break


#6

def osszes(varos,nap):

    count=0
    for reklam in reklamok:
        if reklam[1]==varos and reklam[0]==nap:
            count+=reklam[2]

    return count

#7

PL_OSSZ = osszes("PL",21) 
TV_OSSZ = osszes("TV",21)
NR_OSSZ = osszes("NR",21)

print(f"\n7. feladat\nA rendelt termékek darabszáma a 21. napon PL: {PL_OSSZ} TV: {TV_OSSZ} NR: {NR_OSSZ}")


#8


varosok1 = {"PL":0, "TV":0, "NR":0}
varosok2 = {"PL":0, "TV":0, "NR":0}
varosok3 = {"PL":0, "TV":0, "NR":0}

for reklam in reklamok:
    if reklam[0] <= 10:
        varosok1[reklam[1]]+=1
    elif 10 < reklam[0] and reklam[0]<=20:
        varosok2[reklam[1]]+=1
    elif 20 < reklam[0]:
        varosok3[reklam[1]]+=1


print(f"\n8. feladat:\nNapok \t1..10 \t11..20 \t21..30 ")
print(f"PL\t{varosok1["PL"]}\t{varosok2["PL"]}\t{varosok3["PL"]}")
print(f"TV\t{varosok1["TV"]}\t{varosok2['TV']}\t{varosok3['TV']}")
print(f"NR\t{varosok1['NR']}\t{varosok2['NR']}\t{varosok3['NR']}")