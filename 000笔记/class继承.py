
class Person:
    x = 5
    y = 1
    def __init__(self, fname, lname):
        # 这里的self.firstname=xx相当于在上面
        # (xy的地方)定义一个变量firstname=xx
        self.firstname = fname
        self.lastname = lname
    # 类的函数第一个变量代表类自己，可以不叫self
    def printname(不是self也可以):
        print(不是self也可以.firstname, 不是self也可以.lastname)

class Student(Person):
    # 重新定义变量，将不继承父类
    y = 7
    def __init__(self, fname, lname, grade):
        # super().相当于Person.
        # 这句代码可以替换为Person.__init__(f,l)
        super().__init__(fname, lname)
        # 继承后添加新的内容
        self.grade = grade
    
    def printname(self):
        # return super().printname()
        # 这里重新定义一个函数，不继承父类
        print(self.firstname, self.lastname, self.grade)
    
    # 添加新的方法
    def newf(self):
        pass

stu = Student('mick','muck','7')
print(stu.x,stu.y)
stu.printname()


# 类可以使用定义在类外的函数，但是定义在外的函数第一个变量必须是self
def f1(self,x,y):
    return min(x,y)
class C:
    f = f1
    def g(self):
        return 'hello'
    h=g

c = C()
print(c.f(1,2))