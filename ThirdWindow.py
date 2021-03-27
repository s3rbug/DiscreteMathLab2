from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from SetLogic import SetLogic
from utils import numerate, center_item
from Person import Person


class ThirdWindow(QMainWindow):
    def __init__(self, logic: SetLogic):
        super(ThirdWindow, self).__init__()
        uic.loadUi('ThirdWindowForm.ui', self)
        self.setWindowTitle("Вікно 3")
        self.logic = logic
        self.tables = [self.table_s, self.table_r]
        self.names_list = [self.list_a, self.list_b]

    def update_value(self):
        # load tables
        for i in numerate(self.tables):
            self.tables[i].setRowCount(len(self.logic.fields[0]))
            self.tables[i].setColumnCount(len(self.logic.fields[1]))
            self.tables[i].setVerticalHeaderLabels(Person.list_str(self.logic.fields[0]))
            self.tables[i].setHorizontalHeaderLabels(Person.list_str(self.logic.fields[1]))
            for j in numerate(self.logic.fields[0]):
                for k in numerate(self.logic.fields[1]):
                    self.tables[i].setItem(j, k, center_item(self.logic.relations[i][j][k]))
        # load A and B
        for which in numerate(self.logic.fields):
            self.names_list[which].clear()
            for i in self.logic.fields[which]:
                self.names_list[which].addItem(i.get_name())
