import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5 import QtWidgets, uic
from SecondWindow import SecondWindow
from ThirdWindow import ThirdWindow
from FourthWindow import FourthWindow
from SetLogic import SetLogic
from utils import show_message


def print_variant():
    g = 1  # Номер групи
    n = 2  # Номер у списку групи
    m = "IO"
    output = "Ім'я: Бугайчук Сергій Володимирович\n" + \
             "Група: " + str(m) + "-" + ("0" if g < 10 else "") + str(g) + \
             "\nНомер у групі: " + str(n)
    if m == "IO":
        n += 1
    variant = (n + g % 60) % 30 + 1
    output += "\nВаріант: " + str(variant)
    show_message(output, QMessageBox.Information)


class MainWindow(QtWidgets.QMainWindow):
    def open_window(self, which):
        def foo():
            self.windows[which].show()
        return foo

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('MainWindowForm.ui', self)
        self.setWindowTitle("Вікно 1")
        self.logic = SetLogic()
        self.windows = [SecondWindow(self.logic), ThirdWindow(), FourthWindow()]
        self.window_buttons = [self.window_button2, self.window_button3, self.window_button4]
        for i in range(len(self.window_buttons)):
            self.window_buttons[i].clicked.connect(self.open_window(i))
        self.information.triggered.connect(print_variant)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    font_database = QFontDatabase()
    font_database.addApplicationFont("./assets/Lucida Grande.ttf")
    font = QFont("Lucida Grande")
    QApplication.setFont(font)
    widget = MainWindow()
    app.exec_()
