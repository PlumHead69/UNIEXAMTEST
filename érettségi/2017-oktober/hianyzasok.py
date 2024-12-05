def hetnapja(honap,nap):
    napnev= ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam = [ 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = napszam[honap-1]+nap #miert nem mukodik a MOD ha ide rakom?
    hetnapja = napnev[napsorszam%7]

    return hetnapja


f = open("naplo.txt", "r")
#{}
hianyzasok = []

for line in f:
    s=[]
    
    diaks=[]
    diak=[]
    line.strip()

    if line[0] == "#":
        nap = []
        for char in line.split():
            if char != "#":
                nap.append(int(char))
        
    else:
        diaks.append(line.split())
        nev = diaks[0][0] + " " +diaks[0][1]
        diak= [nev,diaks[0][2]]
    
        s=[diak,nap]
        hianyzasok.append(s)
        
f.close()

print(f"2.Feladat\nA naplóban {len(hianyzasok)} bejegyzés van.")

igazolt=0
igazolatlan = 0

for diak in hianyzasok:
    for char in diak[0][1]:
        if char == "X":
            igazolt+=1
        elif char == "I":
            igazolatlan+=1
print(f"\n3. Feladat\nAz igazolt hiányzások száma {igazolt}, az igazolatlanoké {igazolatlan} óra.")

print(f"\n5. Feladat")
honap = int(input("A hónap sorszáma = ") or 2)
nap = int(input("A nap sorszáma = ") or 3)
print(f"Azon a napon {hetnapja(honap,nap)} volt.")

print(f"\n6.Feladat")
napnev = input("A nap neve = ") or "szerda"
ora = int(input("Az óra sorszáma = ") or 3)

hianyzasnap = 0

for hianyzas in hianyzasok:
    hianyzasossz = 0
    if hetnapja(hianyzas[1][0],hianyzas[1][1]) == napnev:
        if hianyzas[0][1][ora-1] == "X" or hianyzas[0][1][ora-1] == "I":
                hianyzasnap += 1
    hianyzas.append(hianyzasossz)
    
print(f"Ekkor összesen {hianyzasnap} óra hiányzás történt.")

ids = []

for id in hianyzasok:
    ids.append(id[0][0])

counters = []
voltmar = []

for id in ids:
    counter = 0
    s=[]
    if id not in voltmar:
        voltmar.append(id)
        for hianyzas in hianyzasok:
            if id == hianyzas[0][0]:
                for char in hianyzas[0][1]:
                    if char == "X" or char == "I":
                        counter+=1
        s = [id, counter]
        counters.append(s)
legtobb = []
legtobbnum = 0
legtobbnum += max(counters,key = lambda lista : lista[1])[1]

for k in counters:
    if k[1] == legtobbnum:
        legtobb.append(k[0])

print(f"\n7. feladat\nA legtöbbet hiányzó tanulók: {' '.join(legtobb)}")













