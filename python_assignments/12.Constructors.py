# 1. Class with multiple constructors using __init__ and class methods
class MyClass:
    # Default constructor
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            print("Default Constructor Called")
        elif b is None:
            print(f"One Argument Constructor Called with a={a}")
        else:
            print(f"Two Argument Constructor Called with a={a}, b={b}")

# 2. Superclass and subclass with constructor calls
class SuperClass:
    # Public constructor
    def __init__(self, x=None):
        if x is None:
            print("SuperClass Default Constructor")
        else:
            print(f"SuperClass Parameterized Constructor with x={x}")

class ChildClass(SuperClass):
    # Call super class constructors explicitly
    def __init__(self, x=None, y=None):
        if x is None and y is None:
            print("ChildClass Default Constructor")
            super().__init__()  # Call superclass default constructor
        elif y is None:
            print(f"ChildClass One Argument Constructor with x={x}")
            super().__init__(x)  # Call superclass parameterized constructor
        else:
            print(f"ChildClass Two Argument Constructor with x={x}, y={y}")
            super().__init__(x)  # Call superclass parameterized constructor

# 3. Demonstrate private, protected, public constructor equivalents in Python
class AccessModifiers:
    def __init__(self):
        print("Public Constructor")

    @classmethod
    def _protected_constructor(cls):
        print("Protected-like Constructor (by convention)")

    @classmethod
    def __private_constructor(cls):
        print("Private-like Constructor (name mangled)")

    # Access private constructor from inside class
    def access_private(self):
        self.__private_constructor()

# 4. Attributes of constructor: setting object attributes during construction
class AttributesDemo:
    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age = age     # instance attribute
        print(f"Constructor called: Name={self.name}, Age={self.age}")

# Main to instantiate and demonstrate all

def main():
    print("1. Multiple constructors demonstration:")
    obj1 = MyClass()
    obj2 = MyClass(10)
    obj3 = MyClass(10, 20)

    print("\n2. Super and Child class constructors:")
    child1 = ChildClass()
    child2 = ChildClass(5)
    child3 = ChildClass(5, 15)

    print("\n3. Access modifiers in constructor:")
    am = AccessModifiers()
    am._protected_constructor()  # Access protected by convention
    am.access_private()          # Access private inside class
    

    print("\n4. Constructor attributes:")
    person = AttributesDemo("Alice", 30)

if __name__ == "__main__":
    main()
