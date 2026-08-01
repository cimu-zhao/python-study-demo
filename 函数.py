"""
//1 lena()函数统计字符长度
name="itheima"
length=len(name)
print(length)
//2常规计数
str1="itheima"
str2="itcast"
str3="python"
count=0
for i in str1:
    count+=1
print(f"字符串{str1}的长度是：{count}")
count=0
for i in str2:
    count+=1
print(f"字符串{str2}的长度是：{count}")
count=0
for i in str3:
    count+=1
print(f"字符串{str3}的长度是：{count}")
//函数计数(避免重复写代码)
def my_len(date):
    count=0
    for i in date:
        count+=1
    print(f"字符串{date}的长度是：{count}")
my_len(str1)
my_len(str2)
my_len(str3)
//3函数定义
def say_hi():
    print("我是黑马程序员，来学python")
#调用函数
say_hi()
//5函数传参
def add(a,b,c):
    result=a+b+c
    print(f"{a}+{b}+{c}={result}")
add(1,4,7)
add(2,5,8)
add(3,6,9)
//6函数返回值
def add(a,b,c):
    result=a+b+c
    return result
r=add(1,4,7)
print(r)
//7None语法
def say_hi():
    print("你好啊")
result=say_hi()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")
//None用法
#None用于if判断
def check_age(age):
    if age>18:
        return "SUCCESS"
    else:
        return None
result=check_age(16)
if not result:
    #进入if表示result是None值 也就是False
    print("未成年，不可以进入")
name=None
// 8函数文档
def add(x,y):

    add函数可以接受两个参数，进行两数相加的结果
    :param x:x表示其中一个参数
    :param y:y表示另一个参数
    :return:返回值是两数相加的结果

    result=x+y
    print(f"2数相加的结果是：{result}")
    return result
add(1,2)
// 9函数嵌套调用
def f1():
    print("--2--")
def f2():
    print("--1--")
    f1()
    print("--3--")
f2()
//10全局变量局部变量global用法
num=200
def f():
    num=100
    print(num)
f()
print(num)
num=200
def f():
    global num
    num=100
    print(num)
f()
print(num)
"""
