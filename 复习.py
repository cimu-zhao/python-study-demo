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
"""
x=int(input("请输入一个三位数："))
a=x//100
b=x//10%10
c=x%10
print(f"{x}的百位是{a},十位是{b},个位是{c}")
