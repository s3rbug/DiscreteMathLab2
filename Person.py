class Person:
    def __init__(self, name="", sex=""):
        self.name = name
        self.sex = sex

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def is_female(self):
        return self.sex == "Female"

    @staticmethod
    def which_sex(which: int):
        return "Female" if which == 0 else "Male"

    @staticmethod
    def list_str(people: list):
        return [person.name for person in people]
