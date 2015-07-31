__author__ = 'Administrator'
def deco_funcNeedDoc(func):
    """
    检查myfun函数是否有doc
    :param func:
    :return:
    """
    def _deco():
        if func.__doc__==None:
            print("不写注释是个坏毛病!")
        else:
            print ("很好，写注释的习惯",func,':',func.__doc__,'.')
    return  _deco

@deco_funcNeedDoc #装饰器
def myfun():
    """
    这里是注释
    :return:

    """
    print('myfunc执行')
myfun()
