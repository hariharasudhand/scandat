# importing the required libraries

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		# set the title
		self.setWindowTitle("Label")

		# setting the geometry of window
		self.setGeometry(0, 0, 400, 300)

		# creating a label widget
		# by default label will display at top left corner
		self.label_1 = QLabel('Arial font', self)

		# moving position
		self.label_1.move(400, 100)

		# setting font and size
		self.label_1.setFont(QFont('Arial', 10))

		# creating a label widget
		# by default label will display at top left corner
		self.label_2 = QLabel('Times font', self)

		# moving position
		self.label_2.move(100, 120)

		# setting font and size
		self.label_2.setFont(QFont('Times', 10))


		# show all the widgets
		self.show()



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
