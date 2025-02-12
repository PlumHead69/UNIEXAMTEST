def mpbe(ora,perc,mp):
    osszmp = 0

    osszmp += ora * 3600
    osszmp += perc * 60
    osszmp += mp

    return osszmp

with open("hivas.txt","r") as file:
    datas = [line.strip().split() for line in file]

hivasok = []

for i in range(len(datas)):
    item1 = (int(datas[i][0]),int(datas[i][1]),int(datas[i][2]))
    item2 = (int(datas[i][3]),int(datas[i][4]),int(datas[i][5]))

    hivasok.append((item1,item2))

#3

stat={}

for i in range(len(hivasok)):
    stat[hivasok[i][0][0]]=0

for i in range(len(hivasok)):
    stat[hivasok[i][0][0]]+=1

keys=list(stat.keys())
values=list(stat.values())

for i in range(len(keys)):
    if values[i] > 0:
        print(f"{keys[i]} ora {values[i]} hivasok")


#4

leghosszabb=0
sorszam=0

for i in range(len(hivasok)):
    timecalc = mpbe(hivasok[i][1][0],hivasok[i][1][1],hivasok[i][1][2]) - mpbe(hivasok[i][0][0],hivasok[i][0][1],hivasok[i][0][2]) 
    if timecalc > leghosszabb:
        leghosszabb = timecalc
        sorszam = i+1
print(f"A leghosszabb ideig vonalban levo hivo {sorszam} sorban szerepel, a hivas hossza: {leghosszabb} masodperc. ")


#5

ora,perc,mp = input("Adjon meg egy idopontot! (ora perc masodperc):").split()
varakozas = (int(ora),int(perc),int(mp))

kovetkezo=0

def hivasban(hivo,keresett):
    if hivo[0][0] <= keresett[0] <= hivo[1][0] and hivo[0][1] <= keresett[1] <= hivo[1][1] and hivo[0][2] <= keresett[2] <= hivo[1][2]:
        return True


varakozok = 0
for i in range(len(hivasok)):
    if hivasban(hivasok[i],varakozas):
        kovetkezo = i+1
for i in range(len(hivasok)):
    if mpbe(hivasok[i][1][0],hivasok[i][1][1],hivasok[i][1][2]) > mpbe(hivasok[kovetkezo][1][0],hivasok[kovetkezo][1][1],hivasok[kovetkezo][1][2]):
print(kovetkezo)

