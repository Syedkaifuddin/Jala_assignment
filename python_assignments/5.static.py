# 1. Define a static variable and access that through a class
class A1:
    x = 100

print("\n1. Access through class:", A1.x)

# 2. Define a static variable and access that through an instance
class A2:
    x = 200

obj2 = A2()
print("\n2. Access through instance:", obj2.x)

# 3. Define a static variable and change within the instance
class A3:
    x = 300

obj3 = A3()
obj3.x = 999  
print("\n3. After instance change - obj.x:", obj3.x)
print("   Original static value remains:", A3.x)

# 4. Define a static variable and change within the class
class A4:
    x = 400

A4.x = 888
print("\n4. After class-level change:", A4.x)
