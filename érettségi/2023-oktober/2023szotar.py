def Ossz(orders):

    return len(orders)

def AdottNap(orders,chosenday):

    counter = 0
    for order in orders:
        if order['nap'] == chosenday:
            counter += 1
    return counter


def NoadCity(orders):

    days = []
    for i in range(1,31):
        days.append(i)

    for order in orders:
        if order['reklam'] == "NR" and order['nap'] in days:
            days.remove(order['nap'])
            
    return len(days)

def Biggest(orders):

    dblist = []
    
    for order in orders:
        dblist.append(order['db'])

    biggest = max(dblist)
    
    for order in orders:
        if order['db'] == biggest:
            return [biggest, order['nap']]

def Osszes(orders,reklam,nap,bool,end):

    
    counter = 0

    if bool == False:
        for order in orders:
            if order['reklam'] == reklam and order['nap'] == nap:
                counter += order['db']
    

    else:
        day = []
        for i in range(nap,end):
            day.append(i)

        for order in orders: 
            if order['reklam'] == reklam and order['nap'] in day:
                counter += 1
                

    return counter


f = open("rendel.txt", "r")

orders = []

for line in f:
    s = line.strip().split()
    sd = {}
    sd['nap'] = int(s[0])
    sd['reklam'] = s[1]
    sd['db'] = int(s[2])
    orders.append(sd)

print("2. Feladat")
print(f"A rendelések száma: {Ossz(orders)}")

print("\n" + "3. Feladat")
chosenday = input("Kérem, adjon meg egy napot: ")
print(f"rendelések száma az adott napon: {AdottNap(orders,int(chosenday))}")

print("\n" + "4. Feladat")
print(f"{NoadCity(orders)} nap nem volt a reklámban nem érintett városból rendelés")

print("\n" + "5. Feladat")
print(f"A legnagyobb darabszám: {Biggest(orders)[0]}, a rendelés napja: {Biggest(orders)[1]}")

print("\n" + "7. Feladat")
print(f"A rendelt termékek darabszáma a 21. napon PL: {Osszes(orders,'PL',21,False,21)} TV: {Osszes(orders,'TV',21,False,21)} NR: {Osszes(orders,'NR',21,False,21)}")

print("\n" + "8. Feladat:")
print(f"Napok   1..10   11..20  20..30")
print(f"PL      {Osszes(orders,'PL',0,True,11)}      {Osszes(orders,'PL',11,True,21)}     {Osszes(orders,'PL',21,True,31)}")
print(f"TV      {Osszes(orders,'TV',0,True,11)}      {Osszes(orders,'TV',11,True,21)}     {Osszes(orders,'TV',21,True,31)}")
print(f"NR      {Osszes(orders,'NR',0,True,11)}      {Osszes(orders,'NR',11,True,21)}      {Osszes(orders,'NR',21,True,31)}")