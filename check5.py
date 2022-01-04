import sys
import os
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.layoutH = QHBoxLayout()
        img_folder_path = 'G:/Scandat/sacndat_studio/Templates'
        dirListing = os.listdir(img_folder_path)

        for i in dirListing:
            self.checkbox = QCheckBox("chBox-{}".format(i))
            self.checkbox.setCheckState(Qt.Unchecked)

            self.layoutH.addWidget(self.checkbox)
            self.layoutH.setAlignment(Qt.AlignCenter)

        self.label  = QLabel("selected QCheckBox: ")
        self.button = QPushButton("Query whether or not a checkbox is checked")
        self.button.clicked.connect(self.ButtonClicked)

        layoutV     = QVBoxLayout(self)
        layoutV.addLayout(self.layoutH)
        layoutV.addWidget(self.label)
        layoutV.addWidget(self.button)

    def ButtonClicked(self):
        checked_list = []

        for i in range(self.layoutH.count()):
            chBox = self.layoutH.itemAt(i).widget()
            if chBox.isChecked():
                checked_list.append(chBox.text())
        self.label.setText("selected QCheckBox: " + str(list(checked_list)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.resize(350, 300)
    window.show()
    sys.exit(app.exec_())