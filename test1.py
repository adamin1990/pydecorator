__author__ = 'Administrator'
def deco(func):
    """
    使用装饰函数在函数执行前和执行后分别附加额外功能
    :param func:
    :return:
    """
    print("myfunc()调用之前")
    func()
    print("myfunc()调用之后")
    return  func
def myfunc():
    print("myfunc()调用了")

@deco   # 使用语法糖@ 装饰函数 实质语句 myfunc2=deco(myfunc2)
def myfunc2():
    print("python装饰器学习")
#myfunc =deco(myfunc)
#myfunc2()




