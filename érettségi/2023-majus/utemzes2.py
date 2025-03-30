with open("taborok.txt","r") as file:
    datas = [line.strip().split() for line in file]

taborok = [(int(item[0]),int(item[1]),int(item[2]),int(item[3]), item[4], item[5]) for item in datas]

#2
print(f"2. feladat\nAz adatsorok száma: {len(taborok)}\nAz először rögzített tábor témája: {taborok[0][5]}\n Az utoljára rögzített tábor témája: {taborok[-1][5]} ")



#3
print(f"\n3. feladat")

for tabor in taborok:
    if tabor[5] == "zenei":
        print(f"Zenei tábor kezdődik {tabor[0]}. hó {tabor[1]}. napján. ")



#4

nepszeru=0
for tabor in taborok:
    if len(tabor[4])>nepszeru:
        nepszeru=len(tabor[4])

leghosszabb = [(tabor[0], tabor[1], tabor[5]) for tabor in taborok if len(tabor[4])==nepszeru]

print(f"\n4. feladat\nLegnépzserűbbek:\n{leghosszabb}")

#5

def sorszam(honap, nap):
    if honap == 6:
        return nap - 15 
    elif honap == 7:
        return nap + 15
    else:
        return nap + 46
    
#6

print(f"\n6. feladat")
HONAP = int(input("hó:") or 8)
NAP = int(input("nap:") or 1)

c=0

for tabor in taborok:
    if sorszam(tabor[0],tabor[1]) < sorszam(HONAP,NAP) and sorszam(tabor[2],tabor[3]) > sorszam(HONAP,NAP):
        c+=1

print(f"Ekkor éppen {c} tábor tart.")

#7

ID = input("Adja meg egy tanuló betűjelét:") or "L"

jelentkezesek = [tabor for tabor in taborok if ID in tabor[4]]

rendezett=sorted(jelentkezesek, key=lambda lista:(lista[0],lista[1]))

k=open("egytanulo.txt","w")

mehet_e=True
for i in range(len(rendezett)):
    k.write(str(rendezett[i][0])+"."+str(rendezett[i][1])+"-"+str(rendezett[i][2])+"."+str(rendezett[i][3])+". "+rendezett[i][5]+"\n")
    



k.close()







