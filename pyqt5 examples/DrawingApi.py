import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class mainwindow(QWidget):

    def __init__(self):
        super(mainwindow, self).__init__()
        self.Initui()

    def Initui(self):
        self.text = "welcome to weeroda"
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("weeroda")
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(Qt.red))
        qp.setFont(QFont('Arial', 20))
        qp.drawText(10,20, 'welcome to weeroda')
        qp.setPen(QColor(Qt.blue))
        qp.drawLine(10,100,100,100)
        qp.drawRect(10,150,150,100)
        qp.setPen(QColor(Qt.yellow))
        qp.drawEllipse(230,25,120,100)
        qp.drawPixmap(250,50,QPixmap("logo.png"))
        qp.fillRect(20,175,130,70,QBrush(Qt.SolidPattern))
        qp.end()


def main():
    app = QApplication(sys.argv)
    ex = mainwindow()
    ex.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()