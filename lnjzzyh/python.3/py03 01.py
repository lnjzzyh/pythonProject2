#第三章 选择和循环语句
#顺序结构 选择结构 循环结构
# 3.1 选择语句
# 1.单分支选择语句
# 格式：
# if 条件：
#     语句块
# 例：输入年龄判断是否成年，如果成年输出提示字符串'已成年！'
# age=int(input('请输入年龄：'))
# if age>=18:
#     print('已成年！')
# 2.双分支的if语句
# 格式
# if 条件：
#     语句块1
# else
#     语句块2
# 例：输入年龄判断是否成年，如果成年输出提示字符串'已成年！'
# 否则输出'未成年，还差？岁成年
# import math
#
# age=int(input('请输入年龄：'))
# if age>=18:
#     print('已成年！')
# else:
#     print('未成年，还差',18-age,'岁成年!')
# 练习输入两个整数，输出大着
# import math
#
# import math
#
# a=int(input('a:'))
# b=int(input('b:'))
# c=int(input('c:'))
# s=1/2*(a+b+c)
# area=math.sqrt(s*(s-a)*(s-b)*(s-c))
# print('area',area)
# else :
#     print('不能构成三角形')
# 3.多分支的if语句
# 格式：
# if 条件1：
#     语句块1
# elif 条件2：
#     语句块2
# .
# .
# .
# elif 条件n：
#      语句块n
# else：
#      语句块n+1
# 例：输入学生的分数[0,100],用多分支的选择结构转换为等级制。
# s<0 or s>100----error
# s>=90-----A
# s>=80-----B
# s>=70-----C
# s>=60-----D
#           E
# s=int(input('s:'))
# if s<0 or s>100:
#     print('分数无效！')
# elif s>=90:
#     print('A')
# elif s>=80:
#     print('B:')
# elif s>=70:
#     print('C')
# elif s>=60:
#     print('D')
# else:
#     print('E')
# 练习：假设用户名密码
# username='123abc'
# password='123456'
# us=input('Please enter your username:')
# pw=input('Please enter your password:')
# if us!=username:
#     print('ERROR211 The username is incorrect Please re-enter！')
# elif pw!=password:
#     print('ERROR210 The password is incorrect Please re-enter！')
# else:
#     print('Login succeeded！')
# 4.嵌套的选择语句
# if 条件1：
#     if 条件2：
#         语句块2
# else：
#     if  条件3：
#         语句块3
# else：
#     if  条件3：
#         语句块3
# else：
#     语句块4
# 输入3个整数，输出最大的整数
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if a>b:
    if a>c:
        print('最大值:',a)
    else:
        print('最大值：',c)

