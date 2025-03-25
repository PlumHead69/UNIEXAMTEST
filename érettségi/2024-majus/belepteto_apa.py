from datetime import datetime, timedelta


with open(".\\bedat.txt") as file:
    raw = [row.strip().split(' ') for row in file]

data = [ (item[0] , item[1], int(item[2]))  for item in raw ]

#2

print(data[0][1],data[-1][1])

#3

kesok = [ (item[1],item[0]) for item in data if item[1]>"07:50" and  item[1]<"08:15" ]

print (kesok)

#4

menza = [ item for item in data if item[2]==3 ]

print(len(menza))

#5

kolcson_list  = [ item[0] for item in data if item[2]==4 ]

kolcson_set = set ( kolcson_list)

print(len(kolcson_set))

#6

belepo_pre=set()
ujrabelepo=set()

for item in data:
    if item[2]==1 and item[1]<"10:45":
        belepo_pre.add(item[0])
    
    if item[2]==1 and item[1]>"10:50" and item[1]<"11:00" and item[0] in belepo_pre:
        ujrabelepo.add(item[0])

print (ujrabelepo)
# ez nem jó, de nem tudom miért

#7

akciok = [ item[1] for item in data if item[0]=="OELK" ]

ido1=akciok[0].split(':')
ido2=akciok[-1].split(':')

idodiff_ora=int(ido2[0])-int(ido1[0])
idodiff_perc=int(ido2[1])-int(ido1[1])

if idodiff_perc<0 :
    idodiff_ora-=1
    idodiff_perc=60+idodiff_perc

print(idodiff_ora)
print(idodiff_perc)