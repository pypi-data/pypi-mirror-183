import sys, os, random
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib
import matplotlib.pyplot as plt

import pycar.audio as audio
import pycar.carserial as car

class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()
        self.figure = matplotlib.figure.Figure()
        self.canvas = FigureCanvas(self.figure)
        vbox.addWidget(self.canvas)
        self.setLayout(vbox)
        self.axes = []
        for i in range(5):
            ax = self.figure.add_subplot(5,1,i+1)
            self.axes.append(ax)

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        hbox = QHBoxLayout()

        self.cbAudio = QComboBox()
        self.ADevs = audio.get_devices()
        self.cbAudio.addItems(list(map(lambda dev: dev[1]["name"], self.ADevs)))
        self.cbAudio.currentIndexChanged.connect(self.changeAudio)
        hbox.addWidget(self.cbAudio)

        self.cbCom = QComboBox()
        self.CPorts = car.get_ports()
        self.cbCom.addItems(self.CPorts)
        hbox.addWidget(self.cbCom)

        self.setLayout(hbox)
        self.setWindowTitle("EPO4 Manual Control")

    def changeAudio(self, checked):
        self.plotwin = PlotWidget()
        self.plotwin.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWidget()
    mw.show()
    sys.exit(app.exec_())
