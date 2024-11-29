class MyClass:
    pass


obj = MyClass()
class_name = obj.__class__.__name__
print(f"The class name of the instance is: {class_name}")
