import sys
import bluetooth
import PyQt5
import Blsocket
import gui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

uid_list = bluetooth.discover_devices()
print(uid_list)

class App(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.listWidget.itemSelectionChanged.connect(self.handle_selection_change)
        self.listWidget.addItems(uid_list)

    def handle_selection_change(self):
        selected_items = self.listWidget.selectedItems()
        for item in selected_items:
            print(item.text())

            if Blsocket.Blsocket.connectToGlove(item.text()):
                print('true')
                Blsocket.Blsocket.recvData(True)
    
    

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

    
