import random

class Düsman():
    def __init__(self):
        self.can=random.randint(30,60)
        self.maxgüc=20
        self.mingüc=10
        self.kalkan=8

    def vur(self,vurulacak):
        damage=random.randint(self.mingüc,self.maxgüc)
        vurulacak.can=vurulacak.can + vurulacak.kalkan - damage
        if player.kalkan>=1:
            player.kalkan-=1
        print("{} hasar aldın!".format(damage))


class Player(Düsman):
    def __init__(self):
        self.can=150
        self.maxgüc=60
        self.mingüc=30
        self.kalkan=15

    def vur(self,düsman):
        damage= random.randint(self.mingüc,self.maxgüc)
        düsman.can=düsman.can + düsman.kalkan - damage
        if düsman.kalkan >=1:
            düsman.kalkan-=3
        print("düşmana {} vurdun!".format(damage))
        if düsman.can<=0:
            düsmanlar.remove(düsman)
            print("bir düşman öldürdünüz!!")


düsmanlar=list()
for i in range(10):
    düsman=Düsman()
    düsmanlar.append(düsman)

player=Player()
while True:
    if player.can>=1:
        print("player durumu: can==>> {}  max güç==>> {}  min güç==>> {}  kalkan==>> {}".format(player.can,player.maxgüc,player.mingüc,player.kalkan))
    else:
        print("game over :(")
        quit()
    for i in enumerate(düsmanlar):
        print("{}. düşman can==>> {}  max güç==>> {}  min güç==>> {}  kalkan==>> {}".format(i[0],i[1].can,i[1].maxgüc,i[1].mingüc,i[1].kalkan))

    saldırılan= düsmanlar[int(input("saldırılacak düşmanın numarasını seçin:"))]
    player.vur(saldırılan)
    if düsmanlar:
        saldırandüsman= düsmanlar[random.randint(0,len(düsmanlar)-1)]
        saldırandüsman.vur(player)
    elif not düsmanlar:
        print("tebrikler hiç düşman kalmadı!!!")
        quit()