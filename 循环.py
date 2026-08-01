"""
//1 while循环基础语法
i=1
while i<=100:
    print("芷兮我喜欢你")
    i=i+1

//2 while循环猜数字游戏
    import random
num=random.randint(1,100)
flag=True
count=0
while flag:
    guess_num=int(input("请输入你猜的数字："))
    count+=1
    if guess_num==num:
        print("恭喜你猜对了")
        flag=False
    else:
        if guess_num>num:
            print("你猜大了，往小猜")
        else:
            print("你猜小了，往大猜")
print(f"你一共猜了{count}次")

//3 while嵌套循环
i=1
while i<=100:
    print(f"今天是第{i}天，准备表白")

    j=1
    while j<=10:
        print(f"送给芷兮第{j}朵玫瑰花")
        j+=1
    print("芷兮我喜欢你")
    i+=1
print(f"坚持到第{i-1}天，表白成功")

//4 九九乘法表
i=1
while i<10:
    j=1
    while j<=i:
        print(f"{j}*{i}={j*i}\t",end='')
        j+=1
    i=i+1
    print()

// for循环 无法定义循环条件 被动取出数据处理
name="itheima"
for x in name:
    print(x)

//for循环结合range语法
for x in range(0,10,2):
    print(x)
for i in range(0,10):
    print("送玫瑰花")

//for循环嵌套
#for循环嵌套
i=1
for i in range(1,101):
    print(f"今天是向小美表白的第{i}天")
    for j in range(1,1000):
        print(f"给小美送的第{j}朵花")
    print("小美我喜欢你")
print(f"第{i}天表白成功")
// for循环while循环相互嵌套
i=1
for i in range(1,101):
    print(f"今天是向小美表白的第{i}天")
    j=1
    while j<=10:
        print(f"给小美送的第{j}朵花")
        j+=1
    print("小美我喜欢你")
print(f"第{i}天表白成功")
i=1
while i<=100:
    print(f"今天是向小美表白的第{i}天")
    for j in range(1,11):
        print(f"给小美送的第{j}朵花")
    print("小美我喜欢你")
    i+=1
print(f"第{i-1}天表白成功")

//continue语法
for i in range(1,6):
    print("语句一")
    for j in range(1,6):
        print("语句二")
        continue
        print("语句三")

//break语句（只对所在循环生效）
for i in range(1,6):
    print("语句一")
    break
    print("语句二")
print("语句三")
//continue break混合练习
money=10000
for i in range(1,21):
    import random
    num=random.randint(1,10)
    if num<5:
        print(f"员工{i}绩效分{num},不满足，不发工资，下一位")
        continue
    if money>=1000:
        money-=1000
        print(f"员工{i}，满足条件发放工资1000元，公司账户余额{money}元")
    else:
        print("余额不足，不发了")
        break
print("工资发完了，下个月再发吧")

//自己做的改良版
mport random

money = 10000
for i in range(1, 21):
    num = random.randint(1, 10)
    price = random.randint(1000, 2001)
    if num < 5:
        print(f"员工{i}绩效不满足，不发工资，下一位\n")
        continue
    if money > 0:
        if money >= price:
            money -= price
            print(f"员工{i}满足条件，发放工资{price}元，公司账户余额{money}元\n")
        else:
            # 余额不够标准薪资，全部发掉
            pay = money
            money = 0
            print(f"员工{i}满足条件，发放工资{pay}元，公司账户余额{money}元\n")
    else:
        print("公司余额不足，停止发放工资")
        break

print("工资发放流程结束，下个月再发")
"""
