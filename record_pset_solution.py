class Record:

    def __init__(self,forename,surname,age,gender,cs_student):
        self.__forename = forename
        self.__surname = surname
        self.__age = age
        self.__gender = gender
        self.__cs_student = cs_student

    def get_forename(self):
        return self.__forename

    def set_surname(self,surename):
        self.__surname = surname
        return self.__surname

    def get_surname(self):
        return self.__surname

    def set_age(self,age):
        self.__age = age
        return self.__age

    def get_forename(self):
        return self.__forename

    def set_forename(self,forename):
        self.__forename = forename
        return self.__forename



mark = Record("Mark","Wood",39,"M","True")
print(mark.get_forename())
print(mark.set_forename("Dave"))
