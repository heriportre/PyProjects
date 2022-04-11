import time
import random

class Controller():
    def __init__(self, ChannelNow="TRT", TVstatu="close", Volumestatu=0, Channellist=["TRT"]):  #__init() tanımlanırken default değerlerden(örneğin:tvstatu="close") sonra default değerler gelmelidir,
        self.ChannelNow = ChannelNow                                                        # mesela tvstatu="close" dan sonraki parametre yalnız volumestatu olamaz volumestatu=0 olabilir gibi...
        self.TVstatu = TVstatu                                              #init tanımlarken 'self'ten sonra parametre koyarsan obje yaratırken objenin parametre değerlerini istediğin gibi verebilirsin
        self.VolumeStatu = Volumestatu


    def onoff(self):
        if self.TVstatu == "close":
            print("tv is opening...")
            time.sleep(2)
            self.TVstatu = "open"
        elif self.TVstatu == "open":
            print("tv is closing.")
            time.sleep(2)
            self.TVstatu = "close"

    def increasevolume(self):
        self.VolumeStatu += 5

    def decreasevolume(self):
        self.VolumeStatu -= 5

    def show_channel(self):
        if self.ChannelNow in self.Channellist:
            print(self.ChannelNow)
            time.sleep(2)
        else:
            print("channel has been removed.")
            time.sleep(2)
            self.ChannelNow = ""

    def append_channel(self, channel):
        self.Channellist.append(channel)


    def remove_channel(self, channel):
        self.Channellist.remove(channel)


    def change_channel_manually(self):

        while True:
            print("press 'u' to go following channel\npress 'd' to go previous channel\npress 'q' to turn back mainmenu")

            transaction2 = input("transaction:")
            channel_number = self.Channellist.index(self.ChannelNow)

            if transaction2 == "u":
                if self.ChannelNow == self.Channellist[-1]:
                    print("it is the last channel.\nplease turn back.")
                    time.sleep(2)
                else:
                    next_channel = self.Channellist[channel_number + 1]
                    self.ChannelNow = next_channel
                    channel_number += 1
                    print("now channel is {}".format(self.ChannelNow))
                    time.sleep(2)
            elif transaction2 == "d":
                if self.ChannelNow == self.Channellist[0]:
                    print("it is the firts channel.\nplease go forward.")
                    time.sleep(2)
                else:
                    previous_channel = self.Channellist[channel_number - 1]
                    self.ChannelNow = previous_channel
                    channel_number -= 1
                    print("now channel is {}".format(self.ChannelNow))
                    time.sleep(2)
            elif transaction2 == "q":
                break


    def open_wantedchannel(self):
        while True:
            print("write the channel number you want\nor press 'q' to exit.")
            answr = input("the answer:")
            if answr == "q":
                break
            elif int(answr) >= len(self.Channellist):
                print("last channel is {}".format(self.Channellist[-1]))
                answer = input("do you want to go there?(y/n)")
                if answer == "y":
                    self.ChannelNow = self.Channellist[-1]
                    print("now channel is {}".format(self.ChannelNow))
                    time.sleep(2)
                else:
                    pass

            elif int(answr) < len(self.Channellist):
                self.ChannelNow = self.Channellist[int(answr)]
                print("now channel is {}".format(self.ChannelNow))


    def random_channel(self):
        self.ChannelNow = self.Channellist[random.randint(0, (len(self.Channellist)-1))]
        print("now channel is {}".format(self.ChannelNow))
        time.sleep(2)

    def __len__(self):
        a=len(self.Channellist)
        return a
    def __str__(self):
        print("tv statu = {}\nchannel now = {}\nvolume statu = {}\nchannel list = {}".format(self.TVstatu, self.ChannelNow, self.Volumestatu, self.Channellist))

controller=Controller()

while 1:
    print("""
    TV APPLICATION
[1]-----on/off
[2]-----volume settings
[3]-----change channel manually
[4]-----go wanted channel
[5]-----append channel
[6]-----remove channel
[7]-----see valid channel 
[8]-----see channel list
[9]-----TV informations
[10]----random channel
[11]----quit application""")

    choose = input("transaction:")

    if choose == "1":
        controller.onoff()
    elif choose == "2":

        while True:
            print("""
            press 'u' to increase volume level
            press 'd' to decrease volume level
            press 'q' to back mainmenu""")

            transaction = input("transaction:")

            if transaction == "u":
                if controller.VolumeStatu <= 95:
                    controller.increasevolume()
                    print("now volume is {}".format(controller.VolumeStatu))
                else:
                    print("volume level has already max")
                    time.sleep(2)
            elif transaction == "d":
                if controller.VolumeStatu > 0:
                    controller.decreasevolume()
                    print("now volume is {}".format(controller.VolumeStatu))
                else:
                    print("volume level has already min")
                    time.sleep(2)
            elif transaction == "q":
                break
            else:
                print("invalid choose")

    elif choose == "3":
        controller.change_channel_manually()

    elif choose == "4":
        controller.open_wantedchannel()

    elif choose == "5":
        willappend = input("write name of channel adding:")
        print("the channel is being added.")
        controller.append_channel(willappend)
        time.sleep(1)
    elif choose == "6":
        willremove = input("write name of the channel removing:")
        controller.remove_channel(willremove)
        print("the channel is being removed.")
        time.sleep(1)
    elif choose == "7":
        controller.show_channel()

    elif choose == "8":
        print(controller.Channellist)
        input("press 'enter' to turn back mainmenu")

    elif choose == "9":
        controller.__str__()
        input("press 'enter' to turn back mainmenu")

    elif choose == "10":
        controller.random_channel()

    elif choose == "11":
        print("exit application...")
        time.sleep(2)
        quit()