with open("jeladas.txt") as file:
    datas=[line.strip().split() for line in file]

signals=[]

for i in range(len(datas)):
    item = (datas[i][0],datas[i][1],datas[i][2],int(datas[i][3]))
    signals.append(item)

#2
print(f"2. feladat:\nAz utolsó jeladás időpontja {signals[-1][1]}:{signals[-1][2]}, a jármű rendszáma {signals[-1][0]}")




#3
FIRST_CAR = signals[0][0]
first_car_list=[]

for car in signals:
    if car[0]==FIRST_CAR:
        first_car_list.append((car[1],car[2]))

edited = []
for item in first_car_list:
    s = ":".join(item)
    edited.append(s)

print(f"\n3. feladat\nAz első jármű: {FIRST_CAR}")
print("Jeladásainak időpontjai:", " ".join(edited))




#4
print(f"\n4. feladat")
ora=int(input("Kérem, adja meg az órát:") or 6)
perc=int(input("Kérem, adja meg a percet:") or 54)

counter=0
for time in signals:
    if int(time[1])==ora and int(time[2])==perc:
        counter+=1
print(f"A jeladások száma: {counter}")




#5
FASTEST = max(signals, key=lambda lista:lista[3])[3]

fastest_cars=[]

for car in signals:
    if car[3]==FASTEST:
        fastest_cars.append(car[0])

print(f"\n5. feladat\nA legnagyobb sebesség km/h: {FASTEST}")
print("A járművek:"," ".join(fastest_cars))



#6
print(f"\n6. feladat:")
CAR_SIGN = input("Kérem, adja meg a rendszámot:") or "ZVJ-638"

chosen_car_list=[]
for car in signals:
    if car[0]==CAR_SIGN:
        chosen_car_list.append(car)

print(chosen_car_list)

cur_distance=0
for i in range(len(chosen_car_list)):
    if chosen_car_list[i][1]<chosen_car_list[i+1][1]:
        minute = 60-chosen_car_list[i][2]+chosen_car_list[i][1]
    cur_distance+=chosen_car_list[i][3]/













#7
k=open("ido.txt","w")

car_sings=[]

for car_sing in signals:
    car_sings.append(car_sing[0])
car_sings= set(car_sings)


all_car_signals_sorted=[]

for sign in car_sings:
    s=[]
    for car in signals:
        if car[0]==sign:
            s.append(car)
    all_car_signals_sorted.append(s)

car_sings=list(car_sings)
for i in range(len(car_sings)):
    k.write(car_sings[i] + " "+all_car_signals_sorted[i][0][1]+" "+all_car_signals_sorted[i][0][2]+" "+all_car_signals_sorted[i][-1][1]+" "+all_car_signals_sorted[i][-1][2]+"\n")

k.close()




