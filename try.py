from qutip import *
import numpy as np
import matplotlib.pyplot as p
from random import *
FirstLayerNum=10
NextLayerNum=8
FinalLayerNum=2
LearningRate=0.2
up=basis(2,0)
down=basis(2,1)
OriginData=[randint(0,1) for i in range(FirstLayerNum)]
def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))
def sigmoid_prime(z):
    return sigmoid(z)*(1-sigmoid(z))
def GetOriginU():
    global lambsNext
    global UsNext
    global lambsFinal
    global UsFinal
    lambsNext = [[[random() for i in range(4)] for j in range(FirstLayerNum)]for k in range(NextLayerNum)]
    UsNext = [[ lambsNext[k][j][0]*sigmax()+lambsNext[k][j][1]*sigmay()+lambsNext[k][j][2]*sigmaz()+lambsNext[k][j][3]*qeye(2)\
                for j in range(FirstLayerNum)] for k in range(NextLayerNum)]
    # print(UsNext[1][1])
    # print(expect(UsNext[1][1],down))

    lambsFinal = [[[random() for i in range(4)] for j in range(NextLayerNum)]for k in range(FinalLayerNum)]
    UsFinal = [[ lambsFinal[k][j][0]*sigmax()+lambsFinal[k][j][1]*sigmay()+lambsFinal[k][j][2]*sigmaz()+lambsFinal[k][j][3]*qeye(2) \
                for j in range(NextLayerNum)] for k in range(FinalLayerNum)]

def GetOriginPsi(BinList):
    global Psi
    global Ans
    if BinList[2]==1:
        Ans=1
    else:
        Ans=0
    Psi=[basis(2,a) for a in BinList]
def CompuFirst():
    global Psi
    Psi=[sum([UsNext[i][j].unit()*Psi[j].unit() for j in range(FirstLayerNum)]) for i in range(NextLayerNum)]
def CompuFinal():
    global Psi
    Psi=[sum([UsFinal[i][j].unit()*Psi[j].unit() for j in range(NextLayerNum)]) for i in range(FinalLayerNum)]
    print(Psi[1])
def GetCost():
    global Psi
    Psi=[a.unit() for a in Psi]
    global Cost
    Cost=0
    if Ans==1:
        Cost+=abs(Psi[0].full()[0]-0)
        Cost+=abs(Psi[1].full()[0]-1)
    if Ans==0:
        Cost+=abs(Psi[0].full()[0]-1)
        Cost+=abs(Psi[1].full()[0]-0)
    print('Cost:'+str(Cost))
def Back():
    global lambsNext
    global UsNext
    global lambsFinal
    global UsFinal
    DerivNext=[[[GetDerivN(i,j,k) for i in range(4)] for j in range(FirstLayerNum)] for k in range(NextLayerNum)]
    DerivFinal=[[[GetDerivF(i,j,k) for i in range(4)]for j in range(NextLayerNum)]for k in range(FinalLayerNum)]
    print(DerivNext)
    print(DerivFinal)
    lambsNext+=DerivNext
    lambsFinal+=DerivFinal
    UsNext = [[ lambsNext[k][j][0]*sigmax()+lambsNext[k][j][1]*sigmay()+lambsNext[k][j][2]*sigmaz()+lambsNext[k][j][3]*qeye(2)\
                for j in range(FirstLayerNum)] for k in range(NextLayerNum)]
    UsFinal = [[ lambsFinal[k][j][0]*sigmax()+lambsFinal[k][j][1]*sigmay()+lambsFinal[k][j][2]*sigmaz()+lambsFinal[k][j][3]*qeye(2) \
                for j in range(NextLayerNum)] for k in range(FinalLayerNum)]
def GetDerivN(i,j,k):
    global lambsNext
    global UsNext
    global lambsFinal
    global UsFinal
    print('NNN')
    print(i,j,k)
    lambsNext[k][j][i]+=0.1

    GetOriginPsi(OriginData)
    UsNext = [[ lambsNext[k][j][0]*sigmax()+lambsNext[k][j][1]*sigmay()+lambsNext[k][j][2]*sigmaz()+lambsNext[k][j][3]*qeye(2)\
                for j in range(FirstLayerNum)] for k in range(NextLayerNum)]
    CompuFirst()
    CompuFinal()

    lambsNext[k][j][i]-=0.1
    return LearningRate * GetCostDer()
def GetDerivF(i,j,k):
    print('FFF')
    print(i,j,k)
    global lambsNext
    global UsNext
    global lambsFinal
    global UsFinal
    lambsFinal[k][j][i] += 0.1

    GetOriginPsi(OriginData)
    UsFinal = [[lambsFinal[k][j][0] * sigmax() + lambsFinal[k][j][1] * sigmay() + lambsFinal[k][j][2] * sigmaz() +
               lambsFinal[k][j][3] * qeye(2) \
               for j in range(NextLayerNum)] for k in range(FinalLayerNum)]
    CompuFirst()
    CompuFinal()

    lambsNext[k][j][i] -= 0.1
    return LearningRate * GetCostDer()
def GetCostDer():
    global Psi
    Psi=[a.unit() for a in Psi]
    global Cost
    Cos=0
    if Ans==1:
        Cos+=abs(Psi[0].full()[0]-0)
        Cos+=abs(Psi[1].full()[0]-1)
    if Ans==0:
        Cos+=abs(Psi[0].full()[0]-1)
        Cos+=abs(Psi[1].full()[0]-0)
    return (Cost-Cos)/10
GetOriginU()

GetOriginPsi(OriginData)
CompuFirst()
CompuFinal()
GetCost()
Back()
