with open(".\\naplo.txt") as file:
    nyersadat = [row.strip().split(' ') for row in file]

datum=[]
adat=[]

for i in range(len(nyersadat)):
    if(nyersadat[i][0]=='#'):
        datum=nyersadat[i]
    else:
        adat.append(datum+nyersadat[i])

igazolt = sum([x[5].count('X') for x in adat])

print(igazolt)

igazolatlan = sum([x[5].count('I') for x in adat])

print(igazolatlan)

def hetnapja(s_honap, s_nap):
    honap=int(s_honap)
    nap=int(s_nap)
    NAPNEV = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok","pentek", "szombat" ]
    NAPSZAM = [ 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335 ]
    napsorszam = (NAPSZAM[honap-1]+nap) % 7
    return NAPNEV[napsorszam]

print(hetnapja(2,3))

NAP="szerda"
ORA=3

hianyzasok = [x for x in adat if hetnapja(x[1],x[2])==NAP and ( x[5][ORA-1]=="X" or x[5][ORA-1]=="I" )]

print(len(hianyzasok))

stat={}

for i in range(len(adat)):
    stat[adat[i][3]+adat[i][4]]=0

for i in range(len(adat)):
    stat[adat[i][3]+adat[i][4]]+=adat[i][5].count("I")
    stat[adat[i][3]+adat[i][4]]+=adat[i][5].count("X")

print( [key  for (key, value) in stat.items() if value == max(stat.values())] )