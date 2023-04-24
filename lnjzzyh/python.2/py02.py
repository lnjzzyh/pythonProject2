#第二章 python编程基础
#1.变量----程序运行中值可以改变的量.
#2.变量命名---字母数字下划线。不能以数字开头.
#例如：a1,a 1, a1, 1a(错误)
#python中关键字不能用作变量名.
#例如：int float if for 不能用作变量名.
#3.变量命名的常用形式.
#(1)小驼峰形式----MyName Mycore.
#(2)大驼峰形式----myName myScore.
#(3)下划线连接----my name my score.
#4.python中的数据类型
#简单的数据类型--int float str bool(True False) -布尔型
#复杂的数据类型--字典 列表 元组 集合
#整型--int-表示任意大小的整数.
# 120 3214 56789 -9876 -1214
#浮点型---float--表示小数
#例如：3.14 5.6  -9.8
#字符串---str---表示字符串.
#例如:'student' "hello"
#5.变量的赋值
#例如：单个变量赋值
#a=3
#b=3.2
#s="root"
#多个变量赋值
#a=b=c=1
#a,b,c=1,3,4'abc'
#6.type()函数---查看变量的数据类型.
# a=1
# b=2.5
# s='asd'
# print(type(a),type(b),type(s))
#7.运算符
#（1）算术运算符--"+ - * /"(除取小数) //(除取整数) %（求余数） **（幂运算）
# a=12
# b=5
# print('a+b=',a+b)
# print('a/b=',a/b)
# print('a//b',a//b)
# print('a%b',a%b)
# print('a**2',a**2)
#(2)复核赋值运算符 += -= /= %=
#例如： a+=2-----a=a+2
# a=3
# a +=3
# a -=3
# a *=3
# a /=3
# a %=3
# print('a=',a)
#（3）关系运算符---< <=> >= == !=
#<= 包含两个条件小于或等于哪个条件表达式均成立
#>= 包含两个条件大于或等于哪个条件表达式均成立
#==
#!=
# a=5
# b=3
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# print(a==b)
# print(a!=b)
#（4）逻辑运算符----and（与）or（或）not（非）
#逻辑值---True False
# print(3 and 4)#---逻辑与前后的值均为真结果是后面表达式的值。
# print(0 and 4)#---逻辑与前面的值为0结果为0
# a=3
# b=2
# print(a>b and a==b)
#逻辑与连接的关系表达式的逻辑值为真结果为后面表达式的值
# print(a<b and a==b)
#逻辑与连接的关系表达式的逻辑值为假结果即为假
# print(2 or 4)---逻辑或前面若非0的数值结果即为前面的数值
# print(0 or 4)---逻辑或前面若非0的数值结果即为后面的数值
# print(3>2 or 4<5)
#逻辑或连接关系表达式前面表达式逻辑值为真结果即为真
# print(3<2 or 4>5)
#逻辑或连接关系表达式前面表达式逻辑值为真结果为后面表达式的值
# print(not 3<4)
# print(not 3>4)
#成员运算符---（in）（not in）
#判断某个值是否是列表（[]）或元组--（）中的成员
#若是成员返回值为真--True，否则返回值为False，
# list1=[1,2,3,4]
# ls=3
# print(ls in list1)
# print(ls not in list1)
#（6）身份运算符---（is），（is，not）
#若引用同一个值返回值为True，否则为False。
# a=10
# b=20
# print(a is b)
# print(a is not b)
#2.3输出函数---print（）
#1.输出字符串----'Morning'
# print('Morning')
# 2.输出变量的值
# a=45
# s='abc'
# c=5.6
# print(a,c,s)
# 3.输出字符串和变量中的值
# print('a=',a,'s=','s=','c=',c)
# 2.4输入函数---input()函数
# --字符串接收键盘输入的数据
# a=input('请输入a：')
# print(a,type(a))
# 2.强制类型转换
#(1)int()---强制转换为整型
# s1=int(input('s1='))
# s2=int(input('s2='))
# print('s1+s2',s1+s2)
#(2)float()---强制转换为浮点型
# s1=input('s1=')
# s2=input('s2=')
# s1=float(s1)
# s2=float(s2)
# print('s1+s2=',s1+s2)
# (1)导入关键字模块
# import keyword
# print(keyword.kwlist)
# 2.导入数学模块
# import math
# print(math.sqrt(16))
#2.5 案例
# 输入3个数据作为三角形的三边长，计算三角形的面积。
#a,b,c----int(input())
# s=1/2*(a+b+c)
# area=sqrt(s*(s-a)*(s-b)*(s-c))
# print
import math

import math
a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))
s=1/2*(a+b+c)
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print('area=',area)



