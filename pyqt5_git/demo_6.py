#status bar

from PyQt5.QtWidgets import QApplication, QStatusBar, QMainWindow

class window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.Initui()

    def Initui(self):
        self.statusBar().showMessage("status is ready")
        self.setWindowTitle("scandat")
        self.setGeometry(100,200,100,150)
        self.show()

def main():
    app = QApplication([])
    ex = window()
    app.exec_()

if __name__=="__main__":
    main()