def osszes(reklam,nap,orders):
    counter = 0
    for order in orders:
        if order['reklam'] == reklam and order['nap'] == nap:
            counter += order['db']
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
    nums.append((osszes(ad,21,orders)))

print(f"\n7. Feladat\nA rendelt termékek darabszáma a 21. napon PL: {nums[0]} TV: {nums[1]} NR: {nums[2]}")










