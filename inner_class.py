class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.age)

    class Laptop:
        def __init__(self):
            self.brand = "hp"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Mary", 15)
s2 = Student("Jake", 16)
lap1 = Student.Laptop()
s1.show()
s1.lap.show()
