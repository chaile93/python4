#!/usr/bin/env python
# coding: utf-8

# # Object-Oriented-Programming (OOP)

# ## Tasks Today:
# 
#    
# 
# 1) <b>Creating a Class (Initializing/Declaring)</b> <br>
# 2) <b>Using a Class (Instantiating)</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Creating One Instance <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Creating Multiple Instances <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #1 - Create a Class 'Car' and instantiate three different makes of cars <br>
# 3) <b>The \__init\__() Method</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) The 'self' Attribute <br>
# 4) <b>Class Attributes</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Initializing Attributes <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Setting an Attribute Outside of the \__init\__() Method <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Setting Defaults for Attributes <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Accessing Class Attributes <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Changing Class Attributes <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) In-Class Exercise #2 - Add a color and wheels attribute to your 'Car' class <br>
# 5) <b>Class Methods</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Creating <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Calling <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Modifying an Attribute's Value Through a Method <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Incrementing an Attribute's Value Through a Method <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) In-Class Exercise #3 - Add a method that prints the cars color and wheel number, then call them <br>
# 6) <b>Inheritance</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax for Inheriting from a Parent Class <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) The \__init\__() Method for a Child Class (super()) <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Defining Attributes and Methods for the Child Class <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Method Overriding <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) In-Class Exercise #4 - Create a class 'Ford' that inherits from 'Car' class and initialize it as a Blue Ford Explorer with 4 wheels using the super() method <br>
# 7) <b>Classes as Attributes</b> <br>
# 8) <b>Exercises</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Exercise #1 - Turn the shopping cart program from yesterday into an object-oriented program <br>

# ## Creating a Class (Initializing/Declaring)
# <p>When creating a class, function, or even a variable you are initializing that object. Initializing and Declaring occur at the same time in Python, whereas in lower level languages you have to declare an object before initializing it. This is the first step in the process of using a class.</p>

# In[23]:


class Car():
    wheels = 4
    color = 'blue'
    windsheild_wipers = 'wee woo wee woo'
    
    def highlights():
        print('turn them on for safety, do not crash into a moose.')
        
volkswagen = Car()

print(volkswagen.headlights())


# ## Using a Class (Instantiating)
# <p>The process of creating a class is called <i>Instantiating</i>. Each time you create a variable of that type of class, it is referred to as an <i>Instance</i> of that class. This is the second step in the process of using a class.</p>

# ##### Creating One Instance

# In[10]:


ford = Car()

print(ford.windsheild_wipers)


# ##### Creating Multiple Instances

# In[6]:


chevrolet = Car()
Honda = Car()
porche = Car()
print(type(porche.color))


# ##### In-Class Exercise #1 - Create a Class 'Car' and Instantiate three different makes of cars

# In[ ]:





# ## The \__init\__() Method <br>
# <p>This method is used in almost every created class, and called only once upon the creation of the class instance. This method will initialize all variables needed for the object.</p>

# In[27]:


class Car():
    engine = '4.7L'
    
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels
        
mazda = Car('black', 4)

subaru = Car('blue', 6)

print(mazda.color)
print(subaru.color)
print(subaru.wheels)
print(mazda.wheels)


# ##### The 'self' Attribute <br>
# <p>This attribute is required to keep track of specific instance's attributes. Without the self attribute, the program would not know how to reference or keep track of an instance's attributes.</p>

# In[ ]:


# see above


# ## Class Attributes <br>
# <p>While variables are inside of a class, they are referred to as attributes and not variables. When someone says 'attribute' you know they're speaking about a class. Attributes can be initialized through the init method, or outside of it.</p>

# ##### Initializing Attributes

# In[34]:


# see above

class Toy():
    kind = 'car'
    
    def __init__(self, rooftop, horn, wheels):
        self.rooftop = rooftop
        self.horn = horn
        self.wheels = wheels
    
tonka_truck = Toy(1,1,4)
hotwheels_car = Toy(2,3,8)


# ##### Accessing Class Attributes

# In[37]:


# See Above

tonka_truck.rooftop
hotwheels_car.wheels


# ##### Setting Defaults for Attributes

# In[44]:


class = Car()
    engine = '4.7L'
    def __init__(self, wheels):
        self.wheels = wheels
        self.color = 'Blue'
        
honda = Car(4)
honda.color


# ##### Changing Class Attributes <br>
# <p>Keep in mind there are global class attributes and then there are attributes only available to each class instance which won't effect other classes.</p>

# In[41]:


jeep = Car(8)

print(f'Before change: (jeep.color)')

jeep.color = 'White'

print(f'\nAfter change: (jeep.color)')
print(honda.color)


# In[ ]:





# ##### In-Class Exercise #2 - Add a doors and seats attribute to your 'Car' class then print out two different instances with different doors and seats

# In[ ]:





# ## Class Methods <br>
# <p>While inside of a class, functions are referred to as 'methods'. If you hear someone mention methods, they're speaking about classes. Methods are essentially functions, but only callable on the instances of a class.</p>

# ##### Creating

# In[ ]:





# ##### Calling

# In[ ]:


# See Above


# ##### Modifying an Attribute's Value Through a Method

# In[ ]:





# ##### Incrementing an Attribute's Value Through a Method

# In[ ]:





# ##### In-Class Exercise #3 - Add a method that takes in three parameters of year, doors and seats and prints out a formatted print statement with make, model, year, seats, and doors

# In[ ]:


# Create class with 2 paramters inside of the __init__ which are make and model

# Inside of the Car class create a method that has 4 parameter in total (self,year,door,seats)

# Output: This car is from 2019 and is a Ford Expolorer and has 4 doors and 5 seats



# ## Inheritance <br>
# <p>You can create a child-parent relationship between two classes by using inheritance. What this allows you to do is have overriding methods, but also inherit traits from the parent class. Think of it as an actual parent and child, the child will inherit the parent's genes, as will the classes in OOP</p>

# ##### Syntax for Inheriting from a Parent Class

# In[ ]:





# ##### The \__init\__() Method for a Child Class - super()

# In[ ]:





# ##### Defining Attributes and Methods for the Child Class

# In[ ]:


# See Above


# ##### Method Overriding

# In[ ]:


# See Above


# ## Classes as Attributes <br>
# <p>Classes can also be used as attributes within another class. This is useful in situations where you need to keep variables locally stored, instead of globally stored.</p>

# In[ ]:





# # Exercises

# ### Exercise 1 - Turn the shopping cart program from yesterday into an object-oriented program
# 
# The comments in the cell below are there as a guide for thinking about the problem. However, if you feel a different way is best for you and your own thought process, please do what feels best for you by all means.

# In[ ]:


# Create a class called cart that retains items and has methods to add, remove, and show

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def display_options(self):
        print("\nOptions:")
        print("1. Add item")
        print("2. Delete item")
        print("3. View shopping list")
        print("4. Quit")

    def add_item(self, item):
        self.cart.append(item)
        print(f"Added '{item}' to your shopping list.")

    def delete_item(self, item_index):
        if 1 <= item_index <= len(self.cart):
            deleted_item = self.cart.pop(item_index - 1)
            print(f"Deleted '{deleted_item}' from your shopping list.")
        else:
            print("Invalid item number.")

    def view_shopping_list(self):
        if not self.cart:
            print("Your shopping cart is empty.")
        else:
            print("Your current shopping list:")
            for index, item in enumerate(self.cart, start=1):
                print(f"{index}. {item}")

    def run_shopping_cart(self):
        while True:
            self.display_options()
            choice = input("Enter your choice (1/2/3/4): ").strip()

            if choice == '1':
                item = input("Enter item to add: ").strip()
                self.add_item(item)

            elif choice == '2':
                if not self.cart:
                    print("Your shopping cart is empty.")
                else:
                    self.view_shopping_list()
                    item_to_delete = int(input("Enter the number of item to delete: ").strip())
                    self.delete_item(item_to_delete)

            elif choice == '3':
                self.view_shopping_list()

            elif choice == '4':
                print("Thank you for shopping with us! Here is your final shopping list:")
                self.view_shopping_list()
                break

            else:
                print("Invalid choice. Please enter a valid option (1/2/3/4).")

    


# ### Exercise 2 - Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case

# In[ ]:


class Strings:
    def __init__(self):
        self.input_string = ""

    def string_one(self):
        self.input_string = input("Enter a string: ")

    def string_two(self):
        print("String in upper case:", self.input_string.upper())

