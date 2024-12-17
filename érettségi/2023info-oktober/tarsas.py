f = open("dobasok.txt","r")

dobasok = []

for line in f:
    dobasok = line.split()
f.close()

k = open("osvenyek.txt","r")

osvenyek = []

for line in k:
    s = []
    for char in line.strip():
        s.append(char)
    osvenyek.append(s)
k.close()

#{}

print(f"2. Feladat\nA dobások száma: {len(dobasok)}\nAz ösvények száma: {len(osvenyek)}")

leghosszabb = {}

for i in range(len(osvenyek)):
    num = len(osvenyek[i])
    leghosszabb[num] = i

print(f"\n3. Feladat\nAz egyik leghosszabb a(z) {leghosszabb[max(leghosszabb)]+1}. ösvény, hossza: {max(leghosszabb)}")

print("\n4. Feladat")
sorszam = int(input("Adja meg egy ösvény sorszámát!") or 9) -1
jatekosok = int(input("Adja meg a játékosok számát!") or 5)


tartalom = {'M':0,'V':0,'E':0}

for char in osvenyek[sorszam]:
    tartalom[char] += 1

print(f"\n5. Feladat")
for betu,darab in tartalom.items():
    if darab > 0:
        print(f"{betu}: {darab} darab")

h = open("kulonleges.txt","w")

for i in range(len(osvenyek[sorszam])):
    if osvenyek[sorszam][i] == "E" or osvenyek[sorszam][i] == "V":
        h.write(str(i+1) + "\t" + osvenyek[sorszam][i] + "\n")

h.close()

jatekosokd = {}
for i in range(1,jatekosok+1):
    jatekosokd[i] = 0
print(jatekosokd)


nyertesek = []

counter = 1
korbef = False
korok = 0

for dobas in dobasok:
    if counter < jatekosok + 1:
        jatekosokd[counter] += int(dobas)
        counter += 1 
    else:
        jatekosokd[1] += int(dobas)
        counter = 2
        korok += 1
        if korbef == True:
            break
    for place,score in jatekosokd.items():
        if score >= len(osvenyek[sorszam]):
            korbef = True
            if place not in nyertesek:
                nyertesek.append(place)
    

print(f"\n7. Feladat\nA játék a(z) {korok}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: {nyertesek[0]}")

jatekosokd2 = {}
for i in range(1,jatekosok+1):
    jatekosokd2[i] = 0
print(jatekosokd2)

nyertesek2 = []
counter2 = 1
korbef2 = False



print(len(osvenyek[sorszam])) 
for dobas in dobasok:
    if counter2 < len(jatekosokd2)+1:
        curpos = list(jatekosokd2.values())[counter2-1] 

        if curpos >= len(osvenyek[sorszam]):
            nyertesek.append(counter2)
            korbef2 = True
            continue
        else:
            if osvenyek[sorszam][curpos + int(dobas)] == "M":
                jatekosokd2[counter2] += int(dobas)
            elif osvenyek[sorszam][curpos + int(dobas)] == "E":
                jatekosokd2[counter2] += int(dobas) * 2
            
        # V egyszeruen nem adunk hozza a lepesekhez mert ugyis visszamenne
           
        counter2 += 1

    else:
        if korbef2 == True:
            break
        curpos = list(jatekosokd2.values())[0] 

        if osvenyek[sorszam][curpos + int(dobas)] == "M":
            jatekosokd2[1] += int(dobas)
        elif osvenyek[sorszam][curpos + int(dobas)] == "E":
            jatekosokd2[1] += int(dobas) * 2
        counter2 = 2
        

    for place,score in jatekosokd2.items():
        if score >= len(osvenyek[sorszam]):
            korbef2 = True
            if place not in nyertesek2:
                nyertesek2.append(place)
    print(jatekosokd2)
   
print(nyertesek2)











