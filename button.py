"""
from tkinter import *
root = Tk()
root.geometry('500x500')
btn = Button(root, text ='Bluetooth', bd='5', command=root.destroy, bg='lightblue')
btn.pack(side='bottom')
root.mainloop()

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

import sys
from PyQt5 import QtBluetooth as QtBt
from PyQt5 import QtCore


class Application(QtCore.QCoreApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scan_for_devices()
        self.exec()

    def display_status(self):
        print(self.agent.isActive(), self.agent.discoveredDevices())

    def show_info(self, info: QtBt.QBluetoothDeviceInfo):
        print('Device discovered')
        print(info)
        print(f'Name: {info.name()}')
        print(f'UUID: {info.deviceUuid()}')
        pass

    def agent_finished(self,*args, **kwargs):
        print('Agent finished')
        print(f'args {args}')
        print(f'kwargs {kwargs}')

    def agent_error(self,*args, **kwargs):
        print('Agent error')
        print(f'args {args}')
        print(f'kwargs {kwargs}')

    def scan_for_devices(self):
        self.agent = QtBt.QBluetoothDeviceDiscoveryAgent()
        self.agent.setLowEnergyDiscoveryTimeout(5000)

        self.agent.deviceDiscovered.connect(self.show_info)
        self.agent.finished.connect(self.agent_finished)
        self.agent.error.connect(self.agent_error)

        timer = QtCore.QTimer(self.agent)
        timer.start(1000)
        timer.timeout.connect(self.display_status)

        self.agent.start()


if __name__ == '__main__':
    app = Application(sys.argv)

    """
import bluetooth

target_name = "OPPO A5 2020"
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print ("found target bluetooth device with address ", target_address)
else:
    print ("could not find target bluetooth device nearby")
