import numpy as np
import matplotlib.pyplot as plt
from random import randint

rad = 1
height = 15
witdh = 15
spacebtwn = np.sin(67.5*np.pi/180)
oktagony = [[None for i in range(height)] for j in range(witdh)]
romby = [[None for i in range(height-1)] for j in range(witdh-1)]

class Diamond:
    def __init__(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
        self.visited = 0


class Octagon:
    def __init__(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
        self.sciany = [1, 1, 1, 1, 1, 1, 1, 1]
        self.visited = 0


def laczenie( center_x, center_y):
    pkt = []
    T = np.linspace(-22.5*np.pi/180, 2 * np.pi-(22.5*np.pi/180), 9)
    X = rad * np.sin(T) + center_x
    Y = rad * np.cos(T) + center_y
    for n in range(8):
        pkt.append([(X[n], X[n + 1]), (Y[n], Y[n + 1])])
    return pkt

def losowanie(sciany,idxi,idxj):
    for n in range(8):
        p = randint(0, 8)
        if p <4:
            sciany[n] = 0
        if (idxi == 0 and idxj == 0 and n > 2 ): sciany[n] = 1
        if(idxi == height - 1 and idxj == 0 and  n > 0 and n < 6): sciany[n] = 1
        if(idxi == 0 and idxj == witdh - 1 and (n < 2 or n > 4)): sciany[n] = 1
        if(idxi == height -1  and idxj == witdh - 1 and (n > 6 or n < 4)): sciany[n] = 1

        if(idxj == 0 and n>2 and n<6): sciany[n] = 1
        if(idxi == 0 and n>4): sciany[n] = 1
        if(idxi == height - 1 and n > 0 and n < 4): sciany[n] = 1
        if idxj == witdh - 1 and n <2 or n > 6: sciany[n] = 1
    return sciany

def sprawdzajsciany():
    for i in range(height-1):
        for j in range(witdh-1):
            if oktagony[i][j].sciany[0] == 0 or oktagony[i][j+1].sciany[4] == 0:
                oktagony[i][j].sciany[0] = 0
                oktagony[i][j+1].sciany[4] = 0
            if oktagony[i][j].sciany[2] == 0 or oktagony[i+1][j].sciany[6] == 0:
                oktagony[i][j].sciany[2] = 0
                oktagony[i+1][j].sciany[6] = 0
            if oktagony[i][j].sciany[4] == 0 or oktagony[i][j-1].sciany[0] == 0:
                oktagony[i][j].sciany[4] = 0
                oktagony[i][j-1].sciany[0] = 0
            if oktagony[i][j].sciany[6] == 0 or oktagony[i-1][j].sciany[2] == 0:
                oktagony[i][j].sciany[6] = 0
                oktagony[i-1][j].sciany[2] = 0
    for i in range(height-1):
        if oktagony[i][height-1].sciany[2] == 0 or oktagony[i+1][height-1].sciany[6] == 0:
            oktagony[i][height-1].sciany[2] = 0
            oktagony[i+1][height-1].sciany[6] = 0
    for i in range(height - 1):
        if oktagony[height - 1][i].sciany[0] == 0 or oktagony[height - 1][i+1].sciany[4] == 0:
            oktagony[height - 1][i].sciany[0] = 0
            oktagony[height - 1][i+1].sciany[4] = 0


def rysowanie(pkt, sciany):
    for n in range(len(pkt)):
        if sciany[n] == 1:
            x = pkt[n][0]
            y = pkt[n][1]
            plt.plot(x, y, c='black')

fig = plt.figure()
for i in range(height):
    for j in range(witdh):
        oktagony[i][j] = Octagon(center_x=2*i*spacebtwn, center_y=2*j*spacebtwn)
        scianki = losowanie(oktagony[i][j].sciany, i, j)

sprawdzajsciany()

for i in range(height):
    for j in range(witdh):
        polaczone = laczenie(oktagony[i][j].center_x, oktagony[i][j].center_y)
        rysowanie(polaczone, oktagony[i][j].sciany)

rombysiatka = []

for i in range(height-1):
    for j in range(witdh-1):
        romby[i][j] = Diamond(center_x=spacebtwn+i*2*spacebtwn, center_y=spacebtwn+j*2*spacebtwn)
        rombysiatka.append(romby[i][j])

listawsp = [[0, 0, 0]]


def bts(listawsp):
    if len(listawsp) == 0: return
    if listawsp[-1][1] == witdh-1 and listawsp[-1][2] == height-1: return
    dostrace = []
    if listawsp[-1][0] == 0:
        indi, indj = listawsp[-1][1], listawsp[-1][2]
        if oktagony[indi][indj].visited == 0:
            oktagony[indi][indj].visited = 1
        if oktagony[indi][indj].sciany[0] == 0 and oktagony[indi][indj+1].visited == 0:
            dostrace.append(0)
        if oktagony[indi][indj].sciany[1] == 0 and romby[indi][indj].visited == 0:
            dostrace.append(1)
        if oktagony[indi][indj].sciany[2] == 0 and oktagony[indi+1][indj].visited == 0:
            dostrace.append(2)
        if oktagony[indi][indj].sciany[3] == 0 and romby[indi][indj - 1].visited == 0:
            dostrace.append(3)
        if oktagony[indi][indj].sciany[4] == 0 and oktagony[indi][indj - 1].visited == 0:
            dostrace.append(4)
        if oktagony[indi][indj].sciany[5] == 0 and romby[indi-1][indj - 1].visited == 0:
            dostrace.append(5)
        if oktagony[indi][indj].sciany[6] == 0 and oktagony[indi-1][indj].visited == 0:
            dostrace.append(6)
        if oktagony[indi][indj].sciany[7] == 0 and romby[indi-1][indj].visited == 0:
            dostrace.append(7)
        if len(dostrace) == 0:
            listawsp.pop(-1)
            bts(listawsp)
            return
        p = randint(0, len(dostrace)-1)
        if dostrace[p] == 0:
            listawsp.append([0, indi, indj+1])
            bts(listawsp)
        if dostrace[p] == 2:
            listawsp.append([0, indi+1, indj])
            bts(listawsp)
        if dostrace[p] == 4:
            listawsp.append([0, indi, indj-1])
            bts(listawsp)
        if dostrace[p] == 6:
            listawsp.append([0, indi-1, indj])
            bts(listawsp)
        if dostrace[p] == 1:
            listawsp.append([1, indi, indj])
            bts(listawsp)
        if dostrace[p] == 3:
            listawsp.append([1, indi, indj - 1])
            bts(listawsp)
        if dostrace[p] == 5:
            listawsp.append([1, indi-1, indj-1])
            bts(listawsp)
        if dostrace[p] == 7:
            listawsp.append([1, indi-1, indj])
            bts(listawsp)
    elif listawsp[-1][0] == 1:
        indi, indj = listawsp[-1][1], listawsp[-1][2]
        romby[indi][indj].visited = 1
        if oktagony[indi][indj].sciany[1] == 0 and oktagony[indi][indj].visited == 0:
            dostrace.append(2)
        if oktagony[indi+1][indj].sciany[7] == 0 and oktagony[indi+1][indj].visited == 0:
            dostrace.append(1)
        if oktagony[indi+1][indj+1].sciany[5] == 0 and oktagony[indi+1][indj+1].visited == 0:
            dostrace.append(0)
        if oktagony[indi][indj+1].sciany[3] == 0 and oktagony[indi][indj+1].visited == 0:
            dostrace.append(3)
        if len(dostrace) == 0:
            listawsp.pop(-1)
            bts(listawsp)
            return
        p = randint(0, len(dostrace) - 1)
        if dostrace[p] == 0:
            listawsp.append([0, indi+1, indj + 1])
            bts(listawsp)
        if dostrace[p] == 1:
            listawsp.append([0, indi + 1, indj])
            bts(listawsp)
        if dostrace[p] == 2:
            listawsp.append([0, indi, indj])
            bts(listawsp)
        if dostrace[p] == 3:
            listawsp.append([0, indi, indj + 1])
            bts(listawsp)
        else:
            if(len(listawsp) != 0) and listawsp[-1][1] != height-1 and listawsp[-1][1] != witdh:
                listawsp.pop(-1)
            return

bts(listawsp)
for i in range(1,len(listawsp)):
    if listawsp[i][0] == 0:
        X2 = oktagony[listawsp[i][1]][listawsp[i][2]].center_x
        Y2 = oktagony[listawsp[i][1]][listawsp[i][2]].center_y
    else:
        X2 = romby[listawsp[i][1]][listawsp[i][2]].center_x
        Y2 = romby[listawsp[i][1]][listawsp[i][2]].center_y
    if listawsp[i-1][0] == 0:
        X1 = oktagony[listawsp[i-1][1]][listawsp[i-1][2]].center_x
        Y1 = oktagony[listawsp[i-1][1]][listawsp[i-1][2]].center_y
    else:
        X1 = romby[listawsp[i-1][1]][listawsp[i-1][2]].center_x
        Y1 = romby[listawsp[i-1][1]][listawsp[i-1][2]].center_y
    plt.plot([X1,X2],[Y1,Y2], c='red')

plt.xticks([])
plt.yticks([])
plt.show()

