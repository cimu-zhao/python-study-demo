"""
666
13.14
"黑马程序员"

print("666")
print("13.14")
print("黑马程序员")

money=50
print("钱包余额:",money)
money=money-10
print("买了冰激凌花费10元，还剩余：",money,"元")
# 每隔一小时，输出钱包余额
print("现在是下午一点，钱包余额剩余：", money)
print("现在是下午两点，钱包余额剩余：", money)
print("现在是下午三点，钱包余额剩余：", money)
print("现在是下午四点，钱包余额剩余：", money)

"""
"""
# 课后小练习
money=50
print("当前钱包余额：",money,"元")
# 买了冰激凌，花费10元
money=money-10
print("购买了冰激凌，花费:10元")
# 买了可乐，花费5元
money=money-5
print("购买了可乐，花费5元")
print("最终：钱包剩余：",money,"元")

print(type(666))
print(type(13.14))
print(type("黑马程序员"))
money_type=type(money)
print(money_type)
float_str=str(123.456)
print(type(float_str),float_str)

str_int=int("123456789")
print(type(str_int),str_int)
"""
# 标识符
# 规则一：内容限定 只能使用：中文 英文 数字 下划线，注意：不能以数字开头
# 错误1 1_name="张三" SyntaxError: invalid decimal literal
# 错误2 name_!="张三" NameError: name 'name_' is not defined
# 规则二：大小写敏感 弄不混
# 规则三：不可使用关键字


print("2**3=",2**3)
print("5//2=",5//2)
print("5%2=",5%2)

name="""
ddsdfv
dsvdf
dvfdf
这个三引号牛逼!"""
print(name)
print(type(name))
n='"黑马程序员'
print(n)
a="'黑马程序员'"
print(a)
m="\'黑马\'"
print(m)
a="\"程序\""
print(a)
x='\'员\''
print(x)

print("学IT来黑马"+"月薪过万")
name="黑马程序员"
address="建材城东路9号院"
tel=str(4006189090) # 不同类型不能拼接 把数字转化为str类型
print("我是："+name+"，我的地址是："+address+"，我的电话是："+tel)

name="zx"
year=20
height=177.5
message="我的名字：%s ,我的年龄：%d,我的身高：%.1fcm"%(name,year,height)
print(message)

num1=11
num2=11.345
print("数字11宽度限制5，结果是：%5d"% num1)
print("数字11宽度限制1，结果是：%1d"% num1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f"% num2)
print("数字11.345不限制，小数精度2，结果是%.2f"% num2)

# 不做精度控制，原样输出
name = "zx"
year = 20
height = 177.5
print(f"我是{name},我今年{year}岁了，我的身高{height}cm。")
print("2*9的结果是：%d"%(2*9))
print(f"9*9的结果是：{2*9}")
print("字符串在python中的类型为：%s"%type("字符串"))

name=input("请告诉我你是谁？")
print("我知道了，你是zx的男朋友:%s"%name)
num=input("请告诉我你的银行卡密码：？")

print("你的银行卡密码类型是：",type(int(num)))