with open("jeladas2.txt") as f:
    data = [line.strip().split() for line in f] 

signals = []

for i in range(len(data)):
    item = (data[i][0],int(data[i][1]),int(data[i][2]),int(data[i][3]),i)
    signals.append(item)

#2

print(signals[-1])

#3

first_car_signals = []

for signal in signals:
    if signal[0] == signals[0][0]:
        item = (signal[1],signal[2])
        first_car_signals.append(item)

print(first_car_signals)


#4

h = int(input("óra") or 6)
m = int(input("perc") or 54)

c = 0

for signal in signals:
    if signal[1] == h and signal[2] == m:
        c += 1

print(c)


#5

speed_check = []

max_speed = max(signals, key=lambda lista:lista[3])[3]
print(max_speed)

for signal in signals:
    if signal[3] == max_speed:
        speed_check.append(signal[0])

print(speed_check)

#6


serial_number = input("rendszam") or "ZVJ-638"

def s(starth,startm,endh,endm,v):
    t = endh-starth+(endm-startm)/60
    return t*v


same_car_signals = []

for signal in signals:
    if signal[0] == serial_number:
        same_car_signals.append(signal)

curs = 0.0
for i in range(1,len(same_car_signals)):
    print(f"{same_car_signals[i-1][1]}:{same_car_signals[i-1][2]} {round(curs,1)} km")
    curs += s(same_car_signals[i-1][1],same_car_signals[i-1][2],same_car_signals[i][1],same_car_signals[i][2],same_car_signals[i-1][3])

print(f"{same_car_signals[-1][1]}:{same_car_signals[-1][2]} {round(curs,1)} km")


#7
k = open("ido.txt","w")

all_serial_numbers = []
same_car_signals = []

for signal in signals:
    if signal[0] not in all_serial_numbers:
        all_serial_numbers.append(signal[0])

for serial in all_serial_numbers:
    l = []
    for signal in signals:
        if signal[0] == serial:
            l.append(signal)
    same_car_signals.append(l)

for signal in same_car_signals:
    k.write(str(signal[0][0]) + " " + str(signal[0][1]) + " "  + str(signal[0][2]) + " "  + str(signal[-1][1]) + " "  + str(signal[-1][2]) + "\n")

k.close()
