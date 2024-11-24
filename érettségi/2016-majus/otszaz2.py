def ertek(darabszam):
    if darabszam == 1:
        return 500
    elif darabszam == 2:
        return 950
    elif darabszam >= 3:
        return 950+(darabszam-2)*400

f = open("penztar.txt", "r")

kosarak = []
kosar = {}

for line in f:
    s = line.strip()
    if s != "F":  
        if s not in kosar:
            kosar[s] = 1
        else:
            kosar[s] +=1
    else:
        kosarak.append(kosar)
        kosar = {}

print(f"2. Feladat\nA fizetések száma: {len(kosarak)}")
print(f"3. Feladat\nAz első vásárló {len(kosarak[0])} darab árucikket vásárolt.")

print("\n4. Feladat")
sorszam = int(input("Adja meg egy vásárlás sorszámát!") or 2)
arucikk = input("Adja meg egy árucikk nevét!") or "kefe"
darabszam = int(input("Adja meg a vásárolt darabszámot!") or 2)

arucikkek=[]
ossz=0

for i in range(len(kosarak)):
    for item in kosarak[i]:
        if item == arucikk:
            ossz += 1
            arucikkek.append(i+1)

print(f"\n5. Feladat\nAz első vásárlás sorszáma: {arucikkek[0]}\nAz utolsó vásárlás sorszáma: {arucikkek[-1]}\n{ossz} vásárlás során vettek belőle.")
print(f"\n6. Feladat\n{darabszam} darab vételekor fizetendő: {ertek(darabszam)}")
print(f"\n7. Feladat")

for aru,mennyiseg in kosarak[sorszam-1].items():
    print(f"{mennyiseg} {aru}")

k = open("osszeg.txt","w")

for i in range(len(kosarak)):
    tracker = 0
    for darabsz in kosarak[i].values():
        tracker += ertek(darabsz)
    k.write(str(i+1) + ": " + str(tracker) + "\n")

k.close()
















