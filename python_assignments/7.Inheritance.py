# Method-based Inheritance Demo
class A:
    def feature1(self):
        print("A - Feature1")

    def feature2(self):
        print("A - Feature2")

    def common(self):
        print("A - Overridden Method")

class B(A):
    def feature3(self):
        print("B - Feature3")

    def feature4(self):
        print("B - Feature4")

    def common(self):
        print("B - Overridden Method")

class C(B):
    def feature5(self):
        print("C - Feature5")

    def feature6(self):
        print("C - Feature6")

    def common(self):
        print("C - Overridden Method")

# Object creation and method calling
a = A()
b = B()
c = C()

print("\nClass A Methods:")
a.feature1()
a.feature2()
a.common()

print("\nClass B Methods:")
b.feature1()
b.feature2()
b.feature3()
b.feature4()
b.common()

print("\nClass C Methods:")
c.feature1()
c.feature2()
c.feature3()
c.feature4()
c.feature5()
c.feature6()
c.common()

# Polymorphism
print("\nRuntime Polymorphism with super class reference:")
ref: A = B()
ref.common()

ref = C()
ref.common()


#Runtime Polymorphism with data members(attributes):
class A1:
    val = "A value"

class B1(A1):
    val = "B value"

class C1(B1):
    val = "C value"

# Accessing via instances
a1 = A1()
b1 = B1()
c1 = C1()

print("\nData Members:")
print("A1 val:", a1.val)
print("B1 val:", b1.val)
print("C1 val:", c1.val)

# Superclass reference to subclass
ref: A1 = B1()
print("ref (A1 to B1) val:", ref.val)

ref = C1()
print("ref (A1 to C1) val:", ref.val)
