from functools import reduce
import time

__author__ = 'Administrator'
def performance(unit):
    def perf_decorator(f):
        def wrapper(*args,**kwargs):
            t1=time.time();
            r=f(*args,**kwargs)
            t2=time.time()
            t=(t2-t1)*1000 if unit=="ms" else (t2-t1)
            print("call %s() in %f %s"%(f.__name__ ,t,unit))
            return r
        return wrapper
    return perf_decorator
@performance('ms')
def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
print(factorial(10))