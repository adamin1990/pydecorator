__author__ = 'Administrator'
class Person(object):
    def __init__(self,name,gender,birth):
        self.name=name
        self.birth=birth
        self.gender=gender
xiaoming=Person("xiao ming","male","1990")
xiaohong=Person("Xiao Hong","female","1991")

print(xiaoming.name)
print(xiaohong.birth)

