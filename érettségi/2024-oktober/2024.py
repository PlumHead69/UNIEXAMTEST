from datetime import datetime

f = open('bedat.txt', 'r')
codes = []

for i in f:
    codes.append(i)

f.close()


allpupils = []
lates=[]

class Datas:

    def __init__(self) -> None:

        pass

    def Sorting(x,y):

        for i in x:
            pupilid=[]
            str(i)

            extractedParts = i.split()
            pupilid.append(extractedParts[0])
            pupilid.append(extractedParts[1])
            pupilid.append(extractedParts[2])
            
            y.append(pupilid)

            del pupilid

# y list with all pupils sorted     
                   
    def LatePupils(y,start,end,lates):
        
        start_time_object = datetime.strptime(start, '%H:%M').time()
        end_time_object = datetime.strptime(end, '%H:%M').time()
        
        for pupil in y:
            current_Time = pupil[1]
            current_Time_time_object = datetime.strptime(current_Time, '%H:%M').time()
            if current_Time_time_object >= start_time_object and current_Time_time_object <= end_time_object:
                lates.append(pupil)
                
    

    def ActcheckSet(y,act):
        checked=[]
        for pupil in y:
            if int(pupil[2]) == act:
                checked.append(pupil[0])

        setted = set(checked)
        return len(setted)
    
    def More(book,food):
        if book > food:
            print("Többen voltak, mint a menzán")
        else:
            print("Nem voltak többen, mint a menzán")

    def PupInfo(y,id):
        timelist=[]
        for pupil in y:
            if pupil[0] == id:
                if int(pupil[2]) == 1 or int(pupil[2]) == 2:          
                    timelist.append(pupil)
       
            
        arrive_time_object = datetime.strptime(timelist[0][1], '%H:%M')
        leave_time_object = datetime.strptime(timelist[1][1], '%H:%M')
        subtract = leave_time_object - arrive_time_object
        return subtract

    def KisGecik(y,start, end):
        arrivals=[]
        start_time_object = datetime.strptime(start, '%H:%M').time()
        end_time_object = datetime.strptime(end, '%H:%M').time()
        
        for pupil in y:
            if pupil[1] >= str(start_time_object) and int(pupil[2]) == 1: #or pupil[1] <= end_time_object:
                arrivals.append(pupil)
        
        for pupil in arrivals:
            if pupil[1] <= str(end_time_object):
                arrivals.remove(pupil)
        
        
        uniqueList = []
        duplicateList = []
 
        for i in arrivals:
            if i not in uniqueList:
                uniqueList.append(i)
            elif i not in duplicateList:
                duplicateList.append(i)
 
        print(duplicateList)
        print(uniqueList)




d = Datas
d.Sorting(codes,allpupils)
#print(allpupils)

d.LatePupils(allpupils,'07:55','08:15',lates)
#print(lates)




"""#Feladat 2
print("2. Feladat")
print("Az első tanuló " + allpupils[0][1] + "-kor lépett be a főkapun.")
print("Az utolsó tanuló " + allpupils[-1][1] + "-kor lépett ki a főkapun.")

#Feladat 4
print("4. Feladat")
print("A menzán aznap " + str(d.ActcheckSet(allpupils,3)) + " tanuló ebédelt.")

#Feladat 5
print("5. Feladat")
print("Aznap " + str(d.ActcheckSet(allpupils,4)) + " tanuló kölcsönzött a könyvtárban.")
bookact = d.ActcheckSet(allpupils,4)
foodact = d.ActcheckSet(allpupils,3)
print(d.More(bookact,foodact))

#Feladat 6


#Feladat 7
print("7. Feladat")
print("Egy tanuló azonosítója=")
idinput = input()
splitted = str(d.PupInfo(allpupils,idinput)).split(":")
print("A tanuló érkezése és távozása között " + splitted[0] + " óra "+ splitted[1]+ " perc telt el.")"""

d.KisGecik(allpupils,'07:00','11:00')
















