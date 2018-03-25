from qutip import *
import numpy as np
import matplotlib.pyplot as p
from random import *
FirstLayerNum=10
NextLayerNum=10
EndLayerNum=10

def GetOriginU():
    global lambsNext
    global UsNext
    lambsNext = [[[random() for i in range(4)] for j in range(FirstLayerNum)]for k in range(NextLayerNum)]
    UsNext = [[ lambsNext[j][k][0]*sigmax()+lambsNext[j][k][1]*sigmay()+lambsNext[j][k][2]*sigmaz()+lambsNext[j][k][3]*qeye(2)\
                for j in range(FirstLayerNum)] for k in range(NextLayerNum)]
def GetOriginPsi(BinList):
    global Psi
    Psi=[basis(2,a) for a in BinList]
def Compu():
    print(UsNext)
    print(Psi)
    # for i in range(NextLayerNum):
    #     for j in range(FirstLayerNum):
    #         r=UsNext[i][j]*Psi[j]
    r=[sum([UsNext[i][j]*Psi[j] for j in range(FirstLayerNum)]) for i in range(NextLayerNum)]
    print(r)
GetOriginU()
GetOriginPsi([randint(0,1) for i in range(FirstLayerNum)])
Compu()