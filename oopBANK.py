class Banka():
    def __init__(self):
        self.müsterilistesi=list()
    def müsteriol(self):
        Id=input("ıd: ")
        Isım=input("isminiz: ")
        Parola=input("parolanızı belirleyin: ")
        self.müsterilistesi.append(Müsteri(Id,Isım,Parola))
    def müsteriIDkontrol(self,müsteriID):
        self.ids=[i.Id for i in self.müsterilistesi]
        return müsteriID in self.ids
    def müsteriPAROLAkontrol(self, arananmüsteriID, parola):
        for i in self.ids:
            if i==arananmüsteriID:
                print("giriş başarılı!")
    def isimler(self, ıd):
        isimler=[i.Isım for i in self.müsterilistesi]


class Müsteri():
    def __init__(self, ID, ISIM, PAROLA, BAKIYE=0):
        self.id=ID
        self.isim=ISIM
        self.parola=PAROLA
        self.bakiye=BAKIYE


def main():
    banka=Banka()
    while True:
        print("""
        [1] müşteri girişi
        [2] müşteri ol""")
        secim= input("tuşlayınız: ")
        if secim=="1":
            ıd = input("ID: ")
            if banka.müsteriIDkontrol(ıd):
                print("hoşgeldiniz {}".format(i))

                while True:
                    pass


        elif secim=="2":
            pass

        else:
            input("geçersiz işlem\n anamenuye dönmek için rastgele tuşa basın")
