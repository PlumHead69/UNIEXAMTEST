import string
f = open('rendel.txt', 'r')

orders = []

for i in f:
    orders.append(i)

f.close()



allorders = []

class Datas():

    def __init__(self) -> None:

        pass

    def Sorting(unsort,sort):
        
        for i in unsort:
            order=[]
            str(i)

            extractedParts = i.split()
            order.append(int(extractedParts[0]))
            order.append(extractedParts[1])
            order.append(int(extractedParts[2]))
            
            sort.append(order)

            del order
            

    def OrderCalc(allorders):
        return len(allorders)

    def SpecDay(allorders, costumday):
        days=[]
        num = string.digits
        again = False

        if costumday in num:
            for i in allorders:
                if i[0] == int(costumday):
                    days.append(i)
            print("A rendelések száma az adott napon: " + str(len(days)))
        else:
            #print("Rossz adat lett megadva")
            again = True
            return again 
        

    def NoAdsCity(allorders):
        
        NoAdsList = []
        DaysMissed = []

        for i in allorders:
            if i[1] == 'NR':
                NoAdsList.append(i[0])
        
        for i in range(1,31):
            if NoAdsList.count(i) > 0:
                continue
            else:
                DaysMissed.append(i)
            


        if len(DaysMissed) == 0:
            print("Minden nap volt rendelés a reklámban nem érintett városból")
        else:
            return len(DaysMissed)

    def BiggestOrder(allorders):

        biggestnum = 0
        bigid = []

        for order in allorders:
            if order[2] > biggestnum:
                biggestnum=order[2]
            else:
                continue

        bigid.append(biggestnum)

        for order in allorders:
            if order[2] == biggestnum:
                bigid.append(order[0])

        return bigid


    def Osszes(allorders,id,start,end,stat):
        
        sorted = []
        chosenday= []

        for order in allorders:
            if order[1] == id:
                sorted.append(order)

        for order in sorted:
            if order[0] >= start and order[0] <= end:
                chosenday.append(order)

        if stat == True:
            return len(chosenday)
        else:
            i = 0
            for order in chosenday:
                i+=order[2]
            return i





d = Datas

d.Sorting(orders, allorders)

print("2. Feladat")
print("A rendelések száma: " + str(d.OrderCalc(allorders)))

print("\n" +"3. Feladat")

dayselect = input("Kérem adjon meg egy napot:" )
d.SpecDay(allorders,dayselect)
if d.SpecDay(allorders,dayselect) == True:
    print("Rossz adat lett megadva")
    dayselect = input("\n" + "Kérem adjon meg egy napot:" )
    d.SpecDay(allorders,dayselect)

print("\n" +"4. Feladat")
print(str(d.NoAdsCity(allorders)) + " nap nem volt a reklámban nem érintett városból rendelés")


print("\n" +"5. Feladat")
f5 = d.BiggestOrder(allorders)
print("A legnagyobb darabszám: " + str(f5[0]) +"," + " a rendelés napja: " + str(f5[1]))


print("\n" +"7. Feladat")
print("A rendelt termékek darabszáma a 21. napon" + " PL: " + 
      str(d.Osszes(allorders,'PL', 21,21,False)) + " TV: " +
      str(d.Osszes(allorders,'TV', 21,21,False)) + " NR: " +
      str(d.Osszes(allorders,'NR', 21,21,False))
      )



pl1 = str(d.Osszes(allorders,'PL', 1,10,True))
pl2 = str(d.Osszes(allorders,'PL', 11,20,True))
pl3 = str(d.Osszes(allorders,'PL', 21,30,True))

tv1 = str(d.Osszes(allorders,'TV', 1,10,True))
tv2 = str(d.Osszes(allorders,'TV', 11,20,True))
tv3 = str(d.Osszes(allorders,'TV', 21,30,True))

nr1 = str(d.Osszes(allorders,'NR', 1,10,True))
nr2 = str(d.Osszes(allorders,'NR', 11,20,True))
nr3 = str(d.Osszes(allorders,'NR', 21,30,True))

print("8. Feladat")
print("Napok\t" + "1..10\t" + "11..20\t" + "21..30")
print("PL   \t" + pl1 +"\t" + pl2 + "\t" + pl3)
print("TV   \t" + tv1 +"\t" + tv2 + "\t" + tv3)
print("NR   \t" + nr1 +"\t" + nr2 + "\t" + nr3)
