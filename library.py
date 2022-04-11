import os
kitap_listesi = list()

menu = """menu
[1] KITAP EKLE
[2] KITAP CIKAR
[3] KITAPLARI LİSTELE
[Q] CIKIS
"""

def updateyaz(dosya_adi,liste:list):
    dosya = open(dosya_adi,"w")
    for i in liste:
        ktpadı = i[0]
        yzradı = i[1]
        dosya.write(ktpadı+"-"+yzradı+"\n")
    dosya.close()

def verial(dosya_adi,liste:list):
    try:
        dosya = open(dosya_adi)
        veriler = dosya.read()
        veriler = veriler.split("\n")
        veriler.pop()
        for i in veriler:
            i = i.split("-")
            kitap_adi = i[0]
            yazar_adi = i[1]
            demet=(kitap_adi,yazar_adi)
            if demet not in liste:
                liste.append(demet)

        dosya.close()

    except FileNotFoundError:
        dosya = open(dosya_adi,"w")
        dosya.close()
        print("dosya ilk defa oluşturuldu.")
        input()

def kitap_ekle(kitap: tuple, liste: list):
    liste.append(kitap)
    print("kitap başarıyla eklendi.")
    input("ana menuye dönmek için herhangi bir tuşa basın.")


def kontrol(kitap: tuple, liste: list):
    if kitap in liste:
        return True
    else:
        return False


def kitap_cıkar(kitap: tuple, liste: list):
    if kontrol(kitap, liste):
        liste.remove(kitap)
        print("kitap başarıyla cıkarıldı.")
        input("ana menuye dönmek için herhangi bir tuşa basın.")

    else:
        print("aradığınız kitap mevcut değildir!")
        print()
        input("ana menuye dönmek için herhangi bir tuşa basın.")



def listele(liste: list):
    if len(liste)==0:
        print("listede mevcut kitap bulunmamaktadır.")
        input()
    else:
        for i in liste:
            print("kitap adı: ===>>>{}  yazar adı: ===>>>{}".format(i[0], i[1]))
        input("ana menuye dönmek için herhangi bir tuşa basın.")


def cıkıs():
    quit()

def main():
    verial("library.txt",kitap_listesi)
    while True:
        updateyaz("library.txt",kitap_listesi)
        os.system("cls")
        print(menu)
        secim = input("tuşlayınız:")

        if secim == "1":
            kitap_adı = input("kitap adı:")
            yazar_adı = input("yazar adı:")
            kitap = (kitap_adı, yazar_adı)
            kitap_ekle(kitap, kitap_listesi)
        elif secim == "2":
            kitap_adı = input("kitap adı:")
            yazar_adı = input("yazar adı:")
            kitap = (kitap_adı, yazar_adı)
            kitap_cıkar(kitap, kitap_listesi)
        elif secim == "3":
            listele(kitap_listesi)
        elif secim == "q" or secim == "Q":
            cıkıs()
        else:
            print("yanlış tuşladınız.\ntekrar deneyiniz. ")
            input("ana menuye dönmek için herhangi bir tuşa basın.")


main()


