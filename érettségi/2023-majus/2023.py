f = open('taborok.txt', "r")

camps=[]

for camp in f:
    camps.append(camp)

f.close()


class Data:

    def __init__(self) -> None:
        pass

    def Sorting(unsort,sort):
        
        for i in unsort:
            order=[]
            str(i)

            extractedParts = i.split()
            order.append(int(extractedParts[0]))
            order.append(int(extractedParts[1]))
            order.append(int(extractedParts[2]))
            order.append(int(extractedParts[3]))
            order.append(extractedParts[4])
            order.append(extractedParts[5])

            sort.append(order)

            del order   

    def CountCamps(allcamps):
        
        camptypes=[]
        for camp in allcamps:
            camptypes.append(camp[5])

        print((len(camptypes)))
        print(camptypes[0])
        print(camptypes[-1])


    def Musiccamp(allcamps):

        musics=[]
        for camp in allcamps:
            if camp[5] == "zenei":
                musics.append(camp)

        if len(musics) > 0:
            for start in musics:
                print(str(start[0])+ " " + str(start[1]) + " ")

        else:
            print("Nem volt zenei tábor.")

    def Mostpopular(allcamps):

        camps = []
       
        for camp in allcamps:
           camps.append(camp[4])

        longest = max(camps)

        

d = Data


allcamps = []
d.Sorting(camps,allcamps)
#print(allcamps)

#print(d.CountCamps(allcamps))

#d.Musiccamp(allcamps)

d.Mostpopular(allcamps)









