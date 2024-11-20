f = open("bedat.txt","r")

belepsek = []

for line in f:
    s=[]
    k = line.split()
    s.append(k[0])
    time = k[1].split(":")
    s.append(time)
    s.append(int(k[2]))
    belepsek.append(s)
f.close()

ki = []
be = []
for belepes in belepsek:
    if belepes[2] == 1:
        be.append(belepes)
    elif belepes[2] == 2:
        ki.append(belepes)
print(f"2. Feladat\nAz első tanuló {':'.join(be[0][1])}-kor lépett be a főkapun.\nAz utolsó tanuló {':'.join(ki[-1][1])}-kor lépett ki a főkapun.\n")

l = open("kesok.txt","w")
kesok = []
for belepes in belepsek:
    if belepes[1][0] == "07" and belepes[1][1] > "50" or belepes[1][0] == "08" and belepes[1][1] < "15":
        kesok.append(belepes)
for keso in kesok:
    l.write(":".join(keso[1])+" "+keso[0]+"\n")
l.close()

evok = 0
for evo in belepsek:
    if evo[2] == 3:
        evok+=1
print(f"4. Feladat\nA menzán aznap {evok} tanuló ebédelt.\n")

kolcsonzok = []
for kolcsonzo in belepsek:
    if kolcsonzo[2] == 4 and kolcsonzo[0] not in kolcsonzok:
        kolcsonzok.append(kolcsonzo[0])
print(f"5.Feladat\nAznap {len(kolcsonzok)} tanuló kölcsönzött a könyvtárban.")
if evok < len(kolcsonzok):
    print("Többen voltak, mint a menzán.")
else:
    print("Nem voltak többen, mint a menzán.")

be0 = []
kesok = []
for belep in be:
    if belep[1][0] < "10":
        be0.append(belep[0])
for keso in belepsek:
    if keso[0] in be0 and keso[1][0] == "10"and keso[1][1] >= "50" and keso[2] == 1:
        kesok.append(keso[0])
print(kesok)
print(be0)























