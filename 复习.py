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
"""