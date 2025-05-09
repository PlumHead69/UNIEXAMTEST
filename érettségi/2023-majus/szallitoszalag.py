with open("szallit.txt") as f:
    prop = f.readline()
    prop = prop.strip().split()
    datas = [line.strip().split() for line in f]

infos = [(int(item[0]),int(item[1]),int(item[2]),int(item[3])) for item in datas]

#2
print(f"2. feladat")
INDEX = int(input("Adja meg, melyik adatsorra kíváncsi! ") or 3)-1
print(f"Honnan: {infos[INDEX][1]} Hova: {infos[INDEX][2]}")

#3

def tav(szalaghossz,indulashelye,erkezeshelye):
    if indulashelye<erkezeshelye:
        szalaghossz = erkezeshelye-indulashelye
    else:
        szalaghossz = 200-indulashelye+erkezeshelye
    return szalaghossz

#4

hosszok = []

for i in range(len(infos)):
    hossz = tav(prop[0],infos[i][1],infos[i][2])
    hosszok.append((i+1,hossz))

max_hossz = max(hosszok, key=lambda lista:lista[1])[1]
max_hosszok = [str(hossz[0])for hossz in hosszok if hossz[1]==max_hossz]
print(f"\n4. feladat\nA legnagyobb távolság: {max_hossz}\nA maximális távolságú szállítások sorszáma: {' '.join(max_hosszok)}")

#5

weight = 0

for info in infos:
    if info[1]>info[2]:
        weight+=info[3]

print(f"\n5. feladat\nA kezdőpont előtt elhaladó rekeszek össztömege: {weight}")

#6
print(f"\n6. feladat")
IDO = int(input("Adja meg a kívánt időpontot! ") or 300)

idoben = []
for i in range(len(infos)):
    if infos[i][1]<infos[i][2] and infos[i][0]<=IDO:
        if (IDO-infos[i][0])/3+infos[i][1]<infos[i][2]:
            idoben.append(str(i+1))
    elif infos[i][1]>infos[i][2] and infos[i][0]<=IDO:
        if (IDO-infos[i][0])/3-(200-infos[i][1])<infos[i][2]:
            idoben.append(str(i+1))
if len(idoben)>0:
    print(f"A szállított rekeszek halmaza: {' '.join(idoben)}")
else:
    print("üres")

#7

k = open("tomeg.txt", "w")

tomegek = {}

for i in range(len(infos)):
    if infos[i][1] not in tomegek:
        tomegek[infos[i][1]] = infos[i][3]
    else:
        tomegek[infos[i][1]] += infos[i][3]

for item, value in tomegek.items():
    k.write(str(item) + " " + str(value)+"\n")

k.close()

