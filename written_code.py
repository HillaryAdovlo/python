class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__mute = False
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_CHANNEL



def power(self):
    if self.__status:
        self.__status = False
    else:
        self.__status = True


def mute(self):
    if self.__status:
        self.__status = True
    else:
        self.__status = False


def volume_up(self):

    if self.__status:
        if self.__volume < Television.MAX_VOLUME:
            self.__volume = self.__volume + 1


def volume_down(self):
    if self.__status:
        if self.__volume < Television.MIN_VOLUME:
            self.__volume = self.__volume - 1


def channel_up(self):

    if self.__status:
        if self.__channel < Television.MAX_CHANNEL:
            self.__channel = self.__channel + 1


def channel_down(self):

    if self.__status:
        if self.__channel < Television.MIN_CHANNEL:
            self.__volume = self.__channel - 1


def __str__(self):
    if self.__mute:
        return f"power = {self.__status}, channel = {self.__channel}, Volume = 0"
    else:
        return f"power = {self.__status}, channel = {self.__channel}, Volume = {self.__volume}"