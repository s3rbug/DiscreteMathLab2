import random


class SetLogic:
    def __init__(self):
        self.fields = [set(), set()]  # a, b
        self.all_female_names = ["Ірина", "Марія", "Діана", "Настася", "Іванна", "Богдана", "Влада", "Вікторія", "Анна",
                                 "Христина", "Софія", "Оксана", "Наталя", "Олена", "Зоя"]
        self.all_male_names = ["Іван", "Петро", "Остап", "Максим", "Олександр", "Богдан", "Свят", "Стас", "Дмитро",
                               "Влад", "Олег", "Олексій", "Матвій", "Євген", "Єгор"]
        self.which_to_change = [True, True]

    def get_all_names(self, which):
        if which == 0:
            return self.all_female_names
        else:
            return self.all_male_names

    def add_to_field(self, which, data: set):
        self.fields[which] |= data
        print(self.fields[which])

    def change_first(self, first: bool):
        self.which_to_change = [first, self.which_to_change[1]]

    def change_second(self, second: bool):
        self.which_to_change = [self.which_to_change[0], second]

    def clear_field(self, which):
        self.fields[which] = set()


