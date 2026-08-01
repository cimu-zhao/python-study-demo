"""
//1
name="传智播客"
stock_price=19.99
stock_code="003032"
stock_price_daily_grown_factor=1.2
growth_daily=7
print(f"公司：{name},股票代码:{stock_price},当前股价:{stock_price}")
final_price=stock_price*(stock_price_daily_grown_factor**growth_daily)
print("每日增长系数是：%.1f,经过%d天的增长后，股价涨到了：%.2f"%(stock_price_daily_grown_factor,growth_daily,final_price))
//2
user_name=input()
user_type=input()
print("您好：%s,您是尊贵的：%s用户，欢迎您的光临。"%(user_name,user_type))
//3
print("欢迎来到黑马儿童幼儿园，儿童免费，成人收费。")
age=int(input("请输入你的年龄："))
if age>=18:
    print("您已成年，游玩需要补票10元。")
else:
    print("您未成年，可以免费游玩。")
print("祝您游玩愉快。")
//4
print("欢饮来到黑马动物园。")
height=int(input("请输入你的身高(cm):"))
if height>=120:
    print("您的身高超出120cm,游玩需要补票10元。")
else:
    print("您的身高未超出120cm,可以免费游玩。")
print("祝您游玩愉快。")

//5
if int(input("请输入第一次猜想的数字："))==10:
    print("恭喜你第一次就猜对了")
elif int(input("不对，再猜一次："))==10:
    print("猜对了")
elif int(input("猜错了，再猜最后一次："))==10:
    print("恭喜最后一次猜对了")
else:
    print("Sorry,全部猜错了，我想的是：10")

//6
i=1
sum=0
while i<=100:
    sum=sum+i
    i=i+1
print(sum)

//7
name="itheima is a brand of itcast"
count=0
for x in name:
    if x=="a":
        count=count+1
print(f"itheima is a brand of itcast 中一共含有：{count}个字母a")

//8
count = 0
for i in range (1,100):
    if i%2==0:
        count=count+1
print(f"1到100（不含100本身）范围内，有{count}个偶数。")

//9 for循环九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end='')
    print()
//9
def f():
    print("欢迎来到黑马程序员！")
    print("请出示您的健康码以及72小时核酸证明！")
    #或者
    print("欢迎来到黑马程序员！\n请出示您的健康码以及72小时核酸证明！")
f()
//10
def f(x):
    if x<=37.5:
        print(f"欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！\n体温测量中，您的体温是：{x}度，体温正常请进！")
    else:
        print(f"欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！\n体温测量中，您的体温是：{x}度，需要隔离！")
f(37.3)
f(39.3)
//10银行
money=5000000
name=None
name=input("请输入您的姓名:")
def inquire(show_header):
    if show_header:
        print("---------查询余额---------")
    print(f"{name},您好，您的余额剩余：{money}元")
def saving(num):
    global money
    money+=num
    print("---------存款---------")
    print(f"{name},您好，您存款{num}元成功。")
    inquire(False)
def get():
    global money
    money-=num
    print("---------取款---------")
    print(f"{name},您好，您取{num}元成功。")
    inquire(False)
def main():
    print("---------主菜单---------")
    print(f"{name}您好，欢迎来到黑马银行ATM,请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")
while True:
    keyboard_input=main()
    if keyboard_input=="1":
        inquire(True)
        continue
    elif keyboard_input=="2":
        num=int(input("您想要存多少钱？请输入："))
        saving(num)
        continue
    elif keyboard_input=="3":
        num = int(input("您想要取多少钱？请输入："))
        continue
    else:
        break

//11 列表
my_list=[21,25,23,22,20]
my_list.append(31)
print(my_list)
my_list1=[29,33,30]
my_list.extend(my_list1)
print(my_list)
element=my_list.pop(0)
print(element)
print(my_list)
element1=my_list.pop(-1)
print(element1)
print(my_list)
print(my_list.index(31))

//12列表遍历
my_list=[1,2,3,4,5,6,7,8,9,10]
index=0
even_list=[]
while index<len(my_list):
    element=my_list[index]
    if element%2==0:
        even_list.append(element)
    index=index+1
print(even_list)
my_list=[1,2,3,4,5,6,7,8,9,10]
even_list=[]
for element in my_list:
    if element%2==0:
        even_list.append(element)
print(even_list)
//13 元组嵌套
bab=('周杰伦',11,["football","music"])
num=bab.index(11)
print(num)
name=bab[0]
print(name)
bab[2].remove("football")
print(bab)
bab[2].append("coding")
print(bab)
//14 分割字符串的练习
my_str="itheima itcast boxuegu"
count=my_str.count("it")
print(count)
new_my_str=my_str.replace(" ","|")
print(new_my_str)
new_str=new_my_str.split("|")
print(new_str)
//15.序列切片练习
//(1)取出切片然后倒序
my_str="万过薪月，员序程马黑来，nohtyP学"
my_str1=my_str[5:10:-1]
print(my_str1)
  ==my_str="万过薪月，员序程马黑来，nohtyP学"
    my_str1=my_str[5:10:][::-1]
    print(my_str1)
//(2)倒序取出切片
my_str="万过薪月，员序程马黑来，nohtyP学"
my_str1=my_str[::-1][9:14]
print(my_str1)
//(3)split分割“，”，replace替换“来”为空 倒序取出
my_str="万过薪月，员序程马黑来，nohtyP学"
my_str2=my_str.replace("来","")
print(my_str2)
my_str3=my_str2.split("，")
print(my_str3)  #得到列表
my_str4=my_str3[1][::-1] #多重列表注意两个下标
print(my_str4)
==my_str="万过薪月，员序程马黑来，nohtyP学"
  my_str1=my_str.split("，")[1].replace("来","")[::-1]
  print(my_str1)
//16.集合练习
my_list=['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
my_set=set()
for element in my_list:
    my_set.add(element)
print(my_set)
//17.字典练习
info_dict={
    "王力宏":{
        "部门":"科技部",
        "工资":3000,
        "级别":1
    },
    "周杰伦":{
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "林俊杰":{
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "张学友":{
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德华":{
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}
print(info_dict)
for name in info_dict:
    if info_dict[name]["级别"]==1:
        new_info_dict=info_dict[name]
        new_info_dict["级别"]=2
        new_info_dict["工资"]+=1000
        info_dict[name]=new_info_dict
print(f"升职加薪后：{info_dict}")
//18 文件练习
//（1）读取全部内容 用字符串count方法统计itheima出现数量
f=open("D:\wenjian\word.txt","r",encoding="utf-8")
content=f.read()
count=content.count("itheima")
print(count)
//(2)用strip对字符串进行规整，split删除空格
f=open("D:\\wenjian\\word.txt","r",encoding="utf-8")
count=0
for line in f:
    line=line.strip() #去除开头和结尾的空格和换行符
    words=line.split(" ")
    for word in words:
        if word=="itheima":
            count+=1
print(count)
f.close()
"""
