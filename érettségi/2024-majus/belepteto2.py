with open("bedat.txt") as file:
    datas=[line.strip().split() for line in file]


#2
belep=[]
kilep=[]

for data in datas:
    if data[2]=="1":
        belep.append(data)
    elif data[2]=="2":
        kilep.append(data)

print(f"2. feladat\nAz első tanuló {belep[0][1]}-kor lépett be a főkapun.\nAz utolsó tanuló {kilep[-1][1]}-kor lépett ki a főkapun. \n")


#3

k = open("kesok.txte","w")

for data in datas:
    if "07:50"<data[1]<"08:15":
        k.write(data[1]+" "+data[0]+"\n")

k.close()

#4

ebedelok = 0
for data in datas:
    if data[2]=="3":
        ebedelok+=1
print(f"4. feladat\nA menzán aznap {ebedelok} tanuló ebédelt.\n ")

#5

kolcsonoztek=[]
kolcsonzes=0

for data in datas:
    if data[0] not in kolcsonoztek and data[2]=="4":
        kolcsonoztek.append(data[0])
        kolcsonzes+=1


print(f"5. feladat\nAznap {kolcsonzes} tanuló kölcsönzött a könyvtárban. ")
if kolcsonzes>ebedelok:
    print(f"Többen voltak, mint a menzán.")
else:
    print("Nem voltak többen, mint a menzán.")


#6

diakok=[]
for diak in datas:
    if diak[0] not in diakok:
        diakok.append(diak[0])

diak_belepes=[]
diak_kilepes=[]

for diak in diakok:
    be=0
    ki=0
    for diak_kibe in datas:
        if diak==diak_kibe[0]:
            if diak_kibe[2] =="1":
                be+=1
            elif diak_kibe[2] == "2":
                ki+=1
    diak_belepes.append(be)
    diak_kilepes.append(ki)

kimenok=[]
for i in range(len(diak_belepes)):
    if diak_belepes[i]!=diak_kilepes[i]:
        kimenok.append(diakok[i])

print(f"\n6. feladat\nAz érintett tanulók:")
print(kimenok)
#7
print(f"\n7. feladat")
TANULO_ID = input("Egy tanuló azonosítója=") or "ZOOM"

diak_lista=[]

for data in datas:
    if data[0]== TANULO_ID:
        diak_lista.append(data)

be=str(diak_lista[0][1])
ki=diak_lista[-1][1]


def hour_calc(start,end):
    start_h=start.split(":")[0]
    start_m=start.split(":")[1]
    end_h=end.split(":")[0]
    end_m=end.split(":")[1]    

    ossz_h=int(end_h)-int(start_h)-1
    ossz_m=60-int(start_m)+int(end_m)

    return (ossz_h,ossz_m)

print(f"A tanuló érkezése és távozása között {hour_calc(be,ki)[0]} óra {hour_calc(be,ki)[1]} perc telt el.")




