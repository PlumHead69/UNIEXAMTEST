def ado(sav,alap,arak):

    if alap * arak[sav] >= 10000:
        return alap * arak[sav]
    else:
        return 0

f = open("utca.txt","r")
#{}
utcak = []
arak = {}
betussav = "ABC"
s = f.readline().split()

for i in range(len(s)):
    arak[betussav[i]] = int(s[i])


for line in f:
    utca = line.split()

    s = []

    s.append(int(utca[0]))
    s.append(utca[1])
    s.append(utca[2])
    s.append(utca[3])
    s.append(int(utca[4]))

    utcak.append(s)

f.close()

print(f"2. feladat. A mintában {len(utcak)} telek szerepel.")
adoszam = int(input(f"3. feladat. Egy tulajdonos adószáma: ") or 68396)
vane = False
for utca in utcak:
    if utca[0] == adoszam:
        print(f"{utca[1]} utca {utca[2]}")
        vane = True

if not vane:
    print("Nem szerepel az adatállományban.")

savadok = {
    "A":[0,0],
    "B":[0,0],
    "C":[0,0]
}

for utca in utcak:
    savadok[utca[3]][0]+=1
    savadok[utca[3]][1] += ado(utca[3],utca[4],arak)

for i in range(len(savadok)):
    print(f"{betussav[i]} sávban {savadok[betussav[i]][0]} telek esik, az adó {savadok[betussav[i]][1]} Ft")

utcaado = {}
bajos = []

for utca in utcak:
    if utca[1] not in utcaado:
        utcaado[utca[1]] = utca[3]
    else:
        if utca[3] != utcaado[utca[1]] and utca[1] not in bajos:
            bajos.append(utca[1])

print("6. feladat. A több sávba sorolt utcák:")
for baj in bajos:
    print(baj)

k = open("fizetendo.txt","w")

for i in range(len(utcak)):
    k.write(f"{utcak[i][0]} {ado(utcak[i][3],utcak[i][4],arak)}\n")

k.close()




