helyes_parok = []

for elso in range(100,1000):
    for masodik in range(100,1000):
        if (elso-masodik==100 or masodik-elso==100) and (elso%6==0 and masodik%7==0 or elso%7==0 and masodik%6==0):
            if (masodik,elso) not in helyes_parok:
                helyes_parok.append((elso,masodik))

print(f"Összesen {len(helyes_parok)} lehetséges kombináció van!")

c=0

for a in range(100,1000):
    b = a+100
    if b>1000:
        continue
    if (a%6==0 and b% 7==0) or (a%7==0 and b%6==0):
        c+=1

print(f"Összesen {c} lehetséges kombináció van!")










