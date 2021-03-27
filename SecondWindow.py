from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from SetLogic import SetLogic
from utils import create_folder, numerate
from Person import Person


class SecondWindow(QMainWindow):
    def __init__(self, logic: SetLogic):
        super(SecondWindow, self).__init__()
        uic.loadUi('SecondWindowForm.ui', self)
        self.setWindowTitle("Вікно 2")
        self.logic = logic
        self.all_names_list = [self.list_female, self.list_male]
        self.names_list = [self.list_a, self.list_b]
        self.buttons_gender_save = [self.save_female, self.save_male]
        self.save_buttons = [self.save_a, self.save_b]
        self.radio_buttons = [[self.radio_female_a, self.radio_female_b], [self.radio_male_a, self.radio_male_b]]
        self.clear_buttons = [self.clear_a, self.clear_b]
        for i in numerate(self.buttons_gender_save):
            self.buttons_gender_save[i].clicked.connect(self.save_gender_button(i))
        for i in numerate(self.all_names_list):
            self.initialise_list(i)
        for i in numerate(self.clear_buttons):
            self.clear_buttons[i].clicked.connect(self.clear(i))
        for i in numerate(self.save_buttons):
            self.save_buttons[i].clicked.connect(self.save)
        self.save_to_file.clicked.connect(self.save_file)
        self.load_from_file.clicked.connect(self.load_file)

    def save_file(self):
        create_folder()
        file_a = open('logs/a.txt', 'w')
        file_b = open('logs/b.txt', 'w')
        for i in self.logic.fields[0]:
            file_a.write(i.name + " " + i.sex + "\n")
        for i in self.logic.fields[1]:
            file_b.write(i.name + " " + i.sex + "\n")
        file_a.close()
        file_b.close()

    def load_file(self):
        file_a = open('logs/a.txt', 'r')
        file_b = open('logs/b.txt', 'r')
        for i in file_a:
            name, sex = i.split()
            self.logic.fields[0].append(Person(name, sex))
        for i in file_b:
            name, sex = i.split()
            self.logic.fields[1].append(Person(name, sex))
        self.save()
        file_a.close()
        file_b.close()

    def initialise_list(self, which):
        all_names = self.logic.get_all_names(which)
        current_list = self.all_names_list[which]
        for name in all_names:
            current_list.addItem(name)

    def save(self):
        self.logic.generate_relation(0, self.logic.percent)
        self.logic.generate_relation(1, self.logic.percent)
        self.logic.synchronize()

    def save_gender_button(self, which):
        def foo():
            data = [Person(i.text(), Person.which_sex(which))
                    for i in self.all_names_list[which].selectedItems()]
            self.logic.add_to_field(0 if self.radio_buttons[which][0].isChecked() else 1, frozenset(data))
            self.add_value(which)
            self.update_value()

        return foo

    def update_value(self):
        for which in numerate(self.logic.fields):
            self.names_list[which].clear()
            for i in self.logic.fields[which]:
                self.names_list[which].addItem(i.get_name())

    def add_value(self, which):
        name_list = self.list_a if self.radio_buttons[which][0].isChecked() else self.list_b
        name_list.clear()
        for i in self.logic.fields[which]:
            name_list.addItem(i.get_name())
        self.save()

    def clear(self, which):
        def foo():
            self.logic.clear_field(which)
            self.update_value()
        return foo
