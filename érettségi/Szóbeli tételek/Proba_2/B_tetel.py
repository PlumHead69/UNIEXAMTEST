h = [-2, -3, 6, 3, -3, -2, 1,-1, 1,-2]

fagyos_napok = 0
sorozat_e=[]


for i in range(1,len(h)):
    if h[i-1]<0 and h[i]>=0:
        fagyos_napok+=1

if h[-1]<0:
    fagyos_napok+=1
    
print(fagyos_napok)

"""
h = [-2, -3, 6, 3, -3, -2, 1,-1, 1,-2]

fagyos_napok = 0
sorozat_e=[]

ciklus i=2-től hossz(h)
    ha h[i-1]<0 és h[i]>=0:
        fagyos_napok+=1
    elágazás vége
ciklus vége

ha h[-1]<0:
    fagyos_napok+=1
elágazás vége

ki: fagyos_napok

"""


