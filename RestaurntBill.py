import os
masalar= dict() # dict() yerine {} yazabilirdim.

for i in range(10):
    masalar[i]=0

islemler="""
[1].......hesap ekle
[2].......hesap sil
[3].......masaları görüntüle
[Q].......çıkış yap"""

def veri_al(dosya_adı):
    try:
        dosya=open(dosya_adı)
        veriler=dosya.read()
        veriler=veriler.split("\n")
        veriler.pop()
        dosya.close()
        for i in enumerate(veriler):
            masalar[i[0]] = i[1]
    except FileNotFoundError:
        dosya=open(dosya_adı,"w")
        dosya.close()
        print("dosya ilk defa oluşturuldu.")



def veri_yaz_update(dosya_adı):
    dosya=open(dosya_adı,"w")
    for i in range(10):
        updates=str(masalar[i])
        dosya.write(updates+"\n")

    dosya.close()


def hesap_ekle():

    masa_no=int(input("masa no:"))
    try:
        if float(masa_no) >= 10:
            print("böyle bir masa bulunmamaktadır.")
            input("işlemlere dönmek için enter'a basın:")
        else:
            mevcut_hesap = float(masalar[masa_no])
            eklenecek_tutar = float(input("eklenecek tutar:"))
            toplam = mevcut_hesap + eklenecek_tutar
            masalar[masa_no] = toplam
    except:
        print("hata oluştu.")
        input("işlemlere dönmek için enter'a basın:")


def hesap_Sil():

    try:
        masa_no=int(input("masa no:"))
        if masa_no >= 10:
            print("böyle bir masa bulunmamaktadır")
            input("işlemlere dönmek için enter'a basın:")
        else:
            mevcut_tutar=float(masalar[masa_no])
            odenecek_miktar = float(input("ödenecek miktar:"))

            while odenecek_miktar > mevcut_tutar:
                print("yapılacak ödeme mevcut tutardan fazladır.")
                odenecek_miktar=float(input("lütfen ödenecek miktarı tekrar giriniz:"))
            toplam = mevcut_tutar - odenecek_miktar
            masalar[masa_no] = toplam

    except:
        print("hata oluştu.")
        input("işlemlere dönmek için enter'a basın:")


def masaları_goruntule():
    for i in range(10):
        print("masa {} = {}".format(i,masalar[i]))
    input()

def main():
    veri_al("restaurant.txt")
    while True:
        os.system("cls")
        print(islemler)
        secim=(input("işleminiz:"))
        veri_yaz_update("restaurant.txt")
        if secim=="1":
            hesap_ekle()
        elif secim=="2":
            hesap_Sil()
        elif secim=="3":
            masaları_goruntule()
        elif secim=="q" or secim=="Q":
            quit()
        else:
            print("yanlış bir seçim yaptınız ya da seçim yapmadınız.\n tekrar denemek için enter'a basın.")
            input()

main()