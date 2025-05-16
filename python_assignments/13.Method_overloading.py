class MethodOverloadingDemo:
    
    # 1. Methods with same name, different number of parameters (same type)
    def method(self, a, b=None):
        if b is not None:
            print(f"Method called with two parameters: a={a}, b={b}")
        else:
            print(f"Method called with one parameter: a={a}")

    # 2. Methods with same name, different number of parameters, different data types
    # Using single method with type check
    def method_diff_types(self, a, b=None):
        if b is None:
            if isinstance(a, int):
                print(f"Method called with int parameter: a={a}")
            elif isinstance(a, str):
                print(f"Method called with string parameter: a={a}")
            else:
                print("Method called with unknown type")
        else:
            print(f"Method called with two parameters of different types: a={a}, b={b}")

    # 3. Methods with same name and same number of parameters (same type)
    # This is not possible in Python as the latter method overwrites the former
    # So we simulate with type checks or different method names
    def method_same_params_1(self, a, b):
        print(f"Method 1 with parameters: a={a}, b={b}")

    def method_same_params_2(self, a, b):
        print(f"Method 2 with parameters: a={a}, b={b}")

# Testing the class
obj = MethodOverloadingDemo()

# 1.
obj.method(10)
obj.method(10, 20)

# 2.
obj.method_diff_types(10)
obj.method_diff_types("hello")
obj.method_diff_types(10, "world")

# 3.
obj.method_same_params_1(1, 2)
obj.method_same_params_2(3, 4)
