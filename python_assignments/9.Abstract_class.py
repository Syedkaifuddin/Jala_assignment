from abc import ABC, abstractmethod

# 1. Abstract class with abstract and non-abstract methods
class AbstractBase(ABC):
    def non_abstract_method(self):
        print("Non-Abstract Method Called from AbstractBase")

    @abstractmethod
    def abstract_method(self):
        pass

# 2, 3, 4. Subclass of abstract class
class ChildClass(AbstractBase):
    def abstract_method(self):
        print("Abstract Method Implemented in ChildClass")

    def call_abstract_method(self):
        print("\nCalling abstract method via child instance:")
        self.abstract_method()

    def call_non_abstract_method(self):
        print("Calling non-abstract method via child instance:")
        self.non_abstract_method()


# Main logic simulating Java-style main method
if __name__ == "__main__":
    print("2. Accessing non-abstract method using abstract class reference:")
    obj: AbstractBase = ChildClass()
    obj.non_abstract_method()

    print("\n3. Calling abstract method from child class:")
    child = ChildClass()
    child.call_abstract_method()

    print("\n4. Calling non-abstract method from child class:")
    child.call_non_abstract_method()
