# a = '5'
# b ='6'
#
# print(a + b)
# print(str.__add__(a, b))

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # Operator Overloading
    def __add__(self, other):
        s1 = self.m1 + other.m1
        s2 = self.m2 + other.m2
        s3 = Student(s1, s2)

        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    # Operator Overriding
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)




s1 = Student(45, 56)
s2 = Student(7, 7)
s3 = s1 + s2

if s1 > s2:
    print("S1 wins")
else:
    print("S2 wins")


a = 8
print(a.__str__())

print(s1)
print(s2)