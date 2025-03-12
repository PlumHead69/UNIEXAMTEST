
with open("ip.txt","r") as f:
    datas = [line.strip() for line in f]
    


#2
print(len(datas))

#3 mi a legalacsonyabb IP cim?
print(min(datas))

#4
d=0
g=0
h=0

for data in datas:
    starter = data[:4]
    if "fc" in starter or "fd" in starter:
        h+=1
    
    if "2001:0e" in data:
        g+=1
    
    if "2001:0db8" in data:
        d+=1

print((d,g,h))
    
#5

d = open("sok.txt","w")

for i in range(len(datas)):
    if datas[i].count("0") >= 18:
        d.write(str(i+1) + " " + datas[i] + "\n")    

d.close()

#6

SERIAL_NUMBER = int(input("sorszam: ") or 375)-1

IP = datas[SERIAL_NUMBER]


while ":0" in IP:
    IP = IP.replace(":0",":",)


while "::" in IP:
    IP = IP.replace("::",":0:")

print(IP)

#7

if ":0:0:0:0:0:0:" in IP:
    IP = IP.replace(":0:0:0:0:0:0:","::") 

elif ":0:0:0:0:0:" in IP:
    IP = IP.replace(":0:0:0:0:0:","::") 

elif ":0:0:0:0:" in IP:
    IP = IP.replace(":0:0:0:0:","::") 

elif ":0:0:0:" in IP:
    IP = IP.replace(":0:0:0:","::") 

elif ":0:0:" in IP:
    IP = IP.replace(":0:0:","::",1) 



print(IP)
