"""
#打开文件
f=open('D:\\wenjian\\数据容器.txt', 'r', encoding='utf-8')
print(type(f))
#读取文件
#读取10个字节的结果：{f.read(10)}
print(f"读取10个字节的结果：{f.read(10)}")
print(f"读取全部字节的结果：{f.read()}")
print("--------------------------------------------")
#读取文件-readlines()
lines=f.readlines()
print(type(lines))
print(lines)
#一次读取一行
f=open('D:\\wenjian\\数据容器.txt', 'r', encoding='utf-8')
line1=f.readline()
line2=f.readline()
line3=f.readline()
print(f"第一行的数据是：{line1}")
print(f"第二行的数据是：{line2}")
print(f"第三行的数据是：{line3}")
#利用循环读取每一行
f=open('D:\\wenjian\\数据容器.txt', 'r', encoding='utf-8')
for line in f:
    print(line)
#解除文件占用
f.close()
#with open语法
with open('D:\\wenjian\\数据容器.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)
#打开文件，不存在的文件，r,w,a
import time
f=open("D:/wenjian/test.txt","w",encoding="utf-8")
#write写入
f.write("Hello World!!!") #创建但是空白
#flush 刷新
#f.flush()
#close 关闭
f.close()
#文件存在
f=open("D:/wenjian/test.txt","w",encoding="utf-8")
f.write("黑马程序员")
f.close()
#打开文件，不存在的文件
f=open("D:/wenjian/project.txt","a",encoding="utf-8")
f.write("黑马程序员")
f.flush()
f=open("D:/wenjian/project.txt","a",encoding="utf-8")
f.write("学python，就来黑马程序员")
f.close()
"""
