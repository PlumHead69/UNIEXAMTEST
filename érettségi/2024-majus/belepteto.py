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

print("\n6. Feladat")

allstudents = []
studentinfo = []
kesok = []

for student in belepsek:
    if student[0] not in allstudents:
        allstudents.append(student[0])

for student in allstudents:
    belep = 0
    kilep = 0
    belepesek = []
    kilepesek = []
    s = []
    for studentaction in belepsek:
        if studentaction[0] == student:
            if studentaction[2] == 1:
                belep +=1
                belepesek.append(studentaction[1])
            elif studentaction[2] == 2:
                kilep +=1 
                kilepesek.append(studentaction[1])
    s.append(student)
    s.append(belep)
    s.append(kilep)
    s.append(belepesek)
    s.append(kilepesek)
    studentinfo.append(s)

for keso in studentinfo:
    if keso[1] > keso[2]:
        kesok.append(keso[0])
print("Az érintett tanulók:")
print(" ".join(kesok))

print("\n7. Feladat")
tanulo = input("Egy tanuló azonosítója= ") or "ZOOM"

for student in studentinfo:
    if student[0] == tanulo:
        belep = student[3][0]
        kilep = student[4][-1]
        
        if belep[1] < kilep[1]:
            timespentminute =int(kilep[1]) - int(belep[1])
            timespenthour = int(kilep[0]) - int(belep[0])
        else:
            timespentminute =int(kilep[1]) + 60 - int(belep[1])
            timespenthour = int(kilep[0]) - int(belep[0]) -1
        print(f"A tanuló érkezése és távozása között {timespenthour} óra {timespentminute} perc telt el.")