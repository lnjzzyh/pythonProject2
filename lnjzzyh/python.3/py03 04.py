#猜拳游戏
# 1 随机模块---random
# keyword---keyword.kwlist 关键字
# math---math.sqrt---开平方
# import random
# print(random.randint(0,2))
# 游戏规则---石头--0    剪刀-1 布-1
# player compu
# player=0
# compu=1
# import random
#
# player=int(input("请输入石头剪刀布"))
# compu=random.randint(0,2)
# if player<0 or player>2:
#     print("输入错误")
# elif (compu==0 and compu==1)or(player==1 and compu==2)or (player==2 and compu==2):
#     print("恭喜你，你赢了")
# elif player==compu:
#     print("平局")
# else:
#     print("电脑获胜")
# p50-2
# 输出2-200之间的素数：只能被1和它本身整除的数据。
# i=2
# while i<=200:
#     j=2
#     while j<i-1:
#         if i%j==0:
#             break
#         j+=1
#     else:
#         print(i,'是素数。')
#     i+=1
# p50-3 while---九九乘法表
# for i in range(1,10):
#      for j in range(1,i+1):
#          print(j,'*',i,'=',i*j,end='')
#       print()
i=1
while i<=9:
    j=1
    while j<=9:
        print(i,'*',j,'=',i*j,end='')
        j+=1
    print()
    i+=1         