__author__ = 'Administrator'
def deco(func):
    """
    使用内嵌包装函数来确保每次新函数都被调用
    :param func:
    :return:
    """
    print("hhhhhhh")
    def _deco():
        print("调用前")
        func()
        print("调用后")
    return  _deco
@deco   # myfunc=deco(myfunc)
def myfunc():
    print("调用中")
    return 'ok'
myfunc()
myfunc()

