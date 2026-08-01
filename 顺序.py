"""
bool_1=True
bool_2=False
print(f"bool_1变量的内容是：{bool_1},类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2},类型是：{type(bool_2)}")
# 比较运算符
num1=10
num2=20
print(f"10==10的结果是：{num1==num2}")
num1=10
num2=15
print(f"10!=15的结果是：{num1!=num2}")
name1="itcast"
name2="itheima"
print(f"itcast==itheima 结果是：{name1==name2}")
# > < >= <=
num1=10
num2=5
print(f"10>5的结果是：{num1>num2}")
print(f"10<5的结果是：{num1<num2}")
num1=10
num2=10
print(f"10>=10的结果是：{num1>=num2}")
print(f"10<=10的结果是：{num1<=num2}")

age=30
if age>=18:
    print("我已经成年了")
    print("即将步入大学生活")

print("时间过得真快啊")

if int(input("你的身高是多少"))>120:
    print("身高超出限制，不可以免费")
    print("但是vip等级大于3，可以免费")
    if int(input("你的vip等级是多少"))>3:
        print("恭喜你，vip等级达标，可以免费")
    else:
        print("Sorry,你应该买票10元。")
else:
    print("欢迎，你可以免费游玩了")

"""
import random
num=random.randint(1,100)
guess_num=int(input("请输入你猜的数字"))
if guess_num==num:
    print("恭喜你第一次就猜中了")
else:
    if guess_num>num:
        print("你猜的数字太大了，往小猜")
    else:
        print("你猜的数字太小了，往大猜")
    guess_num=int(input("再次输入你要猜测的数字："))
    if guess_num==num:
        print("恭喜第二次猜中了")
    else:
        if guess_num > num:
            print("你猜的数字太大了，往小猜")
        else:
            print("你猜的数字太小了，往大猜")
        guess_num = int(input("最后一次输入你要猜测的数字："))
        if guess_num == num:
            print("恭喜第三次猜中了")
        else:
            print("三次机会用完了，你没有猜中。")