def mpbe(ido):
    osszmp = 0

    osszmp += ido[0] * 3600
    osszmp += ido[1] * 60
    osszmp += ido[2]

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
    timecalc = mpbe(hivasok[i][1]) - mpbe(hivasok[i][0]) 
    if timecalc > leghosszabb:
        leghosszabb = timecalc
        sorszam = i+1
print(f"A leghosszabb ideig vonalban levo hivo {sorszam} sorban szerepel, a hivas hossza: {leghosszabb} masodperc. ")


#5

ora,perc,mp = input("Adjon meg egy idopontot! (ora perc masodperc):").split()
varakozas = (int(ora),int(perc),int(mp))

kovetkezo=0
varakozok=0

keresett_ido = mpbe(varakozas)

for i in range(len(hivasok)):
    for ido in range(mpbe(hivasok[i][0]),mpbe(hivasok[i][1])):
        if ido == keresett_ido:
            kovetkezo=i+1

idozona=[]
for ido in range(mpbe(hivasok[kovetkezo-1][0]),mpbe(hivasok[kovetkezo-1][1])):
    idozona.append(ido)

for i in range(len(hivasok)):
    if mpbe(hivasok[i][0]) in idozona:
        varakozok+=1

print(kovetkezo)
print(varakozok)

