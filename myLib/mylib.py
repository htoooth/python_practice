__all__ = [
    "all",
    "Test"
]

all = []


class Test(object):

    Y = "Hi"

    def __init__(self):
        self.__x = 1

    def Say(self):
        print self.__x

    @classmethod
    def SayHi(cls):
        print cls.Y

    @staticmethod
    def SayWorld():
        print "World"

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @x.deleter
    def x(self):
        del self.__x
