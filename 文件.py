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
"""
# ========== 文件读写完整案例 ==========
# 1. write 写入内容到txt文件（w模式：覆盖原有全部内容）
with open("笔记.txt", "w", encoding="utf-8") as file:
    file.write("Python文件操作学习\n")
    file.write("写入文字、读取文字\n")
    file.write("with语法自动关闭文件，不用手动close()")

# 2. read 读取文件全部内容
with open("笔记.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("读取全部内容：")
print(content)

# 3. a模式：追加内容（不会覆盖旧内容，在末尾新增文字）
with open("笔记.txt", "a", encoding="utf-8") as file:
    file.write("\n这是追加进去的新一行文字")

# 4. 逐行读取文件内容
print("\n逐行读取：")
with open("笔记.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
