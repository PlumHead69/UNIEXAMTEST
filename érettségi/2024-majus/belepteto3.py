with open("bedat.txt") as f:
    datas = [line.strip().split() for line in f]

infos = [(item[0],item[1].split(":"),int(item[2])) for item in datas]

#2
print(f"2. feladat\nAZ első tanuló {infos[0][1][0]}:{infos[0][1][1]}-kor lépett be a főkapun.\nAz utolsó tanuló {infos[-1][1][0]}:{infos[-1][1][1]}-kor lépett ki a főkapun.")

#3

k = open("kesok.txt","w")


for info in infos:
    if (info[1][0]=="07" and info[1][1]>"50") or (info[1][0]=="08" and info[1][1]<"15"):
        k.write(str(info[1][0]) + ":" + str(info[1][1]) + " " + info[0]+"\n")
k.close()

#4

menza = [info for info in infos if info[2]==3]
print(f"\n4. feladat\nA menzán aznap {len(menza)} tanuló ebédelt.")

#5
konyv=[]

for info in infos:
    if info[2]==4 and info[0] not in konyv:
        konyv.append(info[0])


print(f"\n5. feladat\nAznap {len(konyv)} tanuló kölcsönzött a könyvtárban.")

if len(konyv)>len(menza):
    print("Többen voltak, mint a menzán.")
elif len(konyv)<len(menza):
    print("Nem voltak többen, mint a menzán.")


#6

atjaras = {}

for info in infos:
    if info[0] not in atjaras:
        atjaras[info[0]] = 0
    elif info[2] == 1:
        atjaras[info[0]] +=1
    elif info[2] == 2:
        atjaras[info[0]] -=1

csalok=[]

for key,value in atjaras.items():
    if value==0:
        csalok.append(key)

print(f"\n6. feladat\nAz érintett tanulók:\n{' '.join(csalok)}")

#7

print(f"\n7. feladat")

ID = input("Egy tanuló azonosítója= ") or "ZOOM"

def time(start,end):
    if start[1]<=end[1]:
        spent_time = [int(end[0])-int(start[0]),int(end[1])-int(start[1])]
    else:
        spent_time = [int(end[0])-int(start[0])-1,int(end[1])-int(start[1])+60]
    return spent_time

tanulo_atjaras = [info[1] for info in infos if info[0]==ID]
print(f"A tanuló érkezése és távozása között {time(tanulo_atjaras[0],tanulo_atjaras[-1])[0]} óra {time(tanulo_atjaras[0],tanulo_atjaras[-1])[1]} perc telt el.")
