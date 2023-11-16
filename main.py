from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random
import sys


class Zadacha(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        qp = QPainter
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(random.randint(1, 20))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Zadacha()
    ex.show()
    sys.exit(app.exec_())
