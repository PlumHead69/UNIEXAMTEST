def hatar(sor,ertek,kep):
    adottsor = kep[sor]

    for i in range(len(adottsor)-1):
        if (int(adottsor[i+1][0]) + int(adottsor[i+1][1]) + int(adottsor[i+1][2])) - (int(adottsor[i][0]) + int(adottsor[i][1]) + int(adottsor[i][2]))  > ertek:
            return True
    return False 

f = open("kep.txt","r")

kep = []

for line in f: 
    egyszin = []
    sorok = []
    counter = 0
    for szin in line.split():
        if counter == 3:
            sorok.append(egyszin)
            egyszin = []
            counter = 1
            egyszin.append(szin)
        else:
            egyszin.append(szin)
            counter+=1
    kep.append(sorok)

f.close()

print(f"\n2. feladat:\nKérem egy képpont adatait!\n")
sork = int(input("Sor:") or 180)
oszlopk = int(input("Oszlop:") or 320)
print(f"A képpont színe RGB({','.join(kep[sork-1][oszlopk-1])})")

vilagos = 0
for sor in kep:
    for szinek in sor:
        counter = 0
        for szin in szinek:
            counter += int(szin)
        if counter > 600:
            vilagos += 1
        
print(f"\n3. Feladat\nA világos képpontok száma: {vilagos}")

osszszinek = []

for sor in kep:
    for szinek in sor:
        s = []
        counter = 0
        for szin in szinek:
            counter += int(szin)
        s = [szinek, counter]
        osszszinek.append(s)


legsotetebb = min(osszszinek,key = lambda lista : lista[1])[1]
legsotetebbl = []

for osszin in osszszinek:
    if osszin[1] == legsotetebb: 
        legsotetebbl.append(osszin)

print(f"\n4. Feladat\nA legsötétebb pont RGB összege: {legsotetebb}\nA legsötétebb pixelek színe:")

for sotet in legsotetebbl:
    print(f"RGB({sotet[0][0]},{sotet[0][1]},{sotet[0][2]})")

elteresek = []

for i in range(len(kep)):
    if hatar(i,32,kep) == True:
        elteresek.append(i+1)

print(elteresek)
