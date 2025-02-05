
with open("ip.txt","r") as f:
    datas = [line.strip() for line in f]
    


#2
print(len(datas))

#3 mi a legalacsonyabb IP cim?

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

SERIAL_NUMBER = int(input("sorszam: ") or 10)-1

def cookie_cutter(IP):
    return IP.split(":")

print(cookie_cutter(datas[SERIAL_NUMBER]))





def first_short(IP):
    cutted = cookie_cutter(IP)
    newIP=[]
    for piece in cutted:
        if piece.count("0")==4:
            newIP.append(piece.replace("0000","0")) 
        
        elif piece.count("0")>4:
            if piece[0]=="0":
                for i in range(1,len(piece)):
                    if piece[i]=="0" and piece[i-1]!="0":
                        piece[i].replace("0","")
            newIP.append(piece)
    return newIP

                




print(datas[SERIAL_NUMBER])
print(first_short(datas[SERIAL_NUMBER]))











