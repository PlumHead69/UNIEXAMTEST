class Labsim:

    def __init__(self,KeresesKesz,KijaratOszlopindex,KijaratSorindex,NincsMegoldas,OszlopokSzama,SorokSzama):
        
        self.KeresesKesz = KeresesKesz
        self.KijaratOszlopindex = KijaratOszlopindex
        self.KijaratSorindex = KijaratSorindex
        self.NincsMegoldas = NincsMegoldas
        self.OszlopokSzama = OszlopokSzama
        self.SorokSzama = SorokSzama

    def get_KeresesKesz(self):
        return self.KeresesKesz
    
    def set_KeresesKesz(self,bool):
        self.KeresesKesz = bool

    def get_KijaratOszlopindex(self):
        return self.KijaratOszlopindex
    
    def get_NincsMegoldas(self):
        return self.NincsMegoldas
    
    def set_NincsMegoldas(self,bool):
        self.NincsMegoldas = bool

    def get_OszlopokSzama(self):
        return self.OszlopokSzama
    
    def get_SorokSzama(self):
        return self.SorokSzama


    def BeolvasAdatsorok(self,f):    

        self.Adatsorok = []
        
        for line in f:
            self.Adatsorok.append(line.strip("\n"))

        self.KeresesKesz = False
        self.NincsMegoldas = True
        self.OszlopokSzama = len(self.Adatsorok)
        self.SorokSzama = self.Adatsorok[len(0)]
        self.KijaratOszlopindex = self.OszlopokSzama
        self.KijaratSorindex = self.SorokSzama -1
        
            
    def KiirLab(self):
        for line in self.Adatsorok:
            print(line)        
        












f = open("Lab1.txt","r")
l = Labsim

l.BeolvasAdatsorok(l,f)
l.KiirLab(l)


























f.close()





















