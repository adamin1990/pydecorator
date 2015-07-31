__author__ = 'Administrator'
def deco(func):
    """
    对参数不确定的函数进行装饰
    :param func:
    :return:
    """
    def _deco(*args,**kwargs):
        print("%s 调用之间" % func.__name__)
        ret =func(*args,**kwargs)
        print("%s 调用之后 结果%s" % (func.__name__,ret))
        return ret
    return _deco
@deco
def myfunc(a,b):
    print("myfunc(%s ,%s)调用中"%(a,b))
    return a+b
@deco
def myfunc2(a,b,c):
    print("myfunc2(%s,%s,%s)"%(a,b,c))
    return a+b+c
myfunc(1,2)
myfunc(3,4)
myfunc2(1,2,3)
myfunc2(2,3,4)
