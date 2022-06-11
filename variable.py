class Car:
    # class or static variable
    wheel = 4

    def __init__(self, mil, com):
        # instance variables
        self.mil = mil
        self.com = com


car1 = Car("10", "BMW")
car2 = Car("15", "Audi")

print(Car.wheel)
Car.wheel = 5
print(car1.mil, car2.wheel)  # can call the class variable by object
print(car2.mil, Car.wheel)  # call the class variable by using class name
