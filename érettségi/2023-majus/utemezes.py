def sorszam(ho,nap):
    
    if ho == 6:
        return nap - 15 
    elif ho == 7:
        return nap + 15
    else:
        return nap + 46
    
    
    
    
        

def hanytabor(ho,nap,taborok):

    zajlanak = []

    for tabor in taborok:
        #1. típus, ha a tábor ugyanabban a hónapban kezdődik
        if tabor[0] == ho and tabor[1] <= nap:
            zajlanak.append(tabor[5])
            
        #2. típus, ha a tábor hamarabbi hónapban keződik, de tart közben
        elif tabor[2] == ho and tabor[3] >= nap and tabor[0] != tabor[2]: 
            zajlanak.append(tabor[5])

    return len(zajlanak)
   
f = open("taborok.txt","r")

taborok = []
#{}

for line in f:

    s = line.split()
    tabor = []
    tabor.append(int(s[0]))
    tabor.append(int(s[1]))
    tabor.append(int(s[2]))
    tabor.append(int(s[3]))
    tabor.append((s[4]))
    tabor.append((s[5]))

    taborok.append(tabor)
f.close()

print("2. feladat")
print(f"Az adatsorok száma: {len(taborok)}")
print(f"Az először rögzített tábor témája: {taborok[0][5]}")
print(f"Az utoljára rögzített tábor témája: {taborok[-1][5]}\n")

print("3. Feladat")
vane = False
for tabor in taborok:
    if tabor[5] == "zenei":
        print(f"Zenei tábor kezdődik {tabor[0]}.hó {tabor[1]}. napján")
        vane = True
if vane == False:
    print("Nem volt zenei tábor.")

print("\n4. Feladat")
#1. megoldas
members = 0
clipp = [0]
for i in range(len(taborok)):
    if len(taborok[i][4]) > members:
        members=len(taborok[i][4])
        clipp.clear()
        clipp.append(taborok[i])
    elif len(taborok[i][4]) == members:
        clipp.append(taborok[i])


print("Legnépszerűbbek:")
print(f"{clipp[0][0]} {clipp[0][1]} {clipp[0][5]}\n")

#2. megoldas

def mibol(lista):
    return len(lista[4])

#lambda lista : len(lista[4])

#leghosszabb = max(taborok,key = mibol)
leghosszabb = max(taborok,key = lambda lista : len(lista[4]))
print(leghosszabb[0],leghosszabb[1], leghosszabb[5])


print("6. Feladat")
hó = int(input("hó: ") or 8)
nap = int(input("nap: ") or 1)
print(f"Ekkor éppen {hanytabor(hó,nap,taborok)} tábor tart.\n")

print("7. Feladat")
jel = input("Adja meg egy tanuló betűjelét: ") or "L"

jelentkezet = []
for tabor in taborok:
    if jel in tabor[4]:
        jelentkezet.append(tabor)

#1. megoldas
found = False
for nezett in jelentkezet:
    if found:
        break
    for i in range(1,len(jelentkezet)):
        if jelentkezet[i] == nezett:
            continue
        elif nezett[2] == jelentkezet[i][0] and nezett[3] > jelentkezet[i][1]:
            print("Nem mehet el mindegyik táborba.")
            found = True
            break

if not found:
    print("Mehet az összes jelentkezett táborba.")
    
#2. megoldas
def Miszerint(lista):
    return lista[0], lista[1]


rendezett = sorted(jelentkezet,key= lambda lista : (lista[0],lista[1]))


found2 = False
for i in range(1,len(jelentkezet)):
    if (jelentkezet[i][0] == jelentkezet[i-1][2] and jelentkezet[i][1] <= jelentkezet[i-1][3]) or (jelentkezet[i][0] < jelentkezet[i-1][2]):
        found2 = True
        
if found2:
    print("Nem mehet el mindegyik táborba.")
else:
    print("Mehet az összes jelentkezett táborba.")

#3. megoldas

found3 = False
for i in range(1,len(jelentkezet)):
    if sorszam(jelentkezet[i][0],jelentkezet[i][1]) < sorszam(jelentkezet[i-1][2],jelentkezet[i-1][3]):
        found3 = True
        
if found3:
    print("Nem mehet el mindegyik táborba.")
else:
    print("Mehet az összes jelentkezett táborba.")

