class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

# single level inheritance
class B(A):
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

# multi level inheritance
class C(B):
    def feature5(self):
        print("Feature 5 is working")


class D:
    def feature6(self):
        print("Feature 6 is working")

# multiple inheritance
class E(A,D):
    def feature7(self):
        print("Fetaure 7 is working")


a1 = A()
b = B()
c = C()
d = D()
e = E()
a1.feature1()
a1.feature2()
b.feature4()
b.feature1()
c.feature2()
d.feature6()
e.feature2()
e.feature7()