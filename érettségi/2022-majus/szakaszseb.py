with open("meresek.txt") as f:
    datas = [line.strip().split() for line in f]

meresek = [(item[0],(int(item[1]),int(item[2]),int(item[3]),int(item[4])),(int(item[5]),int(item[6]),int(item[7]),int(item[8]))) for item in datas]

#2
print(f"2. feladat\nA mérés során {len(meresek)} jármű adatait rögzítették.")

#3

before_9=[item for item in meresek if item[2][0]<9]
print(f"\n3. feladat\n9 óra előtt {len(before_9)} jármű haladt el a végponti mérőnél.")

#4

print(f"\n4. feladat")
IDO = input("Adjon meg egy óra és perc értéket!").strip().split() or [8,20]

a = [item for item in meresek if item[1][0]==int(IDO[0]) and item[1][1]==int(IDO[1])]
b = [item for item in meresek if item[1][0]<=int(IDO[0])<=item[2][0] and item[1][1]<=int(IDO[1])<=item[2][1]]
print(f"\ta. A kezdeti méréspontnál elhaladt járművek száma: {len(a)}\n\tb. A forgalomsűrűség: {round(len(b)/10,1)}")

#5

def time(start,end):
    start_time = start[3]/1000+start[2]+start[1]*60+start[0]*3600
    end_time = end[3]/1000+end[2]+end[1]*60+end[0]*3600
    return (end_time-start_time)/3600


max_speeds = [(i,round(10/time(meresek[i][1],meresek[i][2]))) for i in range(len(meresek))]
max_speed = max(max_speeds, key=lambda lista:lista[1])[1]
max_speed_car = [meresek[x[0]] for x in max_speeds if x[1]==max_speed]

print(f"\n5. feladat\nA legnagyobb sebességgel haladó jármű\n\trendszáma {(max_speed_car[0][0])}")
print(f"\tátlagsebessége: {max_speed} km/h")

c=0
for meres in meresek:
    if meres[2][1]<max_speed_car[0][2][1] and  meres[2][2]<max_speed_car[0][2][2] :
        c+=1
print(f"\táltal lehagyott járművek száma: {c}")


#6

KORLAT = 90

meghaladta = [x for x in max_speeds if x[1]>KORLAT] 
print(f"\n6. feladat\nA járművek {round(len(meghaladta)/len(meresek)*100,2)}%-a volt gyorshajtó.")

#7

k = open("buntetes.txt","w")

buntetesek = []
for meres in max_speeds:
    buntetes=0
    if 104<=meres[1]<121:
        buntetes=30000
    elif 121<=meres[1]<136:
        buntetes=45000
    elif 136<=meres[1]<151:
        buntetes=60000
    elif 151<=meres[1]:
        buntetes=200000
    buntetesek.append((meresek[meres[0]][0],meres[1],buntetes))
    


for bunti in buntetesek:
    if bunti[2]!=0:
        k.write(bunti[0] + " " + str(bunti[1]) + " km/h\t" + str(bunti[2]) + "Ft\n")

k.close()






