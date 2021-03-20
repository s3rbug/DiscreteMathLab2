from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from SetLogic import SetLogic
from utils import show_message, create_folder


class SecondWindow(QMainWindow):
    def initialise_list(self, which):
        all_names = self.logic.get_all_names(which)
        current_list = self.all_names_list[which]
        for name in all_names:
            current_list.addItem(name)

    def save(self, which):
        def foo():
            data = [i.text() for i in self.all_names_list[which].selectedItems()]
            self.logic.add_to_field(0 if self.logic.which_to_change[which] else 1, set(data))
            self.add_value(which)
            self.update_value()
            for i in data:
                print(i)

        return foo

    def update_value(self):
        for which in range(len(self.logic.fields)):
            self.names_list[which].clear()
            for i in self.logic.fields[which]:
                self.names_list[which].addItem(i)

    def add_value(self, which):
        name_list = self.list_a if self.logic.which_to_change[which] else self.list_b
        name_list.clear()
        for i in self.logic.fields[which]:
            name_list.addItem(i)

    def test(self, which):
        def foo():
            if which == 0:
                self.logic.change_first(self.radio_buttons[which][0].isChecked())
            else:
                self.logic.change_second(self.radio_buttons[which][0].isChecked())

        return foo

    def clear(self, which):
        def foo():
            self.logic.clear_field(which)
        return foo

    def __init__(self, logic: SetLogic):
        super(SecondWindow, self).__init__()
        uic.loadUi('SecondWindowForm.ui', self)
        self.setWindowTitle("Вікно 2")
        self.logic = logic
        self.all_names_list = [self.list_female, self.list_male]
        self.names_list = [self.list_a, self.list_b]
        self.save_buttons = [self.save_female, self.save_male]
        self.button_groups = [self.button_group_female, self.button_group_male]
        self.radio_buttons = [[self.radio_female_a, self.radio_female_b], [self.radio_male_a, self.radio_male_b]]
        for i in range(len(self.save_buttons)):
            self.save_buttons[i].clicked.connect(self.save(i))
        for i in range(len(self.all_names_list)):
            self.initialise_list(i)
        for i in range(len(self.button_groups)):
            self.button_groups[i].buttonClicked.connect(self.test(i))
