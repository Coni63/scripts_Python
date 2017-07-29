# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import numpy as np

def decimal_to_array(nb):
    binary = bin(nb)[2:].zfill(4)
    binary = list(binary)
    arr = np.array(binary, dtype=np.int8).reshape(2,2)
    return arr

pattern = {}

m = np.array([8,4,2,1])

u = np.array([1,0,0,1]).dot(m)
v = np.array([0,1,1,0]).dot(m)
pattern[u] = v
pattern[v] = u

u2 = np.array([1,0,0,0]).dot(m)
v2 = np.array([0,0,0,1]).dot(m)
pattern[u2] = v2
pattern[v2] = u2

u3 = np.array([0,1,0,0]).dot(m)
v3 = np.array([0,0,1,0]).dot(m)
pattern[u3] = v3
pattern[v3] = u3

u4 = np.array([1,1,0,0]).dot(m)
v4 = np.array([0,0,1,1]).dot(m)
pattern[u4] = v4
pattern[v4] = u4

u5 = np.array([1,0,1,0]).dot(m)
v5 = np.array([0,1,0,1]).dot(m)
pattern[u5] = v5
pattern[v5] = u5

u6 = np.array([1,1,0,0]).dot(m)
v6 = np.array([0,0,1,1]).dot(m)
pattern[u6] = v6
pattern[v6] = u6

class CheckBoxVideo(QtWidgets.QWidget):
    # On initialise la class, j'imagine...
    def __init__(self, W, H):
        super(CheckBoxVideo, self).__init__()
        self.width = min(W, 50)
        self.height = min(H, 50)
        self.init_size = 10
        self.size_box = 14
        self.status = True
        self.list_cb = []
        self.grid = np.zeros((self.height, self.width)) #np.random.randint(2, size=(self.width, self.height))
        a = np.random.randint(2, size=(self.init_size, self.init_size))
        self.grid[ (self.height-self.init_size)//2:(self.height+self.init_size)//2 , (self.width-self.init_size)//2:(self.width+self.init_size)//2 ] = a
        self.interface()

    def interface(self):
        self.resize(self.width * self.size_box + 6, self.height * self.size_box + 6)
        self.setWindowTitle(u"Automate cellulaire")
        for j in range(self.height):
            for i in range(self.width):
                check_box = QtWidgets.QCheckBox(self)
                check_box.move(i * self.size_box, j * self.size_box)
                self.list_cb.append(check_box)

        self.timer = QtCore.QBasicTimer()
        self.timer.start(40, self) # 25 img/s

        self.show()

    def timerEvent(self, e):
        if self.status:
            for y in range(0, self.height, 2):
                for x in range(0, self.width, 2):
                    decimal_eq = self.grid[y:y + 2, x:x + 2].reshape(1, 4).dot(m)[0]
                    new_decimal = pattern.get(decimal_eq, None)
                    if new_decimal is not None:
                        self.grid[y:y + 2, x:x + 2] = decimal_to_array(new_decimal)
        else:
            for y in range(1, self.height - 1, 2):
                for x in range(1, self.width - 1, 2):
                    decimal_eq = self.grid[y:y + 2, x:x + 2].reshape(1, 4).dot(m)[0]
                    new_decimal = pattern.get(decimal_eq, None)
                    if new_decimal is not None:
                        self.grid[y:y + 2, x:x + 2] = decimal_to_array(new_decimal)
        self.status = not self.status

        for index, checkBox in enumerate(self.list_cb):
            x = index % self.width
            y = index // self.width
            if self.grid[y, x] == 1:
                checkBox.setCheckState(2)
            else:
                checkBox.setCheckState(0)

if __name__ == "__main__":
    appli = QtWidgets.QApplication(sys.argv)
    ckbx = CheckBoxVideo(40,30)
    sys.exit(appli.exec_())