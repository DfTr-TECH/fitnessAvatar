import sys
import bluetooth
import PyQt5
import gui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

uid_list = bluetooth.discover_devices()
print(uid_list)
class App(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
        self.listWidget.addItems(uid_list)
        

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = App()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__': 
    print(App.listWidget.selectedItems()) # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
    
