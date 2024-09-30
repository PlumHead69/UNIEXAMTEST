f = open("rendel.txt", "r")

orders = []

for line in f:
    s = line.strip().split()
    sd = {}
    sd['nap'] = int(s[0])
    sd['reklam'] = s[1]
    sd['db'] = int(s[2])
    orders.append(sd)

print(orders[3]["reklam"])













