f = open('felajanlas.txt', 'r')

offers = []

for i in f:
    offers.append(i)

f.close()


alloffers = []

class Data:

    def __init__(self) -> None:

        pass
    
    def Sorting(unsort,sort):

        for i in unsort[1:]:
            order=[]
            str(i)
            
            extractedParts = i.split()
            order.append(int(extractedParts[0]))
            order.append(int(extractedParts[1]))
            order.append(extractedParts[2])
            
            sort.append(order)

            del order

    def WhichSide(alloffers,bool):

        BothSides = []
        OneSide = []

        for offer in range(len(alloffers)):
            if alloffers[offer][0] <= alloffers[offer][1]:
                OneSide.append(offer+1)
            else:
                BothSides.append(offer+1)

        if bool == True:
            return OneSide
        else:
            return BothSides


    def OfferStats(alloffers,offernum):

        listings = []
        
        

        for offer in range(len(alloffers)):
            if alloffers[offer][0] <= offernum and alloffers[offer][1] >= offernum:
                listings.append(offer)

            if alloffers[offer][0] >= alloffers[offer][1] :
                if alloffers[offer][0] <= offernum and alloffers[offer][1] >= offernum:
                    listings.append(offer)


        if len(listings) > 0:
            #Felajanlok szama
            print("A felajánlók száma: " + str(len(listings)))

             #viragagyas szine ha csak elso hely szamit
            curcolor = listings[0]
            print("A virágágyás színe, ha csak az első ültet: " + str(alloffers[curcolor][2]))

            #viragagyas szine ha mindegyik szamit
            colors = []
            for color in listings:
                if alloffers[color][2] not in colors:
                    colors.append(alloffers[color][2])
            
            print("A virágágyás színei: " + str(colors))



        else:
            print("Ezt az ágyást nem ültetik be.")


    def ProjectBeultetes(alloffers):

        i=0

        allspotsnum = []

        for k in alloffers:
            allspotsnum.append(k[1])
            allspotsnum.append(k[0])

        allspotsnum.sort()

        for offer in alloffers:
            if offer[0] < offer[1]:    
                calculated = offer[1] - offer[0]
                i+=calculated
                
            else:
                i += allspotsnum[-1] - offer[0]
                i += offer[1]
                
        
        if i == allspotsnum[-1]:
            print("Minden ágyás beültetésére van jelentkező.")
        elif i >= allspotsnum[-1]:
            print("Átszervezéssel megoldható a beültetés.") 
        else:
            print("A beültetés nem oldható meg.")

        
    def Szinek(alloffers):

        sex = open("szinek.txt", "w")
        
        i = 1
        numlist = []
        
                       
                        
        for i in range(len(alloffers)):

            if alloffers[i][0] < alloffers[i][1]:

                for j in range(alloffers[i][0],alloffers[i][1]):

                    offer=[]
                    offer.append(j)
                    offer.append(i)
                    offer.append(alloffers[i][2])
                    

                    numlist.append(offer)

                    del offer                    

            else:

                range_ = alloffers[i][1] + (len(alloffers) - alloffers[i][0])
                

                for k in range(alloffers[i][0],max(alloffers)[0]):

                    offer=[]
                    offer.append(k)
                    offer.append(i)
                    offer.append(alloffers[i][2])
                    
                    
                    numlist.append(offer)

                    del offer

                for l in range(1,alloffers[i][1]+1):

                    offer=[]
                    offer.append(l)
                    offer.append(i)
                    offer.append(alloffers[i][2])
                    

                    numlist.append(offer)

                    del offer

                

        sorter = []
        for i in numlist:
            sorter.append(i[0])
        sorter.sort()
        
        
        offerslist = []
        checklist = []
        fauilty = []
        
        for offer in range(len(numlist)):
            if numlist[offer][0] not in checklist:
                
                checklist.append(numlist[offer][0])
                offerslist.append(numlist[offer])

        for num in range(len(checklist)):
            if num not in checklist:    
                offerslist.insert(num, [" Nincs ultetes " , num])
                checklist.insert(num,num)
                fauilty.insert(num,num)
        
        

        num = 1
        while num <= len(offerslist):

            for i in range(len(checklist)):
                if offerslist[i][0] == num and checklist[i] not in fauilty: 
                    sex.write(str(offerslist[i][0]) + ". " + str(offerslist[i][1] + 1) + " " + str(offerslist[i][2]) + "\n")
                    num+=1
                elif num in fauilty:
                    sex.write("Ez az ágyás nincs beültetve." + "\n")
                    num+=1
                    
        
       
        

        sex.close()




d = Data

d.Sorting(offers,alloffers)

print("2. Feladat")
print("Felajanlasok szama: " + str(len(alloffers)))

print("\n" + "3. Feladat")
print("A bejárat mindkét oldalán ültetők: " + str(d.WhichSide(alloffers,False)))

print("\n" + "4. Feladat")
sorszam = input("Adja meg az ágyás sorszámát: ")
both = d.WhichSide(alloffers, False)
d.OfferStats(alloffers,int(sorszam))

print("\n" + "5. Feladat")
d.ProjectBeultetes(alloffers)


d.Szinek(alloffers)








