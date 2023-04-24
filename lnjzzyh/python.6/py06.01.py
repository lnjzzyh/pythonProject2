#第六章 字典(dict)与集合(set)
#6.1 字典的创建与访问
# 1.字典定义：用大括号括起来的0组或多组键值对的无序序列。
# d1={}#空的字典
# d2={'num':'1001',
#     'name':'Mary',
#     'age':16
#     }
#键：'num','name','age'
#值：'1001','Mary','16'
# print(d2,type(d2))
#字典说明:
# (1)字典中的键只能是固定的数据类型(int,float,str,tuple)
#字典中键不能是可变的数据类型。(list,dict,set)
# 字典中的值可以是任意的数据类型。
#(2)字典中的键不允许重复，若重复后面的键值对覆盖前面的键值对。
# d={'a':1,'b':2,'a':3}
# print(d)
# 2.dict()函数定义字典
# d=dict(a=1,b=3,c=4)
# print(d)
#.dict.fromkeys()方法:所有键对应的值相同
# stu_info=dict.fromkeys(['A','B','C'],256)
# print(stu_info)
# 4.字典的访问
# d={'num':'1001',
#     'name':'Mary',
#     'age':16
#     }
# (1)通过键访问字典（确定字典中有被访问的键）
# print(d['num'],d['name'],d['age'])
# print(d['sex'])
#(2)使用get()方法访问字典(无论键是否存在可以用该方法)
# print(d.get('num'),d.get('age'))
# print(d.get('sex'))
# 字典中存在键即为修改，不存在键即为添加的值
# 6.2字典的操作方式
#2，删除字典中的值对
# （1）del 命令
# d={'num':'1001',
#    'name':'Mary',
#    'age':16
#    }
# del d['num']
#  print(d)
#(2)pop()方法：删除键值并获取值。
# s=d.pop('name')
# print(d,s)
# (3)popitem()方法：随机删除键值对，并以元组的形式获取键和值
# s=d.popitem()
# print(d,s)
# d.clear()
# print(d)
# 3.更新字典