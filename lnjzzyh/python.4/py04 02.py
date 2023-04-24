#1.find()方法：查找子串，找到返回最左段的索引值，找不到返回-1
# s='hello world'
##print(s.find('el),s.find('lo',3,6))
##print(s.find('ab'))
# 2.count()方法：统计子串在原始字符串中出现的次数
# s='bookLook'
# print(s.count('00',2,5))
# 3.split(分隔符)分割：分割字符串
# s='This is a python book'
# print(s.split())
# print(s.split(' ',3))
# s1='This-is-a-dog'
# print(s1.split('-'))
# 4.join()方法：以指定的字符连接字符串
# s='hello'
# print('*'.join(s))
# 5.replace()方法：用新的字符串替代原始的字符串
# s='MondayTuesday'
# print(s.replace('day','DAY'))
# print(s.replace('day','DAY',1))
# 6.strip()方法：删除字符串两端多余的字符。
# s='032 example345'
# print(s.strip('02345'))
#7.upper()--大写变小写
# s='ASDefg'
# print(s.upper(),s.lower())
#8.isalnum()--判断字符串中是否包含数字或字母
# 包含返回值为真，不包含返回值为假
# s='2008beijing'
# print(s.isalnum())
# 练习
s='abcdefg'
# (1)查找子串'bc'，输出对应索引
# print(s.find('bc'))
# (2)查找'abc'，输出返回值
# print(s.find('ade'))
# (3)统计'c'的出现次数
# print(s.count('c'))
# (4)替换'defg'为'abcd'，输出
# print(s.replace('defg','abcd'))
#4.4案例
# 注册验证程序
# 用户名：首字母下划线，长度3-30个字符
# username[0]!='_'
# Len(username)<3 or Len(username)>30
# 密码：长度6-16个字符,字母数字下划线组成
# Len(password)<6 or Len(password)>16
# passwd.find'_'!=1
# p=password.replace('_''1')
# p.isalnum--True
username=input('请输入用户名：:')
password=input('请输入密码：:')
if username[0]!='_':
    print('用户名不合法,必须以下划线开头')
elif len(username)<3 or len(username)>30:
    print('用户名长度不合法,必须在3-30之间')
elif len(password)<6 or len(password)>16:
    print('密码长度不合法,必须在6-16之间')
else:
    if password.find('_')!=-1:
        p=password.replace('_','1')
        if p.isalnum():
            print('Welcome,注册成功，用户名是{},密码是{}'.format(username,password))
        else:
            print('Error2001，注册失败')
#P65-2
test_str='02101 Hello python 10310'
test_str=test_str.strip('0123')
print(test_str)
#P65-3
s='i am a teacher'
s=s.replace('i','I')
print(s)
#P65-1
s=input('请输入单词：')
if s[0]=='M':
    print('Today is Monday')
elif s[0]=='W':
    print('Today is Wednesday')
elif s[0]=='F':
    print('Today is Friday')
elif s[0]=='T':
    if s[1]=='u':
        print('Today is Tuesday')
    else:print('Today is Thursday')
elif s[0]=='S':
    if s[1]=='a':
        print('Today is Saturday')
    else:
        print('Today is Sunday')
else:print('请输入正确的单词')

