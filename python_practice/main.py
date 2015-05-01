from myLib import all, Test, decorator
import muliimportpy

all.append(1)

print all

a = Test()
Test.SayHi()
Test.SayWorld()
a.Say()
print a.x
a.x = 2
print a.x


@decorator.A
def Ts():
    print "h"


@decorator.B
def Tz():
    print "hi"


@decorator.C
def Ta(a, b):
    print a + b

Ta(1, 2)


@decorator.D("hunagtao")
def Tb(a, b):
    print "a+b=", a + b

print "start"

Tb(2, 4)
