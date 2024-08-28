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

        print("Az adatsorok száma: " + str((len(camptypes))))
        print("Az először rögzített tábor témája: " + str(camptypes[0]))
        print("Az utoljára rögzített tábor témája: " + str(camptypes[-1]))


    def Musiccamp(allcamps):

        musics=[]
        for camp in allcamps:
            if camp[5] == "zenei":
                musics.append(camp)

        if len(musics) > 0:
            for start in musics:
                print("Zenei tábor kezdődik " + str(start[0])+ "." + " hó " + str(start[1]) + ". napján ")

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
                print("Legnépszerűbbek:")
                print(str(camp[0]) + " " + str(camp[1]) + " " + str(camp[5]))

        
    def Sorszam(allcamps, month,day):

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

        
        for i in reversed(calender):
            if i[0] == 6 and i[1] < 16:
                calender.remove(i)

        curdaylist=[]
        curdaylist.append(month)
        curdaylist.append(day)

        bool = False
        cardaynum=[]

        for i in range(len(calender)):
            if calender[i] == curdaylist:
                bool = True
                cardaynum.append(i+1)


        simult = 0

        if bool == True:
            
            for camp in allcamps:
                
                if camp[0] == month and camp[2] == month:
                    if camp[1] <= day and camp[3] >= day:
                        simult+=1
                        

                elif camp[0] != month and camp[2] == month:
                    if camp[3] >= day:
                        simult+=1
                        
            print("Ekkor éppen " + str(simult) + " tábor tart.")
            
        else:
            print("Nincs ilyen nap")  
    
    
    def Egytanulo(allcamps,id):

        campslist = []

        for camp in allcamps:
            if id in camp[4] :   
                del camp [4]
                campslist.append(camp)

              
                
        campslist = sorted(campslist)


        k = open("egytanulo.txt", "w")

        for camp in campslist:  
            k.write(str(camp[0]) + "." + str(camp[1]) + "-" + str(camp[2]) + "." + str(camp[3]) + ". " + str(camp[4]) + "\n")
        k.close()

        if len(campslist) == 0:
            print("Rossz gyerek id")  
        else:
            for date in range(len(campslist)-1):
                if campslist[date][2:4] > campslist[date+1][0:2]:
                    print("Nem mehet el mindegyik táborba.")
                    break
            else:
                print("Mindegyik táborba elmehet")

        
    
d = Data


allcamps = []
d.Sorting(camps,allcamps)
#print(allcamps)

print("Feladat 2")
d.CountCamps(allcamps)

print("\n"+"Feladat 3")
d.Musiccamp(allcamps)

print("\n"+"Feladat 4")
d.Mostpopular(allcamps)

"""month = input("hó: ")
day = input("nap: ")"""

print("\n"+"Feladat 6")
d.Sorszam(allcamps,month = int(input("hó: ")),day = int(input("nap: ")))

print("\n"+"Feladat 7")
d.Egytanulo(allcamps,id = input("Adja meg egy tanuló betűjelét: "))





