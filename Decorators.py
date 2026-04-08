# from functools import wraps
# def Decorator_fun(original_fun):
#     @wraps(original_fun)
#     def wrapper_fun(*args,**kwargs):
#         print("Wrapper excuted this before {}".format(original_fun.__name__))
#         return original_fun(*args,**kwargs)
#     return wrapper_fun

# @Decorator_fun
# def Display(name,age):
#     print(f"Display excuted with {name} and {age}")
# Display("Viveksingh",25)


# with class 
# class Decorator_class(object):
#     def __init__(self,original):
#         self.original=original
#     def __call__(self,*args,**kwargs):
#         print("Wrapper excuted this before {}".format(self.original.__name__))
#         return self.original(*args,**kwargs)
# @Decorator_class
# def Display(name,age):
#     print(f"Display excuted with {name} and {age}")
# Display("Viveksingh",25)

# Duct typing
# class Animal:
#     def __init__(self,name,type):
#         self.name=name
#         self.type=type
#         print(f"__init__ call name: {self.name} and type: {self.type}")
#     def call_fun(self):
#         print(f"animal_class")
# class cat(Animal):
#     def __init__(self):
#         super().__init__(cat.__name__,"four leged")
#     def call_fun(self):
#         print("cat_class")
# class Dog(Animal):
#     def __init__(self):
#         super().__init__(Dog.__name__,"four leged")
#     def call_fun(self):
#         print("Dog_class")
# def Display(obj):
#     obj.call_fun()

# cat=cat()
# Dog=Dog()
# Animal=Animal("Animal","Any")
# Display(cat)
# Display(Dog)
# Display(Animal)

def calculate_area(radius):
    """Calculates the area of a circle given its radius."""
    return 3.14159 * (radius ** 2)

# Accessing the docstring via the __doc__ attribute
help(calculate_area)



