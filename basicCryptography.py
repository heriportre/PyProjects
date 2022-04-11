def merge_triplets(fun):
    def x(lst):
        finalLst=[]
        ln=len(lst)//3
        kalan=len(lst)%3
        for i in range(ln):
            finalLst.append(fun(lst[3*i],lst[3*i+1],lst[3*i+2]))
        for i in range(kalan):
            finalLst.append(lst[3*ln+i])
        return finalLst
    return x

"""def merge_triplets(fun,lst):

    finalLst=[]
    ln=len(lst)//3
    kalan=len(lst)%3
    for i in range(ln):
        finalLst.append(fun(lst[3*i],lst[3*i+1],lst[3*i+2]))
    for i in range(kalan):
        finalLst.append(lst[3*ln+i])
    return finalLst"""

"""def a(x,y,z):
    return x*y*z
func=merge_triplets(a)
print(func([1,2,2,4]))"""

"""add_triplets = merge_triplets(lambda x, y, z: x+y+z)
print(add_triplets([1, 2, 3, 4]))
print(add_triplets([1, 2, 3, 4, 5]))
print(add_triplets([1, 2, 3, 4, 5, 6]))"""
from numpy import *
from pandas import *
matrix1 = [[1, 2], [1, 3]]
matrix2 = [[1], [20]]
m1satır=len(matrix1)
m1sutun=len(matrix1[0])
m2satır=len(matrix2)
m2sutun=len(matrix2[0])

"""def encode(m1,m2):
    resmatrix = []
    for i in range(len(m1)):
        resmatrix.append([])
        for j in range(len(m2[0])):
            resmatrix[i].append(0)
            for k in range(len(m2)):
                resmatrix[i][j] += m1[i][k] * m2[k][j]
    return resmatrix"""
alph="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z -"
alph=alph.lower().split()
numb=[i for i in range(1,len(alph)+1)]
base={}
for k in range(len(alph)):
    base[alph[k]]=numb[k]#harflerin alfabetik karşılığı olan sayıları sözlük haline getirip temel hazırladık
print(base)
print(alph)
print(numb)

sttr="ATTACK NOW"

def str_convrt_prencode(sttr):
    sttr = sttr.lower().replace(" ", "-")
    strr = ""
    for i in range(len(sttr)):
        if i%2==1:#stringi 2şerli parçalıyor her 2liden sonra virgil koyuyor(listeye çeviriken virgüllerdenden parçalamak için)
            strr+=sttr[i]
            if i!=len(sttr)-1:#stringin sonuna virgül koymamayı sağlıyor
                strr+=","
        else:
            strr+=sttr[i]
    strr=strr.split(",")#2şerli stringi virgüllerden parçalayıp 2şerli liste yaptık
    print(strr)

    preencode=[]
    for j in range(len(strr)):
        preencode+=[[]]
        for k in range(len(strr[j])):
            preencode[j]+=[[base[strr[j][k]]]]#2şerli listede gezinip her elemana alfabedeki sıra denklerine göre sayılar verdik ve çarpmaya uygun birer matrix haline getirdik
    print(preencode)
    return preencode
a=str_convrt_prencode("ATTACK NOW")
print(a)

"""A matrixi ile parametre m matrixini çarpıyor"""
def encode(m):
    A = [[1, 2], [1, 3]]
    resmatrix = []
    for i in range(len(A)):
        resmatrix.append([])
        for j in range(len(m[0])):
            resmatrix[i].append(0)
            for k in range(len(m)):
                resmatrix[i][j] += A[i][k] * m[k][j]
    return resmatrix

"""str_convrt_prencode(str) e parametre olarak verilen stringteki harfleri str_convrt_prencode(str) alfabedeki denklerine göre sayılar veriyor,"""
def full_encode(mm):
    alphabetcpreencode=str_convrt_prencode(mm)
    full_encoded=[]
    for i in alphabetcpreencode:
        full_encoded+=[encode(i)]
    return full_encoded

print(full_encode(sttr))

""" inverse A matrixi ile parametre m matrixini çarpıyor"""
def decode(m):
    AINV=[[3,-2],[-1,1]]
    resmatrix = []
    for i in range(len(AINV)):
        resmatrix.append([])
        for j in range(len(m[0])):
            resmatrix[i].append(0)
            for k in range(len(m)):
                resmatrix[i][j] += AINV[i][k] * m[k][j]
    return resmatrix

