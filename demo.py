class Computer:

    def __init__(self):
        self.name = "Ravi"
        self.age = 28

    def update(self):
        self.age = 23

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


com1 = Computer()
com2 = Computer()
com2.update()

if com1.compare(com2): 
    print("They are same")
else:
    print("They are different")

# com2 age
print(com2.age)
print(com1.name)
print(com2.name)
# after calling update method
# com2.update()
# updated age of com2
# print(com2.age)
print(com1.age)

# Computer.config(com2)
