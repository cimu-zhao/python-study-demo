"""
//数据容器
//一.列表
name_list=['王力宏','周杰伦','林俊杰','张学友','刘德华']
print(name_list)
name_list=['itheima','itcast','python']
print(name_list)
print(len(name_list))
print(type(name_list))
my_list=[[1,2,3],[4,5,6],[7,8,9]]
print(my_list)
print(len(my_list))
print(type(my_list))
//列表下标索引
print(name_list[0])
print(name_list[1])
print(name_list[2])
print(name_list[-1])
print(name_list[-2])
print(name_list[-3])
print(my_list[1][1])
print(my_list[1][-2])
//列表的方法
//查询
name_list=['itheima','itcast','python']
index=name_list.index('itheima')
print(f"itheima在列表中的下标索引是：{index}")
//修改
name_list=['itheima','itcast','python']
name_list[0]="666"
print(f"列表被修改后元素值是{name_list}")
//插入
name_list=['itheima','itcast','python']
name_list[0]="666"
name_list.insert(1,"best")
print(f"列表插入元素后：{name_list}")
//追加
name_list=['itheima','itcast','python']
name_list[0]="666"
name_list.insert(1,"best")
name_list.append("黑马程序员")
print(f"列表在追加元素后：{name_list}")
my_list=[[1,2,3],[4,5,6],[7,8,9]]
name_list.extend(my_list)
print(f"列表在追加一个新的列表后，结果是：{name_list}")
//删除
(1)del
my_list=[[1,2,3],[4,5,6],[7,8,9]]
del my_list[1]
print(my_list)
(2)pop
name_list=['itheima','itcast','python']
element=name_list.pop(2)
print(f"利用pop方法后取出后的列表内容是{name_list}，取出的元素是：{element}")
(3)remove 只能删除多个出现的第一个元素 如果想删除第二个应用两次
name_list=['itheima','itcast','itheima','python','itheima']
name_list.remove('itheima')
print(name_list)
(4)清空
name_list=['itheima','itcast','python']
name_list.clear()
print(f"列表被清空后{name_list}")
//统计
name_list=['itheima','itcast','itheima','python','itheima']
print(name_list.count('itheima'))
name_list=['itheima','itcast','itheima','python','itheima']
print(len(name_list))
//列表遍历
def list_while_func():
    my_list=["传智教育","黑马程序员","Python"]
    index=0
    while index<len(my_list):
        element=my_list[index]
        print(f"列表的元素：{element}")
        index=index+1
list_while_func()
def list_while_func():
    my_list=[1,2,3,4,5]
    for element in my_list:
        print(f"列表的元素：{element}")
list_while_func()
//二.元组
t1=(1,"hello",True)
t2=()
t3=tuple()
print(f"t1的类型是：{type(t1)},内容是：{t1}")
print(f"t2的类型是：{type(t2)},内容是：{t2}")
print(f"t3的类型是：{type(t3)},内容是：{t3}")
t4=("hello",)
print(f"t4的类型是：{type(t4)},内容是：{t4}")
t5=((1,2,3),(4,5,6))
print(f"t5的类型是：{type(t5)},内容是：{t5}")
//取出某一个元素
num=t5[1][-1]
print(num)
//元组查询
t6=("传智教育","黑马程序员","Python")
index=t6.index("Python")
print(f"在元组t6中查找Python,对应的下标是；{index}")
//统计
t7=("传智教育","黑马程序员","Python","黑马程序员","黑马程序员","黑马程序员")
num=t7.count("黑马程序员")
print(f"在元组t7中统计黑马程序员的数量有：{num}个")
//元组的遍历：while循环
t8=("传智教育","黑马程序员","Python","黑马程序员","黑马程序员")
index=0
while index<len(t8):
    print(f"元组的元素有：{t8[index]}")
    index+=1
//元组的遍历：for循环
t8=("传智教育","黑马程序员","Python","黑马程序员","黑马程序员")
for element in t8:
    print(f"元组的元素有：{element}")
//元组嵌套列表 可修改列表
t9=('itheima','itcast','python',[1,2,3],[4,5,6])
print(f"t9的内容是：{t9}")
t9[3][-1]=2
t9[4][0]=5
print(f"t9的内容是：{t9}")
//三 字符串
//字符串定义和下标查询
my_str="itheima and itcast"
value=my_str[2]
value2=my_str[-16]
value3=my_str[-7]
print(value)
print(value2)
print(value3)
num=my_str.index("and")
print(f"and的起始下标是：{num}")
//字符串的替换
my_str="itheima and itcast"
new_my_str=my_str.replace("it","程序")
print(new_my_str)
//字符串的分割
my_str="hello Python itheima itcast"
my_str_list=my_str.split(" ")
print(f"将字符串{my_str}进行split切分之后得到：{my_str_list},类型是：{type(my_str_list)}")
//字符串的规整
my_str="   itheima and itcast   "
new_my_str=my_str.strip()#不传入参数
print(f"字符串{my_str}被strip后，结果是：{new_my_str}")
my_str="12itheima and itcast21"
new_my_str=my_str.strip("12")
print(f"字符串{my_str}被strip后，结果是：{new_my_str}")
//字符串的统计
my_str="itheima and itcast"
count=my_str.count("it")
print(f"字符串{my_str}中it出现的个数：{count}")
print(len(my_str))
//序列
#对List进行切片，从1开始，4结束，步长1
my_list=[0,1,2,3,4,5,6]
result1=my_list[1:4]  #步长默认值是1可以省略不写
print(f"结果1:{result1}")

#对tuple进行切片，从头开始到最后结束，步长1
my_tuple=(0,1,2,3,4,5,6)
result2=my_tuple[:]  #起始和结束不写表示从头到尾，步长1可以省略
print(f"结果2:{result2}")

#对str进行切片，从头开始到最后结束，步长2
my_str="01234567"
result3=my_str[::2]
print(f"结果3:{result3}")

##对str进行切片，从头开始到最后结束，步长-1
my_str1="01234567"
result4=my_str1[::-1]
print(f"结果4：{result4}")

#对List进行切片，从3开始，1结束，步长-1
my_list2=[0,1,2,3,4,5,6]
result5=my_list2[3:1:-1]
print(f"结果5：{result5}")

#对tuple进行切片,从头开始到最后结束,步长1
my_tuple2=(0,1,2,3,4,5,6)
result6=my_tuple2[::-2]
print(f"结果6：{result6}")
//四,集合
my_set={"传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima"}
my_set_empty=set()
print(f"定义的集合内容是：{my_set},类型是：{type(my_set)}")
print(f"定义的空集合内容是：{my_set_empty},类型是：{type(my_set_empty)}")
//添加
my_set.add("Python")
print(my_set)
//移除
my_set.remove("黑马程序员")
print(my_set)
//随机取出一个元素
element=my_set.pop()
print(f"取出：{element},还剩：{my_set}")
//清空
my_set.clear()
print(my_set)
//取出两集合差集（集合均不改变）
set1={1,2,3}
set2={1,5,6}
set3=set1.difference(set2)
print(set1)
print(set2)
print(set3)
//消除两集合差集（集合1改变2不改变）
set1.difference_update(set2)
print(set1)
print(set2)
//2集合合并
set1={1,2,3}
set2={1,5,6}
set3=set1.union(set2)
print(set1)
print(set2)
print(set3)
//统计长度
set1={1,2,3,4,5,6,7,8,9,7,5,3}
print(len(set1))#集合自带去重
//集合的遍历（支持for循环）
set1={1,2,3,4,5,6}
for element in set1:
    print(element)
//五,字典
//定义
my_dict1={"王力宏":99,"周杰伦":88,"林俊杰":77}
my_dict2={}
my_dict3=dict()
print(f"字典的内容是：{my_dict1},类型是：{type(my_dict1)}")
print(f"字典的内容是：{my_dict2},类型是：{type(my_dict2)}")
print(f"字典的内容是：{my_dict3},类型是：{type(my_dict3)}")
print(my_dict1["王力宏"])
stu_score_dict={
    "王力宏":{
        "语文":77,
        "数学":66,
        "英语":33
    },"林俊杰":{
        "语文":88,
        "数学":86,
        "英语":55
    },"周杰伦":{
        "语文":99,
        "数学":96,
        "英语":66
}
}
print(f"学生的考试信息：{stu_score_dict}")
print(stu_score_dict["周杰伦"]["语文"])
print(stu_score_dict["林俊杰"]["英语"])
//新增与更新
my_dict={"周杰伦":99,"林俊杰":88,"张学友":77}
my_dict["张信哲"]=66
print(f"新增后：{my_dict}")
my_dict["周杰伦"]=98
print(my_dict)
//删除与清空
my_dict={"周杰伦":99,"林俊杰":88,"张学友":77}
element=my_dict.pop("周杰伦")
print(my_dict)
print(element)
my_dict.clear()
print(my_dict)
//字典的遍历
my_dict={"周杰伦":99,"林俊杰":88,"张学友":77}
keys=my_dict.keys()
print(keys)
for key in keys:
    print(f"字典的key是:{key}")
    print(f"字典的value是：:{my_dict[key]}")
for key in my_dict:
    print(f"字典的key是:{key}")
    print(f"字典的value是：:{my_dict[key]}")
//统计数量
print(len(my_dict))
//数据容器的通用操作
my_list=[1,2,3,4,5]
my_tuple=(1,2,3,4,5)
my_str="abcdefg"
my_set={1,2,3,4,5}
my_dict={"key1":1,"key2":2,"key3":3,"key4":4,"key5":5,}
#len元素个数
print(f"列表 元素个数有：{len(my_list)}")
print(f"元组 元素个数有：{len(my_tuple)}")
print(f"字符串 元素个数有:{len(my_str)}")
print(f"集合 元素个数有：{len(my_set)}")
print(f"字典 元素个数有:{len(my_dict)}")
#max函数
print(f"列表 最大的元素是：{max(my_list)}")
print(f"元组 最大的元素是：{max(my_tuple)}")
print(f"字符串 最大的元素是:{max(my_str)}")
print(f"集合 最大的元素是：{max(my_set)}")
print(f"字典 最大的元素是:{max(my_dict)}")
#min函数
print(f"列表 最小的元素是：{min(my_list)}")
print(f"元组 最小的元素是：{min(my_tuple)}")
print(f"字符串 最小的元素是:{min(my_str)}")
print(f"集合 最小的元素是：{min(my_set)}")
print(f"字典 最小的元素是:{min(my_dict)}")
#类型转换:容器转列表
print(f"列表转列表的结果是：{list(my_list)}")
print(f"元组转列表的结果是：{list(my_tuple)}")
print(f"字符串转列表的结果是:{list(my_str)}")
print(f"集合转列表的结果是：{list(my_set)}")
print(f"字典转列表的结果是:{list(my_dict)}")
#类型转换:容器转元组
print(f"列表转元组的结果是：{tuple(my_list)}")
print(f"元组转元组的结果是：{tuple(my_tuple)}")
print(f"字符串转元组的结果是:{tuple(my_str)}")
print(f"集合转元组的结果是：{tuple(my_set)}")
print(f"字典转元组的结果是:{tuple(my_dict)}")
#类型转换:容器转字符串
print(f"列表转字符串的结果是：{str(my_list)}")
print(f"元组转字符串的结果是：{str(my_tuple)}")
print(f"字符串转字符串的结果是:{str(my_str)}")
print(f"集合转字符串的结果是：{str(my_set)}")
print(f"字典转字符串的结果是:{str(my_dict)}")
#容器转换：容器转集合
print(f"列表转集合的结果是：{set(my_list)}")
print(f"元组转集合的结果是：{set(my_tuple)}")
print(f"字符串转集合的结果是:{set(my_str)}")
print(f"集合转集合的结果是：{set(my_set)}")
print(f"字典转集合的结果是:{set(my_dict)}")
#容器排序
my_list=[3,1,2,5,4]
my_tuple=(5,2,3,1,4)
my_str="cgfaebd"
my_set={4,2,5,3,1}
my_dict={"key2":1,"key5":2,"key1":3,"key4":4,"key3":5,}

print(f"列表对象排列的结果是：{sorted(my_list)}")
print(f"元组对象排列的结果是：{sorted(my_tuple)}")
print(f"字符串对象排列的结果是:{sorted(my_str)}")
print(f"集合对象排列的结果是：{sorted(my_set)}")
print(f"字典对象排列的结果是:{sorted(my_dict)}")

print(f"列表对象反向排列的结果是：{sorted(my_list,reverse=True)}")
print(f"元组对象反向排列的结果是：{sorted(my_tuple,reverse=True)}")
print(f"字符串对象反向排列的结果是:{sorted(my_str,reverse=True)}")
print(f"集合对象反向排列的结果是：{sorted(my_set,reverse=True)}")
print(f"字典对象反向排列的结果是:{sorted(my_dict,reverse=True)}")
"""
print('bc'<'cb')