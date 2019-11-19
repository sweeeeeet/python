#定义函数
def add(x,y):
    #函数体
    ret=x+y
    return ret

#函数调用
ret=add(2,4)
print(ret)

#在定义函数时赋值默认参数
def mius(x,y=0):
    return x-y
print(mius(4))

#一个函数可以返回多个值
def get_point():
    x=10
    y=20
    return x,y
#解包 unpack
x,y=get_point()
print(x,y)



#高阶函数:在参数中允许传入函数
def addPlus(x,y,f):
    return f(x)+f(y)

print(addPlus(2,3,abs))

#函数返回函数
def sum(x):
    m=0
    def f():
        for i in range(10):
            m=i+x
        return m
    return f
r=sum(3)
#对函数的调用结果是一个函数
print(r)
#对r调用才能得到结果
print(r())


print('=='*10)
#关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

#拼接两个列表
a=[1,2]
b=[3,4]
#将b拼接到a上，并不会创建新的对象
print(a.extend(b))

#字符串拼接
a=["sd","sd","ddd"]
#join前面的字符串对象代表拼接的分割符是什么
result="；".join(a)

print(a*3)