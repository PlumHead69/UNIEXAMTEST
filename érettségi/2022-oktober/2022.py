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
            print(listings)

             #viragagyas szine ha csak elso hely szamit
            curcolor = listings[0]
            print(alloffers[curcolor][2])

            #viragagyas szine ha mindegyik szamit
            colors = []
            for color in listings:
                if alloffers[color][2] not in colors:
                    colors.append(alloffers[color][2])
            
            print(colors)



        else:
            print("Ezt az ágyást nem ültetik be.")


    def ProjectBeultetes(alloffers, maxoffers):

        i=0

        for offer in alloffers:
            if offer[0] < offer[1]:    
                calculated = offer[1] - offer[0]
                i+=calculated
                
            else:
                i += maxoffers - offer[0]
                i += offer[1]
                
        
        if i == maxoffers:
            print("Minden ágyás beültetésére van jelentkező.")
        elif i >= maxoffers:
            print("Átszervezéssel megoldható a beültetés.") 
        else:
            print("A beültetés nem oldható meg.")

        





d = Data

d.Sorting(offers,alloffers)

#Felajanlasok szama
#print(len(alloffers))

#print(d.WhichSide(alloffers,False))

both = d.WhichSide(alloffers, False)

d.OfferStats(alloffers,100)

allspotsnum = []

for k in alloffers:
    allspotsnum.append(k[1])
    allspotsnum.append(k[0])

allspotsnum.sort()

d.ProjectBeultetes(alloffers,allspotsnum[-1])

print(allspotsnum[-1])









