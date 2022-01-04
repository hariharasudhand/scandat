# L = ["Geeks\n", "for\n", "Geeks\n"]
#
# # writing to file
# file1 = open('myfile.txt', 'w')
# file1.writelines(L)
# file1.close()
#
# # Using readlines()
# file1 = open('file.txt', 'r')
# Lines = file1.readlines()
# print(len(Lines))
# count = 0
# # Strips the newline character
# for line in Lines:
#     count += 1
#     print("Line{}: {}".format(count, line.strip()))


# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Python ")

		# setting geometry
		self.setGeometry(100, 100, 600, 400)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for widgets
	def UiComponents(self):

		# creating a push button
		button = QPushButton("pressed", self)

		# setting geometry of button
		button.setGeometry(200, 150, 100, 40)

		# adding action to a button
		button.clicked.connect(self.clickme)

		# getting text in button
		text = button.text()

		# creating label to print text
		label = QLabel(text, self)
		label.move(200, 200)

	# action method
	def clickme(self):

		# printing pressed
		print("click")

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
