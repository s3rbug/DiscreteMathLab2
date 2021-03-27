from utils import bool_chance


class SetLogic:
    def __init__(self):
        self.synchronize = None
        self.percent = 0.8
        self.fields = [list(), list()]  # a, b
        self.relations = [[], []]  # S, R
        self.result_relation = []
        self.all_female_names = ["Ірина", "Марія", "Діана", "Настася", "Іванна", "Богдана", "Влада", "Вікторія", "Анна",
                                 "Христина", "Софія", "Оксана", "Наталя", "Олена", "Зоя"]
        self.all_male_names = ["Іван", "Петро", "Остап", "Максим", "Олександр", "Богдан", "Свят", "Стас", "Дмитро",
                               "Влад", "Олег", "Олексій", "Матвій", "Євген", "Єгор"]

    def get_all_names(self, which):
        if which == 0:
            return self.all_female_names
        else:
            return self.all_male_names

    def set_synchronize(self, synchronize):
        self.synchronize = synchronize

    def add_to_field(self, which, data: frozenset):
        self.fields[which] = list(data | frozenset(self.fields[which]))

    def clear_field(self, which):
        self.fields[which] = list()

    def generate_relation(self, which, chance):
        n = len(self.fields[0])
        m = len(self.fields[1])
        result_relation = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if self.fields[0][i].get_name() == self.fields[1][j].get_name():
                    continue
                elif which == 0:
                    if self.fields[0][i].is_female() and self.fields[1][j].is_female() and bool_chance(chance):
                        result_relation[i][j] = 1
                elif which == 1:
                    if bool_chance(chance):
                        if self.fields[0][i].is_female() != self.fields[1][j].is_female():
                            result_relation[i][j] = 1
        self.relations[which] = result_relation.copy()

    def set_relation(self, which):
        n = len(self.fields[0])
        m = len(self.fields[1])
        if which == 4:
            result_relation = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    result_relation[i][j] = self.relations[0][j][i]
        else:
            result_relation = [[0 for _ in range(m)] for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if which == 0:
                        if self.relations[0][i][j] == 1 or self.relations[1][i][j] == 1:
                            result_relation[i][j] = 1
                    elif which == 1:
                        if self.relations[0][i][j] == 1 and self.relations[1][i][j] == 1:
                            result_relation[i][j] = 1
                    elif which == 2:
                        if self.relations[0][i][j] == 0 and self.relations[1][i][j] == 1:
                            result_relation[i][j] = 1
                    elif which == 3:
                        result_relation[i][j] = 0 if self.relations[1][i][j] == 1 else 1
        self.result_relation = result_relation.copy()


