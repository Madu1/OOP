class Student:
    # class variable
    school = "St. Clare"

    def __init__(self, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    # instance methods
    def calc_avg(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3.0

    # accessors
    def get_mark1(self):
        return self.mark1

    # mutators
    def set_mark1(self, m1):
        self.mark1 = m1

    # class method
    @classmethod
    def print_school_name(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is a static method.")


s1 = Student(36, 65, 98)
s2 = Student(41, 85, 95)
print(s1.calc_avg())
print(s2.calc_avg())
print(s1.get_mark1())
s1.set_mark1(82)
print(s1.get_mark1())
print(Student.print_school_name())
Student.info()
