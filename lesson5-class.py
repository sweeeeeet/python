class Test():
    '''
    这是一个用来测试类创建语法的类
    '''
    # pass

    #类属性（静态变量）
    val=88

    #静态方法，并不是Java中的静态成员函数，不能调用类属性
    @staticmethod#装饰器
    def Func():
        print("in fun")
    #Func=staticmethod(Func)#或是用装饰器代替

    #类方法
    def Func2(cls):
        """
        类方法可以调用类属性
        """
        print(cls.val)


    def __init__(self,a=10):
        #构造函数，在类创建时会进行初始化
        #若是出现在成员函数中的变量需要调用了函数后对成员变量进行初始化了才能进行调用
        #因此一个类的实例属性最好都放在__init__中
        self.x=10
        self.y=a

    def Print(self):
        """
        实例方法：成员函数/普通方法

        """
        #成员变量不需要提前声明，在成员方法中声明
        self.num=19
        print("hello")
        print(self.y)


    #python中的多态
    """
    从函数的角度看，并不知道xy的具体类型
    但是知道xy支持相加操作，不管啥类型，都往一起相加，这就是python中的多态
    """
    def add(x,y):
        return x+y
    print(add(10,20))
    print(add("hello","world"))
    print(add([1,2,3],[4,5,6]))

#创建对象
test=Test(12)
#调用成员函数
test.Print()
