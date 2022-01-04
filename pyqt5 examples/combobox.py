import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw

class mainwindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("combobox")

        self.setLayout(qtw.QVBoxLayout())

        label = qtw.QLabel("this is my label")
        label.setFont(qtg.QFont('arial', 18))
        self.layout().addWidget(label)

        my_combo = qtw.QComboBox(self, editable = True)
        my_combo.addItem("pepper", "something")
        my_combo.addItem("chilly", 2)
        my_combo.addItem("brwny", qtw.QWidget)
        my_combo.addItem("choclate")


        my_button = qtw.QPushButton("press me!", clicked = lambda :pressed_it())
        self.layout().addWidget(my_button)

        self.show()

        def pressed_it():
            label.setText(f"you picked {my_combo.currentText()}!")

app = qtw.QApplication([])
mw = mainwindow()

app.exec_()

