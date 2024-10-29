def travelcalc(start,end,speed):

    timespent = 0
    if start['óra'] == end['óra']:
        timespent = int(end['perc']) - int(start['perc'])
    else:
        timespent = 60 - int(start['perc']) + int(end['perc'])

    s = timespent/60 * speed

    return s

f = open("jeladas.txt","r")

autok = []

for line in f:

    auto = []
    s = line.split()

    auto.append(s[0])
    time={
        'óra':s[1],
        'perc':s[2]
    }
    auto.append(time)
    auto.append(int(s[3]))
    
    autok.append(auto)


print("2. Feladat")
print(f"Az utolsó jeladás időpontja {autok[-1][1]['óra']}:{autok[-1][1]['perc']}, a jármű rendszáma {autok[-1][0]}\n")

print("3. Feladat")
print(f"Az első jármű {autok[0][0]}")
jelek = []
for auto in autok:
    if auto[0] == autok[0][0]:
        jelek.append(list(auto[1].values()))

items=[]
for item in jelek:
    s = ':'.join(item)
    items.append(s)
print("Jeladásainak időpontjai:"," ".join(items))
#bajos rész volt

print("\n4. Feladat")
óra = str(input("Kérem, adja meg az órát: ") or 6)
perc = str(input("Kérem, adja meg a percet: ") or 54)

jeladasoknum = 0
for auto in autok:
    if auto[1]['óra'] == óra and auto[1]['perc'] == perc:
        jeladasoknum+=1
print(f"A jeladások száma: {jeladasoknum}")

print("\n5. Feladat")
maxspeed = 0
for auto in autok:
    if auto[2] > maxspeed:
        maxspeed=auto[2]
print(f"A legnagyobb sebesség km/h: {maxspeed}")

maxspeedcars = []
for auto in autok:
    if auto[2] == maxspeed:
        maxspeedcars.append(auto[0])
print("A járművek:", *maxspeedcars)

print("\n6. Feladat")
redszam = input("Kérem, adja meg a rendszámot: ") or "ZVJ-638"
jelzesek = []
for auto in autok:
    if auto[0] == redszam:
        jelzesek.append(auto)

curdistance = 0
for i in range(len(jelzesek)-1):
    s = jelzesek[i][1].values()
    print(":".join(s),curdistance,"km")
    cd = travelcalc(jelzesek[i][1],jelzesek[i+1][1],jelzesek[i][2])
    cd = round(cd,1)
    curdistance+=cd

#7. Feladat
mindeneslista = []

onlyonce = []
for auto in autok:
    if auto[0] not in onlyonce:
        onlyonce.append(auto[0])

for car in onlyonce:
    autolist = []
    for i in range(len(autok)):
        if car == autok[i][0]:
            autolist.append(autok[i])

    s = [autolist[0],autolist[-1]]
    
    mindeneslista.append(s)



k = open("ido.txt","w")

for auto in mindeneslista:
    ido1 = list(auto[0][1].values())
    ido2 = list(auto[1][1].values())
    k.write(str(auto[0][0])+ " " +" ".join(ido1)+ " "+" ".join(ido2) + "\n")





