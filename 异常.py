"""
f=open("D://wenjian//abc.txt","r",encoding="utf-8")
结果:文件未找到
Traceback (most recent call last):
FileNotFoundError: [Errno 2] No such file or directory: 'D://wenjian//abc.txt'
#捕获常规异常
try:
    f=open("D://wenjian//linux.txt","r",encoding="utf-8")
except:
    print("文件不存在，我将open的模式，改用w模式去打开")
    f=open("D://wenjian//linux.txt","w",encoding="utf-8")
#捕获指定异常
try:
    print(name)
except NameError as e:
    print("出现了变量未被定义的异常")
    print(e)
#捕获多个异常
try:
    1/0
except (NameError,ZeroDivisionError) as e:
    print("出现了变量未被定义 或者 除以0的异常错误")
#未正确设置捕获异常类型，将无法捕获异常
#捕获所有异常
try:
    print(name)
except Exception as e:
    print("出现异常了")
#
try:
    f=open("D://wenjian//linux.txt","r",encoding="utf-8")
except Exception as e:
    f=open("D://wenjian//linux.txt","w",encoding="utf-8")
else:
    print("没有异常，真开心")
finally:
    f.close()
#异常的传递性
def func1():
    print("func1 开始执行")
    num=1/0
    print("func1 结束执行")
#定义一个无异常的方法 调用上面的方法
def func2():
    print("func2 开始执行")
    func1()
    print("func2 结束执行")
def main():
    try:
        func2()
    except Exception as e:
        print("出现异常了，异常的信息是：{e}")
main()
"""

