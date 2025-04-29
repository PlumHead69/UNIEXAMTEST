with open("jeladas.txt","r") as file:
    datas = [line.strip().split() for line in file]

signals = [(item[0],int(item[1]),int(item[2]),int(item[3])) for item in datas]

#2
print(f"2. feladat\nAz utolsó jeladás időpontja {signals[-1][1]}:{signals[-1][2]}, a jármű rendszáma {signals[-1][0]}")

#3

elso_auto = [(str(signal[1]) + ":" + str(signal[2]))for signal in signals if signal[0]==signals[0][0]]
print(f"\n3. feladat\nAz első jármű: {signals[0]}\nJeladásainak időpontjai: {' '.join(elso_auto)}")

#4
print(f"\n4. feladat")
ORA = int(input("Kérem, adja meg az orat: ") or 6)
PERC = int(input("Kérem, adja meg a percet: ") or 54)

jeladasok_szama = [signal for signal in signals if signal[1]==ORA and signal[2]==PERC] 

print(f"A jeladasok szama: {len(jeladasok_szama)}")


#5

MAX_SPEED = max(signals, key=lambda lista:lista[3])[3]
max_speed_cars = [signal[0] for signal in signals if signal[3]==MAX_SPEED]

print(f"\n5. feladat\nA legnagyobb sebesség km/h: {MAX_SPEED}\nA járművek: {' '.join(max_speed_cars)}")

#6

def time_calc(first, second):
    if first[0]==second[0]:
        return second[1]-first[1]
    else:
        return second[1]+60-first[1]


print(f"\n6. feladat")
RENDSZAM= input("Kerem adja meg a rendszamot:") or "ZVJ-638"

chosen_car = [signal for signal in signals if signal[0]==RENDSZAM]

s=0.0
for i in range(len(chosen_car)):
    if i==0:
        print(str(chosen_car[i][1])+":"+str(chosen_car[i][2]) +" "+ str(s) +"km")
    else:
        s+= round(chosen_car[i-1][3]*(time_calc((chosen_car[i-1][1],chosen_car[i-1][2]),(chosen_car[i][1],chosen_car[i][2]))/60),1)
        print(str(chosen_car[i][1])+":"+str(chosen_car[i][2]) +" "+ str(s) + "km")


#7

k=open("ido.txt","w")

rendszamok = {}
for signal in signals:
    if signal[0] not in rendszamok:
        rendszamok[signal[0]] = (str(signal[1])+" "+str(signal[2]),"0")
    else:
        rendszamok[signal[0]] = (rendszamok[signal[0]][0],str(signal[1])+" "+str(signal[2]))

for value,key in rendszamok.items():
    k.write(value +" "+key[0] +" "+ key[1] + "\n")

k.close()










