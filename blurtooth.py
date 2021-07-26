
import bluetooth

target_name = "OPPO A5 2020"
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print("found target bluetooth device with address "), target_address
else:
    print("could not find target bluetooth device nearby")

"""
import sys
import signal

from PyQt5 import QtBluetooth as QTBt
from PyQt5 import QtCore

class Application(QtCore.QCoreApplication):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.scan_for_device()
        self.exec()

    def displaystatus(self):
        print(self.agent.isActive(), self.agent.discoveredDevices())

    def foo(self, *args, **kwargs):
        print('foo', args, kwargs)

    def scan_for_devices(self):
        self.agent = QTBt.QBluetoothDeviceDiscoveryAgent(self)
        self.agent.deviceDiscovered.connect(self.foo)
        self.agent.finished.connect(self.foo)
        self.agent.error.connect(self.foo)
        self.agent.setLowEnergyDiscoveryTimeout(1000)
        
        
        timer = QtCore.QTimer(self.agent)
        timer.start(500)
        timer.timeout.connect(self.display_status)

        self.agent.start()
        
if __name__ == '__main__':
        import sys
        app = Application(sys.argv)
        









import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtBluetooth

class bluetoothTest(QWidget):

    def __init__(self, parent = None):
        super(bluetoothTest, self).__init__(parent)
        self.connectToRobot()
        self.win = QWidget()
        self.win.show()

    def connectToRobot(self):
        self.sock = QtBluetooth.QBluetoothSocket(QtBluetooth.QBluetoothServiceInfo.RfcommProtocol)

        self.sock.connected.connect(self.connectedToBluetooth)
        self.sock.readyRead.connect(self.receivedBluetoothMessage)
        self.sock.disconnected.connect(self.disconnectedFromBluetooth)
        self.sock.error.connect(self.socketError)
        port = 1
        self.sock.connectToService(QtBluetooth.QBluetoothAddress("98:D3:C1:FD:2C:46"),port)

    def socketError(self,error):
        print(self.sock.errorString())

    def connectedToBluetooth(self):
        self.sock.write('A'.encode())

    def disconnectedFromBluetooth(self):
        self.print('Disconnected from bluetooth')

    def receivedBluetoothMessage(self):
        while self.sock.canReadLine():
            line = self.sock.readLine()
            print(str(line, "utf-8"))

def main():
    # deal with a bluetooth bug on mac
    if sys.platform == 'darwin':
        os.environ['QT_EVENT_DISPATCHER_CORE_FOUNDATION'] = '1'

    app = QApplication(sys.argv)
    ex = bluetoothTest()
    sys.exit(app.exec_())

if __name__ == '__main__':
        main()

"""