class Student(object):
    """
    This creates a student object with specified name and ID.
    Students name will be a String
    Student ID will be an Int
    """
    UNITS_TO_GRADUATE = 180.00

    def __init__(self, name, stuid):
        self.__set_name(name)
        self.__set_id(stuid)
        self.units_earned = 10

    def has_enough_units(self):
        if self.units_earned >= self.UNITS_TO_GRADUATE:
            print(f'{self.get_name()} has all the units they need to graduate!')
        else:
            print(f'{self.get_name()} does not have the units they need at this time.')

    def profile(self):
        print(f'Student Name: {self.get_name()}  ID # {self.get_id()}')

    def get_name(self):
        return self.__name

    def __set_name(self, name):
        self.__name = name

    name = property(get_name, __set_name)

    def get_id(self):
        return self.__id

    def __set_id(self, stuid):
        self.__id = stuid

    id = property(get_id, __set_id)

    def units_earned(self):
        print(self.units_earned)

    def set_units(self, units):
        self.units_earned = units

    units = property(units_earned, set_units)


class Frosh(Student):
    def __init__(self, name, stuid):
        super().__init__(name, stuid)
        self.set_units(0)

    def profile(self):
        print(f'Dawww look, it\'s a wee little freshman Student Name: {self.get_name()}  ID # {self.get_id()}')
