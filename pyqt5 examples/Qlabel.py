import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    l1 = QLabel()
    l2 = QLabel()
    l3 = QLabel()
    l4 = QLabel()

    l1.setText("welcome to weeroda")
    l2.setText("Scandat Studio")
    l4.setText("weeroda.com")

    l1.setAlignment(Qt.AlignCenter)
    l3.setAlignment(Qt.AlignCenter)
    l4.setAlignment(Qt.AlignRight)
    l3.setPixmap(QPixmap("logo.png"))

    vbox = QVBoxLayout()
    vbox.addWidget(l1)
    vbox.addStretch()
    vbox.addWidget(l2)
    vbox.addStretch()
    vbox.addWidget(l3)
    vbox.addStretch()
    vbox.addWidget(l4)

    l1.setOpenExternalLinks(True)
    l2.linkHovered.connect(hovered)
    l4.linkActivated.connect(clicked)
    l1.setTextInteractionFlags(Qt.TextSelectableByMouse)
    win.setLayout(vbox)

    win.setWindowTitle(" scandat studio ")
    win.setGeometry(100,100,300,200)
    win.show()
    sys.exit(app.exec())

def hovered():
    print("hovered")

def clicked():
    print("clicked")

if __name__ == "__main__":
    window()