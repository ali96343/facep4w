
# https://stackoverflow.com/questions/681953/how-to-decorate-a-class


from functools import wraps

def dec(msg='default'):
    def decorator(klass):
        old_foo = klass.foo
        @wraps(klass.foo)
        def decorated_foo(self, *args ,**kwargs):
            print('@decorator pre %s' % msg)
            old_foo(self, *args, **kwargs)
            print('@decorator post %s' % msg)
        klass.foo = decorated_foo
        return klass
    return decorator

@dec('foo decorator')  # You must add parentheses now, even if they're empty
class Foo(object):
    def foo(self, *args, **kwargs):
        print('foo.foo()')

@dec('subfoo decorator')
class SubFoo(Foo):
    def foo(self, *args, **kwargs):
        print('subfoo.foo() pre')
        super(SubFoo, self).foo(*args, **kwargs)
        print('subfoo.foo() post')

@dec('subsubfoo decorator')
class SubSubFoo(SubFoo):
    def foo(self, *args, **kwargs):
        print('subsubfoo.foo() pre')
        super(SubSubFoo, self).foo(*args, **kwargs)
        print('subsubfoo.foo() post')

SubSubFoo().foo()

