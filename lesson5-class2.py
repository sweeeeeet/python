class Parent():
    def __init__(self):
        self.msg='hehe'

    def PrintMessage(self):
        print(self.msg)


class Child(Parent):
    def PrintMessage(self):
        print("child")

#继承了父类的子类即使什么也不干，也可以创建子类对象，调用父类的方法
c=Child()
c.PrintMessage()