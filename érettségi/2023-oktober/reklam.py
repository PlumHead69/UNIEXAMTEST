def osszes(reklam,nap,orders,bool):
    if bool == False:
        counter = 0
        for order in orders:
            if order['reklam'] == reklam and order['nap'] == nap:
                counter += order['db']
        return counter
    else:
        counter = 0
        for order in orders:
            if order['reklam'] == reklam and order['nap'] == nap:
                counter += 1
        return counter
f = open('rendel.txt', 'r')

orders = []

for line in f:
    s = line.strip().split()
    sd = {}
    sd['nap'] = int(s[0])
    sd['reklam'] = s[1]
    sd['db'] = int(s[2])
    orders.append(sd)

print(f"2. Feladat\nA rendelések száma: {len(orders)}")

adottnap = int(input(f"\n3. Feladat\nKérem, adjon meg egy napot: ") or 9)
num=0
for order in orders:
    if order['nap'] == adottnap:
        num+= 1     
print(f"A rendelések száma az adott napon: {num}")

alldays = 30
orderdays = []
for order in orders:
    if order['nap'] not in orderdays and order['reklam'] == "NR":
        orderdays.append(order['nap'])

if alldays != len(orderdays):
    print(f"\n4. Feladat\n{alldays-len(orderdays)} nap nem volt a reklámban nem érintett városból rendelés")
else:
    print(f"\n4. Feladat\nMinden nap volt rendelés a reklámban nem érintett városból")

highestcount = 0
day = 0
for order in orders:
    if order['db'] > highestcount:
        highestcount = order['db']
        day = order['nap']
print(f"\n5. Feladat\nA legnagyobb darabszám: {highestcount}, a rendelés napja: {day}")

ads = {}
ads['PL'] = 0
ads["TV"] = 0
ads["NR"] = 0

nums = []
for ad in ads.keys():
    nums.append((osszes(ad,21,orders,False)))

print(f"\n7. Feladat\nA rendelt termékek darabszáma a 21. napon PL: {nums[0]} TV: {nums[1]} NR: {nums[2]}")

allads = []

for ad in ads.keys():
    s=[]
    ten=0
    twenty=0
    thirty=0
    for i in range(1,31):
        if i <=10:
            ten += osszes(ad,i,orders,True)
        elif i >= 11 and i <= 20:
            twenty += osszes(ad,i,orders,True)
        else:
            thirty += osszes(ad,i,orders,True)

    s = [ten,twenty,thirty]
    allads.append(s)


print(f"\n8. Feladat:\nNapok    1..10   11..20  21..30")
print(f"PL       {allads[0][0]}      {allads[0][1]}     {allads[0][2]}")
print(f"TV       {allads[1][0]}      {allads[1][1]}     {allads[1][2]}")
print(f"NR       {allads[2][0]}      {allads[2][1]}      {allads[2][2]}")