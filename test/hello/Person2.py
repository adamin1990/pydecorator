from filecmp import cmp

__author__ = 'Administrator'
class Person(object):
    pass
p1=Person()
p1.name="lixiaopeng"

p2=Person()
p2.name="wangwang"

p3=Person()
p3.name="ADAM"

L1=[p1,p2,p3]
# L2=sorted(L1,lambda p1,p2:cmp(p1.name,p2.name))
L2=sorted(L1,key=lambda p:p.name.upper(),reverse=True)


print(L2[0].name)
print(L2[1].name)

