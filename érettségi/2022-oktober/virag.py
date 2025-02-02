with open("felajanlas.txt") as f:
    places_num = int(f.readline())
    data = [offer.strip().split() for offer in f]


offers = []
for i in range(len(data)):
    item = (int(data[i][0]), int(data[i][1]), data[i][2])
    offers.append(item)


#{}

#2

print(len(offers))

#3

both_sides = []
for i in range(len(offers)):
    if  offers[i][0] > offers[i][1]:
        both_sides.append(i+1)
print(both_sides)

#4

def side_difference(tuple):
    nums = []
    if tuple[0] > tuple[1]:
        for i in range(1,tuple[1]+1):
            nums.append(i)
        for i in range(tuple[0],places_num+1):
            nums.append(i)
    else:
        for i in range(tuple[0],tuple[1]):
            nums.append(i)
    return nums

serial_number = int(input("Ágyás sorszám: ") or 100)

offers_for_spot = []

for place in range(len(offers)):
    if serial_number in side_difference(offers[place]):
        offers_for_spot.append((place+1,offers[place][2]))

if len(offers_for_spot) > 0:
    print(len(offers_for_spot))
    colors = [item[1] for item in offers_for_spot]
    print(colors[0])
    colors = list(dict.fromkeys(colors))
    print(colors)
else:
    print("Nincs felajanlas")

#5

flower_beds = []
misseds_beds = []

for offer in offers:
    for bed in side_difference(offer):
        flower_beds.append(bed)

for i in range(1,places_num):
    if i not in flower_beds:
        misseds_beds.append(i)

if len(misseds_beds) == 0:
    print("Minden ágyás beültetésére van jelentkező")
else:
    if len(flower_beds) >= places_num:
        print("Átszervezéssel megoldható a beültetés")
    else:
        print("A beültetés nem oldható meg.")

#6

k = open("szinek.txt","w")

already_planted = []

for i in range(1,places_num):
    if i not in misseds_beds:
        for offer_palce in range(len(offers)):
            if i in side_difference(offers[offer_palce]) and i not in already_planted:
                k.write(offers[offer_palce][2] + " "+ str(offer_palce+1) + "\n")
                already_planted.append(i)
    else:
        k.write("# 0\n" )

k.close()
