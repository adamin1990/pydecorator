__author__ = 'Administrator'
def deco(func):
    """
    对带参数的函数进行装饰
    :param func:
    :return:
    """
    def _deco(a,b):
        print("调用钱")
        ret =func(a,b)
        print("调用后")
        return ret
    return _deco
@deco
def myfun(a,b):
    print("myfun(%s,%s)中"%(a,b))
    return a+b
myfun(1,2)
myfun(3,4)
