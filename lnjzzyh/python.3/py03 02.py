#3.2循环语句
# 1.while循环
# 格式：
# while 条件：
#     循环体
# 例：循环输出5个'*'
# i=1
# while i<=5:
#     print('*')
#     i+=1
#2.参数end=''
# i=1
# while i<=5:
#     print('*',end='    ')
#     i+=1
# 3.for循环
# 格式：
# for 变量 in 序列（字符串，列表，元组）：
#     循环体
# x='******'
# for s in x:
#        print(s,end='')
# 4.range(start,stop,step)
# range(2,10,1)---------1,2,3,4,5,6,7,8,9
# range(0,21,2)---------0,2,4,,,,,,,,,20
# 用for循环计算1+2+3....+100的和。
s=0
for i in range(1,101,1):
    s+=i
print('s=',s)