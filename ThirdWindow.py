from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from SetLogic import SetLogic
from utils import show_message, create_folder


class ThirdWindow(QMainWindow):
    def __init__(self):
        super(ThirdWindow, self).__init__()
        uic.loadUi('ThirdWindowForm.ui', self)
        self.setWindowTitle("Вікно 3")
