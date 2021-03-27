from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from SetLogic import SetLogic
from utils import numerate, center_item
from Person import Person


class FourthWindow(QMainWindow):
    def __init__(self, logic: SetLogic):
        super(FourthWindow, self).__init__()
        uic.loadUi('FourthWindowForm.ui', self)
        self.setWindowTitle("Вікно 4")
        self.logic = logic
        self.radio_buttons = [self.radio_union, self.radio_inter, self.radio_difference1,
                              self.radio_difference2, self.radio_reverse]
        self.radio_group.buttonClicked.connect(self.update_value)

    def update_value(self):
        which = 0
        for i in numerate(self.radio_buttons):
            if self.radio_buttons[i].isChecked():
                self.logic.set_relation(i)
                which = i
                break
        if which == 4:
            self.table.setRowCount(len(self.logic.fields[1]))
            self.table.setColumnCount(len(self.logic.fields[0]))
            self.table.setVerticalHeaderLabels(Person.list_str(self.logic.fields[1]))
            self.table.setHorizontalHeaderLabels(Person.list_str(self.logic.fields[0]))
        else:
            self.table.setRowCount(len(self.logic.fields[0]))
            self.table.setColumnCount(len(self.logic.fields[1]))
            self.table.setVerticalHeaderLabels(Person.list_str(self.logic.fields[0]))
            self.table.setHorizontalHeaderLabels(Person.list_str(self.logic.fields[1]))
        for i in numerate(self.logic.result_relation):
            for j in numerate(self.logic.result_relation[i]):
                self.table.setItem(i, j, center_item(self.logic.result_relation[i][j]))
