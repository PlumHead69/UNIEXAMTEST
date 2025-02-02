with open("veetel.txt","r") as file:
    datas = [line.strip().split() for line in file]

signals=[]

for i in range(0,len(datas),2):
    signals.append(((int(datas[i][0]),int(datas[i][1])),(datas[i+1])))

#2

print(f"első: {signals[0][0][1]}")
print(f"utolsó: {signals[-1][0][1]}")

#3

for signal in signals:
    for message in signal[1]:
        if "farkas" in message:
            print(f"{signal[0][0]}.nap {signal[0][1]}. emberke")

#4

stat = {}

for i in range(len(signals)):
    stat[signals[i][0][0]]=0

for i in range(len(signals)):
    stat[signals[i][0][0]]+=1

for i in sorted(stat):
    print((i, stat[i]))

#5









