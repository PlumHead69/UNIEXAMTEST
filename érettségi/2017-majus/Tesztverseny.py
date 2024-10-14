def Helyes(jovalaszok,versenyzovalaszok):

    eredmeny =""

    for i in range(len(jovalaszok)):
        if versenyzovalaszok[i] == jovalaszok[i]:
            eredmeny += "+"
        else:
            eredmeny +=" "

    return eredmeny

def Jovalaszokdb(sorszam,versenyzok,jovalaszok):

    helyesvalasz = 0

    for ertek in versenyzok.values():
        if ertek[sorszam-1] == jovalaszok[sorszam-1]:
            helyesvalasz += 1

    return helyesvalasz

def Pontszamlalo(valaszok, jovalaszok):

    pont = 0
    pontok = [3,3,3,3,3,4,4,4,4,4,5,5,5,6]

    for i in range(len(jovalaszok)):
        if valaszok[i] == jovalaszok[i]: 
            pont += pontok[i]

    return pont

def Dobogosok(pontos):
    
    dobogosok = []

    for i in range(len(pontos)):
        helyezet = []
        if len(dobogosok) < 1:
            helyezet = [pontos[i], 1]
            dobogosok.append(helyezet)
            continue

        if dobogosok[i-1][0][1] == pontos[i][1]:
            helyezet = [pontos[i], dobogosok[i-1][1]]
            dobogosok.append(helyezet)
        else:
            helyezet = [pontos[i], dobogosok[i-1][1]+1]
            dobogosok.append(helyezet)
            
        if dobogosok[-1][1] > 3:
            dobogosok.pop(-1)
            break

    return dobogosok
        
        

    

f = open("valaszok.txt","r")

jovalaszok = f.readline().strip()
versenyzok = {}

for line in f:
    s = line.strip().split()
    versenyzok[s[0]] = s[1]

f.close()

print("1. Feladat: Az adatok beolvasása\n")
print(f"2. Feladat: A vetélkedőn {len(versenyzok)} versenyző indult.\n")
azonkeres = input("3. feladat: A versenyző azonosítója = ") or "AB123"
print(f"{versenyzok[azonkeres]}\t(a versenyző válasza)\n")
print(f"4.Feladat: \n{jovalaszok}\t(a helyes megoldás)")
print(f"{Helyes(jovalaszok,versenyzok[azonkeres])}\t(a versenyző helyes válaszai)\n")
sorszam = int(input("5. feladat: A feladat sorszáma = ") or "10")
helyesvalasz = Jovalaszokdb(sorszam,versenyzok,jovalaszok)
print(f"A feladatra {helyesvalasz} fő, a versenyzők {round(helyesvalasz/len(versenyzok) * 100,2)}%-a adott helyes választ.\n")

print("6. feladat: A versenyzők pontszámának meghatározása\n")
pontos = []

for kulcs, ertek in versenyzok.items():
    pontszam = Pontszamlalo(ertek,jovalaszok)
    pontos.append([kulcs,pontszam])


#Faljba írás
k = open("pontok.txt","w")

for versenyzo in pontos:
    k.write(f"{versenyzo}\n")
    

#Rendezni kell a pontost
def Rendezes(kl):
    return kl[1]

pontos.sort(key = Rendezes, reverse = True)

print("7. feladat: A verseny legjobbjai:")
dobogos = Dobogosok(pontos)
for i in range(len(dobogos)):
    print(f"{dobogos[i][1]}.díj ({dobogos[i][0][1]} pont) : {dobogos[i][0][0]}")

