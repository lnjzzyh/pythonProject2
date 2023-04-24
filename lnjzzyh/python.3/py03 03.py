#3.3 循环嵌套----for
# 1.格式
# for 变量1 in 序列1:
#     for 变量2 in 序列2:
#         循环体
# for j in range(1,3):
#     for j in range(1,4):
#         print('*',end='')
#     print()
#i=1 j=1*j=2*j=3*
#i=2 j=1*j=2*j=3*
#嵌套特点：外层变量每取一个值内层从起始值到最大值循环一周。
# 例题1：
# 九九乘法表----1
# 1*1=1 1*2=2 1*3=3.....1*9=9
# 2*1=2 2*2=4 2*3=6.....2*9=18
# .
# .
# .
# 9*1=9 9*2=18 9*3=27...9*9=81
# range=(1,10)
# for i in range(1,10):
#     for j in range(1,10):
#         print(i,'*',j,'=',i*j,end='')
#     print()
# 九九乘法表----2
# 1*1=1 2*1=2....9*1=9
# 1*2=2 2*2=4....9*2=18
# .
# .
# .
# 9*1=9 9*2=18 9*3=27...9*9=81
# for i in range(1,10):
#     print(j,'*',i,'=',i*j,end='')
#     print()
# 九九乘法表----3
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 2*4=8
# .......
# 1*9=9 2*9=18 3*9=27..........9*9=81
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,'*',j,'=',i*j,end='')
#     print()

#      *
#     ***
#    *****
#   *******
#  *********
# ***********
# 空格：4 3 2 1 0 ：5=i
# for i in range(1,6):
#      for j in range(1,6-i):
#          print('',end='')
#      for k in range(1,2*1):
#          print('',end='')
#      print()
#1.4 break和continue语句
# 1.break语句：与if联合使用，强制退出循环
# 例题：1+2+3+.....+n<10000,计算n的最大值。
# s=0
# i=1
# while True:
#     s +=i
#     if s>10000:
#         break
#     i +=1
# print('n',i-1)
# 2.continue:结束某次循环
# 用continue输出50 以内的偶数。
# for i in range(1,51):
#     if i%2!=0:
#         continue
#     else:
#         print('i是偶数')
# if 3<4 and 3>2
#     print()



