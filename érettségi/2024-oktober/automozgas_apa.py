with open(".\\jeladas.txt") as file:
    raw = [row.strip().split('\t') for row in file]

data = [ (item[0],int(item[1]),int(item[2]),int(item[3]))  for item in raw ]


def jelido(x):
    return int(str(x[1])+str(x[2]))

#2

utolso_jel = max(data, key=jelido)
print(utolso_jel[0:3])

#3

print(data[1][0])

idopontok = [ str(item[1])+":"+str(item[2]) for item in data if item[0]==data[1][0] ]

print (idopontok)

#4

ora = 6
perc = 54

idopontok = [ item for item in data if item[1]==ora and item[2]==perc  ]

print(len(idopontok))

#5

def seb(x):
    return int(x[3])

max_seb = max(data, key=seb)[3]

autok = [ item[0] for item in data if item[3]==max_seb  ]

print(max_seb)

print(autok)

#6

rendszam = 'ZVJ-638'

prev_item = [ rendszam,0,0,0]
s=0

for item in data:
    if item[0]==rendszam:
        # S=v*t
        s=s+prev_item[3]*((item[1]-prev_item[1])+(item[2]-prev_item[2])/60)
        prev_item=item
        print (str(item[1])+":"+str(item[2]),round(s,1))



#7

ido={}

for item in data:
    if not(item[0] in ido):
        ido[item[0]]=(str(item[1])+":"+str(item[2]),'0')
    else:
        ido[item[0]]=(ido[item[0]][0],str(item[1])+":"+str(item[2]))
        

print(ido)