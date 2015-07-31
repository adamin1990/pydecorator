__author__ = 'Administrator'
def deco(arg):
    def _deco(func):
        def __deco():
            print("%s 调用 [%s]之前" % (func.__name__,arg))
            func();
            print("%s 调用 [%s]之后" %( func.__name__,arg))
        return __deco
    return _deco
@deco("mymodule")
def myfunc():
    print("myfunc调用")
@deco("module2")
def myfunc2():
    print("module2调用")
myfunc()
myfunc2()
