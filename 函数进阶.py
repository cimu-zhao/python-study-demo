"""
#演示函数的多返回值类型
def test_return():
    return 1,"hello",True
x,y,z=test_return()
print(x)
print(y)
print(z)
//
def user_info(name,age,gender):
    print(f"您的名字是:{name},年龄是:{age},性别是:{gender}")
#位置参数
user_info("Tom",28,"男")
#关键字参数
user_info(name='小王',age=20,gender='女')
user_info(age=10,gender='女',name='笑笑')
user_info('小欣',gender='女',age='19')
#缺省参数
def use_info(name,age,gender='男'):
    print(f"您的名字是:{name},年龄是:{age},性别是:{gender}")
use_info(name='小王', age=20)
use_info(name='小王',age=20,gender='女')
#位置不定长 元组
def user_info(*args):
    print(f"args参数的类型是：{type(args)},内容是:{args}")
user_info(1,2,3,'小明','男孩')
#关键字不定长 字典
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)},内容是:{kwargs}")
user_info(name='小王',age=20,gender='女')
#函数作为数据传入
def test_fund(compute):
    result=compute(1,2)
    print(type(compute))
    print(result)
def compute(x,y):
    return x+y
test_fund(compute)
#匿名函数
def test_func(comnpute):
    result=comnpute(1,2)
    print(result)
test_func(lambda x,y:x+y)

"""




