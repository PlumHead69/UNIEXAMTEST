with open("felajanlas.txt","r") as file:
    all_spots = int(file.readline())
    datas = [line.strip().split() for line in file]

agyasok = [(int(item[0]),int(item[1]),item[2] )for item in datas]

#2

print(f"2. feladat\nA felajanlasok szama: {len(agyasok)}")

#3

mindket_oldal = [str(i+1) for i in range(len(agyasok)) if agyasok[i][0]>agyasok[i][1]]
print(f"\n3. feladat\nA bejárat mindkét oldalán ültetők: {" ".join(mindket_oldal)}")


#4

print(f"\n4. feladat")
SORSZAM = int(input("Adja meg az agyas sorszamat: ") or 100) 

counter = [agyas for agyas in agyasok if (agyas[0]<agyas[1] and agyas[0]<=SORSZAM<=agyas[1]) or (agyas[0]>agyas[1] and agyas[1]>SORSZAM>agyas[0])]

ultetes=False
if len(counter)!=0:
    print(f"A felajanlok szama: {len(counter)}")
    ultetes=True
else:
    print("Ezt az agyast nem ultetik be")

if ultetes==True:
    print(f"A virágágyás színe, ha csak az első ültet: {counter[0][2]}")
    szinek = [item[2] for item in counter]
    szinek = set(szinek)
    print(f"A virágágyás színei: {" ".join(szinek)}")


#5


hianyok = [i for i in range(1,all_spots)]
ajanlatok = 0

for agyas in agyasok:
    if agyas[0]<agyas[1]:
        ajanlatok+=agyas[1]-agyas[0]
        for i in range(agyas[0],agyas[1]):
            if i in hianyok:
                hianyok.remove(i)
    else:
        ajanlatok+= all_spots-agyas[0] + agyas[1]
        for i in range(agyas[0],all_spots):
            if i in hianyok:
                hianyok.remove(i)
        for i in range(1,agyas[1]):
            if i in hianyok:
                hianyok.remove(i)

print(f"\n5. feladat")
if ajanlatok==all_spots:
    print("Minden ágyás beültetésére van jelentkező.")
elif len(hianyok)!=0 and ajanlatok>all_spots:
    print("Átszervezéssel megoldható a beültetés.")
elif len(hianyok)!=0 and ajanlatok<all_spots:
    print("A beültetés nem oldható meg.")

#6

def oldal_valtas(tuple):
    nums = []
    if tuple[0] > tuple[1]:
        for i in range(1,tuple[1]+1):
            nums.append(i)
        for i in range(tuple[0],all_spots+1):
            nums.append(i)
    else:
        for i in range(tuple[0],tuple[1]):
            nums.append(i)
    return nums



k = open("szinek.txt","w")

voltmar = []
for i in range(1,all_spots):
    if i not in hianyok:
        for ajanlat in range(len(agyasok)):
            if i in oldal_valtas(agyasok[ajanlat]) and i not in voltmar:
                k.write(agyasok[ajanlat][2] + " "+ str(ajanlat+1) + "\n")
                voltmar.append(i)
    else:
        k.write("# 0\n" )

k.close()