from PyQt5.QtWidgets import *

app = QApplication([])
button = QPushButton("click")

def on_click_button():
    msg = QMessageBox()
    msg.setText("you click the button")
    msg.exec_()

button.clicked.connect(on_click_button)
button.show()
app.exec_()