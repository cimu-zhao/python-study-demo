"""
字符串相关功能的工具模块
"""
def str_reverse(s):
    #将字符串进行反转的操作
    #:param s: 将被反转的字符串
    #return  反转后的字符串
    return s[::-1]

def substr(s,x,y):
    #功能按照给定的下标完成给定字符串的切片
    #:param s: 将被反转的字符串切片
    #:param x:
    #:param y:
    #:return
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("黑马程序员"))
    print(substr("黑马程序员",1,3))