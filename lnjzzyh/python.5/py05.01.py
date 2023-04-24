#第五章 列表和元组
# 简单数据类型--int float str bool（布尔型true False）
# 复杂数据类型--list tuple dict set
# 5.1列表概述
# 1.定义：用中括号括起来的0个或多个数据有序序列
# l1=[]#空列表
# l2=[1,2,3,4]#同一数据
# l3=[1,1.2,'st',True,[1,2,3]]#不同类型
# print(type(l1),type(l2),type(l3))
# 2.列表的赋值与引用
# l1=[1,2,3,4]#列表赋值
# l2=l1#引用
# l1[3]=5
# print(l1)
# print(l2)
# 3.通用操作系统在列表中的应用
#(1)索引
# l=['a','b','c','d']
# 'a''d'
# print(l[0],l[-4])
# print(l[3],l[-1])
# (2)分片
# 'a''b''c'
# print(l[0:3])
# 反向输出
# print(l()[::-1])
# (3)+--连接*--复制
# print([1,2,3]+[4,5,6])
# print([1,2,3]*3)
##(4)len()max()min()
# print(len(l),max(l),min(l))
# 4.列表的遍历
# (1)while循环遍历
# animal=['snake','tiger','elephant','bird','pander']
# d=len(animal)
# i=0
# while i<=d-1:
#     print(animal[i],end='')
#     i +=1
# (2)for 循环遍历
# 格式
# for 变量 in 序列：
# 循环
# animal=['snake','tiger','elephant','bird','pander']
# for an in animal:
#     print(an,end='')
# 5.list()函数--转换列表
# s='hello'
# l=list(l)
##0,2,4,6,8....20
#print(range()
#5.2列表的操作方法
#find() count() strip() join()
#replace() strip() upper() lower() isalnum()--字符串的操作方法
#列表是可变的数据类型 增 删 改 查
# 字符串是不可变的数据类型
# (1)增加列表中的数据
#(1)增加列表中的数据
#---append()方法---向列表的末尾追加一个数据
# l=[1,2,3]
# l.append(4)
# print(l)
# ---insert()方法：---向指定列表中指定位置添加数据
# l=[1,3,4]
# l.insert(1,2)
# print(l)
# ---extend()方法---向列表末尾追加多个数据
# l=[1,2]
# l.extend([3,4,5,6])
# print(l)
# ----分片增加数据
# l=[1,2,3,8,9,10]
# l[3:3]=[4,5,6,7]
# print(l)
# 2.查找和统计
# (1)查找---index()方法
# animal=['snake','tiger','elephant','bird','pander']
# x=input('请输入动物名称')
# # 成员运算符 in not in
# if x in animal:
#     print('该动物名称的索引值是：{}'.format(animal.index(x)))
# else:
#     print('该动物名称不存在！')
# (2)统计--count()方法
# l=[1,2,2,2,3]
# c=l.count(2)
# print(c)
# 练习：
# s='12345'
# 将s转换为列表l.
# l=list(s)
# print(l)
# 计算l的长度和最大值
# print(len(s),max(s))
# 将l反向输出
# print(l[::-1])
# 向l列表的末尾添加6，,7，,8
# l.extend([6,7,8])
print(1)
# (3)删除列表中的数据
# (1)del命令
# l=[1,2,3,4]
# del l[1]
# print(l)
#(2)pop()方法:默认删除列表中的最后一个数据并获取被删除的数据。
# l=[1,2,3,4]
# # d=l.pop()
# # print(d)
# # print(l)
# d=l.pop(2)
# print(l)
# (2)remove():删除列表中的一个匹配项
# l=['a','b','a']
# # l.remove('a')
# # print(l)
# while 'a' in l:
#     l.remove('a')
# print(l)
# (4)分片删除列表中的数据
# l=[1,2,3,4,5,6]
# l[1:5]=[]
# print(l)
# (4)列表排序
#(1)reverse()方法：将列表中的数据反向存放
# l1=[4,3,1,2]
# l1.reverse()
#  print(l1)
# (2)sort()方法：将列表中的数据升序或降序排列。
# --升序
# l=[4,1,2,5,3]
# l.sort()
# print(l)
# --降序
# l.sort(reverse=True)
# print(l)
# --字符串升序
# l=['abc','a','abcd','ab']
# l.sort(key=len)
# print(l)
# --字符串降序
# l.sort(key=len,reverse=True)
# print(l)
# (3)sorted()函数排序
# --数字降序
# l=[4,1,2,5,3]
# l=sorted(l,reverse=True)
# print(l)
# --字符串降序
# l=sorted(l,key=len,reverse=True)
# print(l)
# 字符串升序
# l=['abc','a','abcd','ab']
# l=sorted(l，key=len)
# print(l)
# 字符串降序
# l=sorted(l,key=len,reverse=True)
# print(l)
# 5.3元组(tuple)
# 1.元组的定义:用小括号括起来的0个或多个数据的有序序列
# 元组是不可变的数据类型
# t1=()#空元组
# t2=(2,)
# t3=(1,2,3)
# t4=(1,1,2,'as',[1,2],(1,))
# print(type(t2))
#2.索引获取元组中的数据
# t=(1,2,3,4,5)
# 输出1,5
# print(t[0],t[-1])
# 3.分片获取元组中的多个数据
# 输出2,3,4
# print(t[1:4])
# 4. +*在元组中的应用
# 输出1,2,3,4,5,6,7,8
# print(t + (7,8))
# 输出(1234512345)
# print(t*2)
# 5.len()max()min()
# print(len(t),max(t),min(t))
# 6.遍历元祖
# for
# t=(1,2,3,4,5)
# for t1 in t:
#     print(t1,end='')
# while
# d=len(t)
# i=0
# while i<d-1:
#     print(t[i])
#     i+=1
# 5.4案例
# 编写程序完成简易计算器的四则运算.(+,-,*,/).
operater=['+','-','*','/']
num1=float(input('第一个数字: '))
oper=input('运算符: ')
num2=float(input('第二个数字: '))
if oper in operater:
    if oper=='+':
        print('输出结果',num1+num2)
    elif oper=='-':
        print('输出结果:',num1-num2)
    elif oper=='*':
        print('输出结果:',num1*num2)
    else:
        print('输出结果:',num1/num2,)
else:
    print('输入有误')