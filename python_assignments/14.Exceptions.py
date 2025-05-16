# 14.Exceptions.py

# 1. Generate Arithmetic Exception without handling
def arithmetic_exception_no_handling():
    print("1. Generating Arithmetic Exception (division by zero) without handling:")
    result = 10 / 0  # This will cause ZeroDivisionError in Python
    print(result)

# 2. Handle Arithmetic Exception with try-except
def handle_arithmetic_exception():
    print("\n2. Handling Arithmetic Exception:")
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print("Caught exception:", e)

# 3. Method that throws exception, called without try block
def method_throws_exception():
    raise ValueError("This is a manually raised exception")

def call_method_without_handling():
    print("\n3. Calling method that throws exception without try block:")
    method_throws_exception()  # Will crash if not caught

# 4. Multiple except blocks example
def multiple_catch_blocks():
    print("\n4. Multiple except blocks:")
    try:
        val = int("hello")  # ValueError
    except ZeroDivisionError:
        print("Caught ZeroDivisionError")
    except ValueError:
        print("Caught ValueError")
    except Exception as e:
        print("Caught generic exception:", e)

# 5. Throw exception with your own message
def throw_exception_with_message():
    print("\n5. Throw exception with custom message:")
    try:
        raise RuntimeError("Custom runtime error message")
    except RuntimeError as e:
        print("Caught exception:", e)

# 6. Create your own exception
class MyCustomException(Exception):
    pass

def custom_exception_program():
    print("\n6. Custom exception example:")
    try:
        raise MyCustomException("This is my custom exception")
    except MyCustomException as e:
        print("Caught custom exception:", e)

# 7. Program with finally block
def program_with_finally():
    print("\n7. Program with finally block:")
    try:
        x = 1 / 1
        print("Try block executed successfully")
    except ZeroDivisionError:
        print("Exception caught")
    finally:
        print("Finally block always executed")

# 8. Generate Arithmetic Exception (same as 1)
def generate_arithmetic_exception():
    print("\n8. Generating Arithmetic Exception:")
    try:
        x = 5 / 0
    except ZeroDivisionError as e:
        print("Caught exception:", e)

# 9. Generate FileNotFoundException (FileNotFoundError in Python)
def generate_filenotfound_exception():
    print("\n9. Generating FileNotFoundException:")
    try:
        with open("non_existent_file.txt", "r") as f:
            pass
    except FileNotFoundError as e:
        print("Caught exception:", e)

# 10. Generate ClassNotFoundException analog in Python (ModuleNotFoundError)
def generate_classnotfound_exception():
    print("\n10. Generating ClassNotFoundException analog (ModuleNotFoundError):")
    try:
        import some_non_existent_module
    except ModuleNotFoundError as e:
        print("Caught exception:", e)

# 11. Generate IOException analog in Python (IOError or OSError)
def generate_ioexception():
    print("\n11. Generating IOException analog (IOError/OSError):")
    try:
        # Trying to write to a directory path will raise an IOError/OSError
        with open("/", "w") as f:
            pass
    except (IOError, OSError) as e:
        print("Caught exception:", e)

# 12. Generate NoSuchFieldException analog (AttributeError in Python)
def generate_nosuchfield_exception():
    print("\n12. Generating NoSuchFieldException analog (AttributeError):")
    class Test:
        pass
    try:
        t = Test()
        print(t.some_nonexistent_attribute)
    except AttributeError as e:
        print("Caught exception:", e)


# --- Calling all functions sequentially ---

if __name__ == "__main__":
    # 1. Arithmetic Exception without handling
    try:
        arithmetic_exception_no_handling()
    except ZeroDivisionError as e:
        print("Caught unhandled exception in main:", e)

    # 2. Handling Arithmetic Exception
    handle_arithmetic_exception()

    # 3. Call method that throws exception without try (wrap in try to prevent crash)
    try:
        call_method_without_handling()
    except ValueError as e:
        print("Caught exception from method:", e)

    # 4. Multiple except blocks
    multiple_catch_blocks()

    # 5. Throw exception with custom message
    throw_exception_with_message()

    # 6. Custom exception program
    custom_exception_program()

    # 7. Program with finally block
    program_with_finally()

    # 8. Generate Arithmetic Exception
    generate_arithmetic_exception()

    # 9. Generate FileNotFoundException
    generate_filenotfound_exception()

    # 10. Generate ClassNotFoundException analog
    generate_classnotfound_exception()

    # 11. Generate IOException analog
    generate_ioexception()

    # 12. Generate NoSuchFieldException analog
    generate_nosuchfield_exception()
