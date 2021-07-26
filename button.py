"""
from tkinter import *
root = Tk()
root.geometry('500x500')
btn = Button(root, text ='Bluetooth', bd='5', command=root.destroy, bg='lightblue')
btn.pack(side='bottom')
root.mainloop()
"""
# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("bluetooth")

		# setting geometry
		self.setGeometry(100, 100, 600, 400)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for widgets
	def UiComponents(self):

		# creating a push button
		button = QPushButton("Bluetooth", self)

		# setting geometry of button
		button.setGeometry(200, 150, 100, 30)

		# adding action to a button
		button.clicked.connect(self.clickme)

	# action method
	def clickme(self):

		# printing pressed
		print("pressed")

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
