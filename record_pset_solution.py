class Record:

    def __init__(self,forename,surname,age,gender,cs_student):
        self.__forename = forename
        self.__surname = surname
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        else:
            self.__age = age
        self.__gender = gender
        if cs_student not in ["True","False"]:
            raise ValueError("CS Student must be 'True' or 'False'")
        else:
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
