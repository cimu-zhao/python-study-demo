"""
#用import导入time模块使用sleep功能（函数）
import time #导入Python内置的time模块（time.py这个代码文件）
print("你好")
time.sleep(5)
print("我好")
#用from import导入time模块使用sleep功能（函数）
from time import sleep
print("你好")
sleep(5)
print("我好")
#用 * 导入time模块使用sleep功能（函数）
from time import * # *表示全部的意思
print("你好")
sleep(5)
print("我好")
#别名
import time as t
print("你好")
t.sleep(5)
print("我好")
#自定义模块
import my_modulel1
my_modulel1.test(10,20)
from my_module1 import test
test(20,30)
#后替换前
from my_module1 import test
from my_module2 import test
test(20,10)
#模块导入
from my_module1 import *
testA(1,2)
testB(2,1)
"""



