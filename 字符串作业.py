"""1. (程序题)
任务1、编写一个注册验证程序，设定如下条件：

（1）用户名必须以下划线“_”开头，长度必须在3～30个字符之间；

（2）密码必须由下划线、数字和字母共同组成，不允许有其他符号，长度必须在8～16个字符之间。

运行程序，程序执行结果如下。


import re
user_name=input("请输入用户名：")
password=input("请输入密码：")
if user_name[0]!='_':
    print("用户名请使用下划线")
elif len(user_name)<3 or len(user_name)>30:
    print("用户名长度超出限制")
elif len(password)<8 or len(password)>16:
    print("密码长度超出限制")
elif password.find('_')==-1:
    print("密码中未输入下划线")
else:
    if re.search(r'[a-zA-Z]',password) and re.search(r'[0-9]',password):
        print("恭喜您，注册成功！")
    else:
        print("密码中有其他符号，注册失败")
2. (程序题)
敏感词替换。给定一个字符串，
判断字符串中的文字是否是敏感词汇
（敏感词汇可以自己定义），
如果存在则使用*替换。运行程序，程序执行结果如下。
sensitive = ["垃圾", "暴力", "赌博", "诈骗"]

sensitive = ["垃圾", "暴力", "赌博", "诈骗"]
content=input("请输入文本：")
for  word in sensitive:
    content=content.replace(word,"**",len(word))
print(f"替换后：{content}")

3.输入一行字符，分别统计出其中英文字母、空格、数字和
其它字符的个数。运行程序，程序执行结果如下
# 初始化计数器
str=0
blank=0
digit=0
other=0
s=input("请输入一行字符：")
for c in s:
    if c.isalpha():
        str+=1
    elif c.isspace():
        blank+=1
    elif c.isdigit():
        digit+=1
    else:
        other+=1
print(f"英文字母个数：{str}个，空格个数：{blank}个，数字个数{digit}个，其它字符个数{other}个")


结果
第1/1条 运行结果

运行结果错误,该组未通过
4. (程序题)
文本进度条。编写程序，模拟输出简单的非刷新文本进度条。要求按照任务执行百分比将整个任务划分为100个单位，每执行10%输出一次进度条，每行输出包含进度百分比、代表已完成部分（）和未完成部分（..）的两种字符，以及一个跟随完成度前进的小箭头，风格如下：

%10 [->..................]

print("--------------执行开始--------------")
for percent in range(0, 101, 10):
    star_num=percent//10*2
    dight_num =20-star_num-1
    stars="*"*star_num
    dights="."*dight_num
    print(f"%{percent:2d}[{stars}->{dots}]")
print("--------------执行结束--------------")
"""
