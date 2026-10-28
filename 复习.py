"""price=float(input("请输入产品单价："))
weight=float(input("请输入产品重量："))
money=price*weight
print(f"您需要支付{money}元")
a,b,c=1,2,"hello"
print(f"变量a的值是{a},类型是{type(a)}")
print(f"变量b的值是{b},类型是{type(b)}")
print(f"变量c的值是{c},类型是{type(c)}")
#逻辑运算符
print(3-3 and 3<6)
print(3<6 and 3+5)
print(1+2 or 3<6)
print(3<6 or 3+5)
print(not 3>6)
age=int(input("请输入年龄："))
height=int(input("请输入身高："))
if age>=18 and age<=30 and height>=170 and height<=185:
    print("恭喜，符合飞行员报考条件")
else:
    print("抱歉，你不符合飞行员的报考条件")
list=[1,2,3,4,5]
a=5
if a in list:
    print(a)
for b in list:#遍历
    print(b)
a=10
b=20
print(a is b)
print(a is not b)
b=10
print(a is b)
x=int(input("请输入一个三位数："))
a=x//100
b=x//10%10
c=x%10
print(f"{x}的百位是{a},十位是{b},个位是{c}")
import random
sc=random.randint(1,100)
count=0
while True:
    Guess_num=int(input("请输入你猜的数字："))
    count+=1
    if Guess_num>sc:
        print("猜大了，往小猜")
    elif Guess_num<sc:
        print("猜小了，往大猜")
    else:
        print(f"恭喜你，答对了，你一共猜了{count}次")
        break
i=1
while i<10:
    j=1
    while j<=i:
        print(f"{i}*{j}={i*j}\t",end='')
        j+=1
    i+=1
    print()
    x,y=[1,2,3],[1,2,3]
print(x is y)
print(x is [1,2,3])
print(x is not [1,2,3])
x=20
y=(20,"Python")
print(x in y)
x,y='Py','Python'
print(x in y)
year=int(input("请输入查询年份："))
if year%4==0:
    if year%100!=0:
        print(f"{year}年是闰年")
    elif year%100==0:
        if year%400==0:
            print(f"{year}年是闰年")
        else :
            print(f"{year}年不是闰年")
else:
    print(f"{year}年不是闰年")
    year=int(input("请输入查询年份："))
if(year%4==0 and year%100!=0)or(year%400==0):
    print(f"{year}年是闰年")
else:
    print(f"{year}年不是闰年")
score=int(input("请输入你的成绩："))
if score<0 or score>100:
    print("成绩不合规")
elif score>=90 and score<=100:
    grade="A（优秀）"
elif score>=80 and score<90:
    grade= "B（良好）"
elif score>=70 and score<80:
    grade="C（中等）"
elif score>=60 and score<70:
    grade="D（及格）"
else:
    grade="E（不及格）"
print(f"你的成绩等级是{grade}")
a=float(input("第一个："))
b=float(input("第二个："))
c=float(input("第三个："))
list=[a,b,c]
list.sort() #从小到大
print(f"排序后为{list}")
list.sort(reverse=True) #从大到小
print(f"排序后为{list}")
a=float(input("第一个："))
b=float(input("第二个："))
c=float(input("第三个："))
t=0
if a>b:
    t=a
    a=b
    b=t
if a>c:
    t=a
    a=c
    c=t
if b>c:
    t=b
    b=c
    c=t
print(f"{a},{b},{c}")

nums=[3,1,4,1,5,9,2]
new_nums=sorted(nums)
print(new_nums)
print(nums)

nums.sort()
print(nums)

print(sorted(nums,reverse=True))
nums=[]
for i in range(1,5):
    s=int(input(f"第{i}个数"))
    nums.append(s)
new_nums=sorted(nums)
print(new_nums)
print(nums)

nums.sort()
print(nums)

print(sorted(nums,reverse=True))
import re
text = "Hello world! Hello Python. Python is great, and hello world is fun."
def f(s):
    words=re.split(r'\W+',s)
    word=[]
    for w in words:
        if w !="":
          word.append(w)
    result=list(filter(lambda w:len(w)>2,words))
    return result
print(f(text))
data = ["apple", "123", "python", "45.6", "hello", "789"]
def custom_sort(item):
    if item.isalpha():
        return (0,item)
    elif item.isdigit():
        return (1,int(item))
    else:
        return (2,float(item))
result=sorted(data,key=custom_sort)
print(f"排序后的结果：{result}")
s=input("请输入一个字符串:")
for i in range(len(s)-1,-1,-1):
    print(s[i],end='')

import re
def f(username, password):
    if not username.startswith('_'):
        return "用户名必须以下划线'_'开头"
    if not (3 <= len(username) <= 30):
        return "用户名长度必须在3～30个字符之间"
    if not (8 <= len(password) <= 16):
        return "密码长度必须在8～16个字符之间"
    if not re.match(r'^[A-Za-z0-9_]+$', password):
        return "密码必须由下划线、数字和字母组成，不允许有其他符号"
    if not (re.search(r'[A-Za-z]', password) and re.search(r'\d', password) and re.search(r'_', password)):
        return "密码必须由下划线、数字和字母共同组成"
    return "用户名正确，密码正确，注册成功！"
if __name__ == "__main__":
    user_name = input("请输入用户名：")
    pass_word = input("请输入密码：")
    print(f(user_name, pass_word))

    class Student:<br/>
        pass
        if __name__=='__main__':
            stu=Student()
                print(stu)
        class Person:<br/>
            def greet(self):
            print("Hello")
        personl=Person()
        personl.greet()

        class Book:
        number=0
        def __init__(self,name):
            self.name=name
    print(Book.number)
    Book.number+=1
    print(Book.number)
    b=Book("Python程序设计")
    print(b.number)

    class Book:
        number=0
        def __init__(self,name):
            self.name=name
            Book.number+=1
            self.id=Book.number
    b1=Book("《红楼梦》")
    b2=Book("《水浒传》")
    b3=Book("《西游记》")
    print(f"书籍的总数是：{Book.number}")
    print(f"{b1.name}的数量是{b1.name}")
    print(f"{b2.name}的数量是{b2.name}")
    print(f"{b3.name}的数量是{b3.name}")

    class Person:
        career="student" #类属性
        def __init__(self,name,age):
            self.name=name
            self.age=age
    person1=Person("Miya",30)
    person2=Person("Dave",28)
    print(person1.career)
    print(person2.career)
    person1.career="teacher"
    print(person1.career)
    print(person2.career)

    class Student:
        name='Unknown'
    if __name__=='__main__':
        Student.count=0
        stu1=Student()
        Student.count+=1
        stu2=Student()
        Student.count+=1
        stu1.age=19
        stu2.age=20
        print(f"stu1姓名：{stu1.name}s,年龄：{stu1.age}")

    class Student:
        school = "河南能源化工学院"

        def __init__(self, name, age):
            self.name = name
            self.age = age


    stu1 = Student("豆包", 3)
    stu2 = Student("workbich", 19)
    print(f"{stu1.name}是{stu1.school}的学生，我今年{stu1.age}岁了·")
    print(f"{stu2.name}是{stu2.school}的学生，我今年{stu2.age}岁了·")

class Room:
    def __init__(self,name):
        self.__name=name
r1=Room("房间1")
name=r1._Room__name
print(name)

 class Student:
    def SetName(self,newname):
        self.name=newname
    def PrintName(self):
        print(f"姓名：{self.name}")
if __name__=='__main__':
    stu1=Student()
    stu2=Student()
    stu1.SetName('李晓明')
    stu2.SetName('马红')
    stu1.PrintName()
    stu2.PrintName()
   # Student.SetName('未知')
    #Student.PrintName()

    class Student:
    def __init__(self):
        print('调用构造方法')
        self.school='河南能源化工学院'
    def say(self):
        print('学校：',self.school)
s=Student()
s.say()

class Dog:
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age
    def eat(self):
        print(f"{self.name}正在吃狗粮")
    def run(self):
        print(f"{self.name}在奔跑玩耍")
dog1=Dog("KK","金毛",2)
dog1.eat()
dog1.run()

class Student:
    def __init__(self,name):
        self.name=name
        print(f"姓名为{self.name}的对象被创建")
    def __del__(self):
        print(f"姓名为{self.name}的对象被销毁")
def func(name):
    stu=Student(name)
def main():
    stu1=Student('李晓明')
    stu2=Student('马红')
    stu3=stu2
    del stu2
    func('张刚')
    del stu3
    stu4=Student('刘建')
if __name__=='__main__':
    main()

    class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self, other):
        return self.age>other.age
    def __ne__(self, other):
        return self.age!=other.age
    def __le__(self, other):
        return self.age<=other.age
if __name__=='__main__':
    stu1=Student('李晓明',19)
    stu2=Student('马红',20)
    stu3=Student('张刚',19)
    print("马红的年龄小于等于李晓明的年龄：",stu2<=stu1)
    print("张刚的年龄小于等于李晓明的年龄：",stu3<=stu1)
    print("马红的年龄大于等于李晓明的年龄：",stu2>stu1)
    print("张刚的年龄小于等于李晓明的年龄：",stu3>stu1)
    print("张刚的年龄小于等于李晓明的年龄：",stu3!=stu1)
    print("马红的年龄不等于马红的年龄：",stu3!=stu2)

class Book:
    kind="书籍"
    def __init__(self,name,author,price):
        self.name=name
        self.author=author
        self.price=price
    def show_info(self):
        print(f"类别：{Book.kind},书名：{self.name},作者：{self.author},价格：{self.price}")
b1=Book("西游记","吴承恩",39.8)
b2=Book("朝花夕拾","鲁迅",25.0)
b1.show_info()
b2.show_info()
print(f"类属性：  {Book.kind}")
print(“四大名著”)
"""