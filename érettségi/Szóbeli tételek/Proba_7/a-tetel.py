import random as r

szekek = {}
tf = [0,1]

for i in range(1,33):
    r_int = r.choice(tf)
    szekek[i]=r_int

sor=[]
for key,value in szekek.items():
    if value==0:
        sor.append("x")
    else:
        sor.append(str(key))
    
    if len(sor)==4:
        print(f"{sor[0]} {sor[1]}\t{sor[3]} {sor[2]}")
        sor=[]   
    
        

