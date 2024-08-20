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
       
        i = [0,""]

        for camp in allcamps:
           if len(camp[4]) > i[0]:
               i[0] = len(camp[4])
               i.pop()
               i.append(camp[5])
              

        for camp in allcamps:
            if camp[5] == i[1]:
                print(str(camp[0]) + " " + str(camp[1]) + " " + str(camp[5]))

        
    def Sorszam(month,day):

        calender=[]
        
        top=30
        curmonth=6
        

        for i in range(3):
            if i > 0 :
                curmonth+=1
                if i < 2 :
                    top+=1
            for k in range(top):
                curday = []
                curday.append(curmonth)
                curday.append(k+1)
                calender.append(curday)

                del curday

        k=0
        for i in range(len(calender)):
            if calender[i][0] == 6 and calender[i][1] > 16:
                print(k)
                k+=1

        curdaylist=[]
        curdaylist.append(month)
        curdaylist.append(day)

        print(calender)

        for i in range(len(calender)):
            if calender[i] == curdaylist:
                print(i)
                print(len(calender))
        


        

d = Data


allcamps = []
d.Sorting(camps,allcamps)
#print(allcamps)

#print(d.CountCamps(allcamps))

#d.Musiccamp(allcamps)

#d.Mostpopular(allcamps)

d.Sorszam(8,31)







