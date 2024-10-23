def sorszam(hó,nap):
    
    ido = [hó,nap]
    days = []

    for day in range(16,32):
        pack = [6]
        pack.append(day)
        days.append(pack)
    for day in range(1,31):
        pack = [7]
        pack.append(day)
        days.append(pack)
    for day in range(1,32):
        pack = [8]
        pack.append(day)
        days.append(pack)

    
    for i in range(len(days)):
        if days[i] == ido:
            return i+1
        
    a = "Helytelen adat"        
    return(a)

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
print(jelentkezet)





