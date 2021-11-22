# example setattr

# https://block.arch.ethz.ch/blog/2016/07/adding-methods-to-python-classes/


def print_classname_ex(x):
    print(x.__class__.__name__)


class B(object):
    def print_classname_1(self):
        print(self.__class__.__name__)


class A:
    def print_name_2(self,):
        print(self.__class__.__name__)

    print_fromB = B.print_classname_1



setattr(A, "print_classname_ex", print_classname_ex)


a = A()

a.print_name_2()
a.print_fromB()
a.print_classname_ex()


# ------------------------------------------------------------
# https://block.arch.ethz.ch/blog/2016/11/creating-functions-dynamically/

funcs = {}
 
for i in range(10):
   code = """def constraint_{0}(x): return x[{0:d}] > 1e-12""".format(i)
   exec(code, {}, funcs)



import random
 
r = [random.random() for _ in range(10)]
 
for name in funcs:
   print ( funcs[name].__name__ )
   print ( type(funcs[name]) )
   print ( funcs[name](r) )
   print ()

# ------------------------------------------------------------
# http://www.odosmatthewscoding.com/2018/10/how-to-inject-methods-into-python.html


# 1 step

def injector_model(function, mod=None):
    name = function.__name__
    def wrapper(k):
        if mod == None:
            setattr(k, name, eval(name))
        else:
            setattr(k, name, mod(eval(name)))
        return k
    return wrapper

# 2 step

def inject_static_method(function):
    return injector_model(function, staticmethod)

def inject_class_method(function):
    return injector_model(function, classmethod)

def inject_instance_method(function):
    return injector_model(function)


def static_test():
    print("I'm static")

def class_test(cls):
    print(cls)

def instance_test(self):
    print(self)

@inject_static_method(static_test)
@inject_class_method(class_test)
@inject_instance_method(instance_test)
class TestClass:
    pass



TestClass.static_test() 
#prints -> I'm static
TestClass.class_test()
#prints -> <class '__main__.TestClass'>
tc = TestClass()
tc.instance_test()
#prints -> <__main__.TestClass object at 0x00000051B>



# https://eli.thegreenplace.net/2009/11/28/python-internals-working-with-python-asts
# https://block.arch.ethz.ch/blog/2016/11/creating-functions-dynamically/


# subsitute init


def addId(cls):

    class AddId(cls):

        def __init__(self, id, *args, **kargs):
            super(AddId, self).__init__(*args, **kargs)
            self.__id = id

        def getId(self):
            return self.__id

    return AddId


class Foo:
    pass

FooId = addId(Foo)

foo=FooId( 10  )

print (foo.__dict__)

# --------------------------------------------------------------------

