"""
new_str='This is a Python book'
a=new_str.count('is')
b=new_str.count('is',1,6)
print(a)
print(b)
sname='I want to study Python'
print("sname.title():",sname.title())
print("sname.upper():",sname.upper())
print("sname.lower():",sname.lower())
print("sname.swapcase():",sname.swapcase())
print("sname.capitalize():",sname.capitalize())
password=input("请输入你的密码（必须包含数字与字母）")
print("密码是否全是字母：",password.isalpha())
print("密码是否全是数字：",password.isnumeric())
print(f'是否以k开始：{new_str.startswith("k")}')
print(f'是否以k结束：{new_str.endswith("k")}')
str1=str(input("请输入字符串："))
print(str1.swapcase())
s=input("请输入一串字符：")
result=''
for ch in s:
    if ch.isalpha():
        result+=ch.swapcase()
    else:
        result+=ch
print(f"结果：{result}")"""
strs=input("请输入一个字符串：")
str_len=len(strs)
str_max=max(strs)
str_min=min(strs)
print(str_len)
print(str_max)
print(str_min)
contents=("'张三：一班，李四：二班，王五：三班，赵六：四班'")
import re
p=re.compile(r'.班')
for one in p.findall(contents):
    print(one)
import re
str="p2y21thon,p3ypu2p,py1gmy,copy,sleepy"
print(re.findall(r".*?p[0-9]+y\w*",str))\
    import re
phone_pattern=re.compile(r"^1[3-9]\d{9}$")
print(phone_pattern.match("13812345678"))
print(phone_pattern.match("12345678901"))
text='电话1：13811112222，电话2：13933334444'
print(phone_pattern.findall)