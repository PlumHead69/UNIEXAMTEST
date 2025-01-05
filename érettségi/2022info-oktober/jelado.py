import math as m
with open("jel.txt") as f:
    data = [line.strip().split() for line in f] 

signals = []

for i in range(len(data)):
    item = (int(data[i][0]),int(data[i][1]),int(data[i][2]),int(data[i][3]),int(data[i][4]),i+1)
    signals.append(item)

#2

serial_number = int(input("sorszam") or 3)

for signal in signals:
    if signal[5] == serial_number:
        print(f"x={signal[3]} y={signal[4]}")

#3

def passed_sec(first,second):
    return (second[0]-first[0])*3600 + (second[1]-first[1])*60 + second[2]-first[2]

#4

def to_hours(secs):
    hours = round(secs/3600)-1
    secs-= hours*3600
    minutes = round(secs/60)-1
    secs-= minutes*60
    seconds = secs
    return (hours,minutes,seconds)

secs = passed_sec(signals[0],signals[-1])
print(to_hours(secs))

#5

max_x = max(signals,key=lambda lista:lista[3])[3]
max_y = max(signals,key=lambda lista:lista[4])[4]

min_x = min(signals,key=lambda lista:lista[3])[3]
min_y = min(signals,key=lambda lista:lista[4])[4]
print(f"Bal alsó: {min_x} {min_y}, Jobb felső: {max_x} {max_y}")


#6

cur_distance= 0.000

for i in range(len(signals)-1):
    cur_distance += round(m.sqrt((signals[i][3]-signals[i+1][3])**2+(signals[i][4]-signals[i+1][4])**2),3)
print(cur_distance)

#7


for i in range(len(signals)-1):
    time = 0
    distance = 0
    if passed_sec(signals[i],signals[i+1]) > 5*60:
        time += round(passed_sec(signals[i],signals[i+1])/5*60,0)
    elif round(m.sqrt((signals[i][3]-signals[i+1][3])**2+(signals[i][4]-signals[i+1][4])**2),3) > 10:
        distance += round(m.sqrt((signals[i][3]-signals[i+1][3])**2+(signals[i][4]-signals[i+1][4])**2)/10,0)
    if time >= distance:
        print(f"{signals[i][0]} {signals[i][1]} {signals[i][2]} időeltérés {time}")
    elif distance > time:
        print(f"{signals[i][0]} {signals[i][1]} {signals[i][2]} koordinata-eltérés {distance}")








