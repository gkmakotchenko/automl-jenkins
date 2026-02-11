import os,sys, json
from datetime import datetime
from math import *  # noqa: F403

def Calc(x,y):  # плохое имя, нет аннотаций, стиль
  z=x+y
  return  z

class data:
    def __init__(self,ID,Name):
        self.ID=ID
        self.Name=Name

def doStuff( a, b ,c=None ):
    if a==None:
        print("a is none")  # print в библиотечном коде
    if b:
        pass
    unused = 123
    return Calc(a,b)

def main():
    d=data(1,"test")
    print( doStuff(1,2) )
    if True: print("inline")  # noqa: E701
    return 0

if __name__=="__main__":
    sys.exit(main())
