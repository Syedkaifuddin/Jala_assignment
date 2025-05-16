# 1. PRIVATE Fields and Method
class PrivateClass:
    def __init__(self):
        self.__private_field = "Private Data"
    
    def __private_method(self):
        print("Private Method Called")

    def access_private(self):
        print("1. PRIVATE field:", self.__private_field)
        self.__private_method()

class SubPrivateClass(PrivateClass):
    def try_access_private(self):
        print("Sub class can't access __private_field or __private_method directly")

# 2. PROTECTED Fields and Methods
class ProtectedClass:
    def __init__(self):
        self._protected_field = "Protected Data"
    
    def _protected_method(self):
        print("Protected Method Called")

class SamePackageClass:
    def access_protected(self):
        obj = ProtectedClass()
        print("\n2. PROTECTED field (same package):", obj._protected_field)
        obj._protected_method()

# Simulating different package by different class
class ChildInDifferentPackage(ProtectedClass):
    def access_inherited_protected(self):
        print("Access from child (different package):", self._protected_field)
        self._protected_method()

class OtherClassDifferentPackage:
    def access_protected_direct(self):
        obj = ProtectedClass()
        print("Access from non-child (different package):", obj._protected_field)
        obj._protected_method()

# 3. PUBLIC Fields and Methods
class PublicClass:
    def __init__(self):
        self.public_field = "Public Data"

    def public_method(self):
        print("Public Method Called")

class PublicAccess:
    def access_public(self):
        obj = PublicClass()
        print("\n3. PUBLIC field:", obj.public_field)
        obj.public_method()


# Calling all as per the instructions
if __name__ == "__main__":
    # 1. PRIVATE
    p = PrivateClass()
    p.access_private()
    sp = SubPrivateClass()
    sp.try_access_private()

    # 2. PROTECTED
    same = SamePackageClass()
    same.access_protected()

    child = ChildInDifferentPackage()
    child.access_inherited_protected()

    other = OtherClassDifferentPackage()
    other.access_protected_direct()

    # 3. PUBLIC
    pub = PublicAccess()
    pub.access_public()
