def mydecorator(student):
    #define a new display method
    def newdisplay(self):
        print('Name: ', self.name)
        print('Subject: Programming')
    
    #replace the display with newdisplay
    student.display = newdisplay
    
    #return the modified student 
    return student

@mydecorator
class Student:
    def __init__(self, name):
        self.name = name
        
    def display(self):
        print('Name:', self.name)
        

obj = Student('Pencil Programmer')
obj.display()
'''
Name:  Pencil Programmer
Subject: Programming
'''

# ------------------------------------------------------

class Mydecorator:
    #accept the class as argument
    def __init__(self, student):
        self.student = student
    
    #accept the class's __init__ method arguments
    def __call__(self, name):
        #define a new display method
        def newdisplay(self):
            print('Name: ', self.name)
            print('Subject: Python')
            
        #replace display with newdisplay
        self.student.display = newdisplay
        
        #return the instance of the class
        obj = self.student(name)
        return obj

@Mydecorator
class Student:
    def __init__(self, name):
        self.name = name
        
    def display(self):
        print('Name: ', self.name)

obj = Student('Pencil Programmer')
obj.display()
'''
Name:  Pencil Programmer
Subject: Python
'''

# The only difference here is that instead of class reference 
# we are returning the reference of the object.
# https://pencilprogrammer.com/decorate-python-class/

