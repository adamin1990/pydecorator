__author__ = 'Administrator'
class locker:
    """
    装饰器带类参数
    """
    def __init__(self):
        print("locher init 不应该调用")

    @staticmethod
    def acquire():
        print("locker.acquire() called.（这是静态方法）")

    @staticmethod
    def release():
        print("realease 方法调用，不需要对象实例")
def deco(cls):
    '''
    cls 必须实现 acquire和release静态方法
    :param cls:
    :return:
    '''
    def _deco(func):
        def __deco():
            print("%s 调用 %s 之前"%(func.__name__,cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()
        return __deco
    return _deco
@deco(locker)
def myfunc():
    print("myfunc()调用")
myfunc()
myfunc()
