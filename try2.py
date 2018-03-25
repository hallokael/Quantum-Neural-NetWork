from qutip import *
import numpy as np
import matplotlib.pyplot as p
from random import *

FirstLayerNum=10
NextLayerNum=10
EndLayerNum=10

lambsNext = [[[random() for i in range(4)] for j in range(FirstLayerNum)]for k in range(NextLayerNum)]
UsNext = [[ lambsNext[j][k][0]*sigmax()+lambsNext[j][k][1]*sigmay()+lambsNext[j][k][2]*sigmaz()+lambsNext[j][k][3]*qeye(2)\
            for j in range(FirstLayerNum)] for k in range(NextLayerNum)]
Psi=[basis(2,a) for a in [randint(0,1) for i in range(FirstLayerNum)]]
r=[sum([UsNext[i][j]*Psi[j] for j in range(FirstLayerNum)]) for i in range(NextLayerNum)]

