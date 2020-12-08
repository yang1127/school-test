# # 基本数据类型
# # 1定义
# # 1.1 定义整型int变量
# age = 18 #本质 age = int(age)
# print(age)

# # 1.2 定义浮点型float
# salary = 3000.3
# print(type(salary))
# print(salary)

# # 2 数据类型转换
# s = '123'
# res = float(s)
# print(type(s))
# print(s)
# print(type(res))
# print(res)

# # 定义 "" '' """"""
# name1 = "张三"  #本质 name = str("张三")
# name2 = '李四'  #本质 name = str('李四')
# name3 = """王五""" #本质 name = str("""王五""")
# print(name1)
# print(name2)
# print(name3)

# 类型转换 str()可以将任意数据类型抓换为字符串类型
# str = 'hello python!'
# 1.1 按照索引取值（正向、反向）
#print(str[13]) # 越界
# print(str[12]) # ! 正向
# print(str[-1]) # ! 反向
# 1.2 切片-截取[起始下标:长度]
# print(str[0:5]) # hello
# print(str[0:5:2]) # hlo 间隔一位跳着取索引
# print(str[::-1]) # !nohtyp olleh 反向切片取值
# 1.3 长度
# print(len(str)) # 13 无'\0'
# 1.4 成员运算 in 和 not in
# print('hello' in str) # Ture
# print('world' in str) #Flase
# print('world' not in str) #True
# 1.5 移除

# 1.6 切割 split
# str3 = '127.0.0.1'
# print(str3.split('.')) # ['127', '0', '0', '1']
# 1.7 循环
# str4 = '西安财经大学信息学院软件工程'
# for key in str4:
#     print(key)
# 西
# 安
# 财
# 经
# 大
# 学
# 信
# 息
# 学
# 院
# 软
# 件
# 工
# 程
# 1.8 其他操作

# format
# name = '李四'
# str5 = 'name is {name}'.format(name=name)
# str6 = 'name is {}'.format(name)
# print(str5) # name is 李四
# print(str6) # name is 李四

# 格式化输出
# name = '张三'
# age = 18
# print('我叫%s，今年%d岁' %(name,age)) # 我叫张三，今年18岁

# 输出
# name = input('请输入你的名字：')
# age = input('请输入你的年龄：')
# print(name,age)

#练习题1
# name = input('请输入你的名字：')
# age = input('请输入你的年龄：')
# # str1 = '我叫{}'.format(name)
# # str2 = ',年龄{}岁'.format(age)
# # print(str1,str2)
#
# # print('我叫{name}，今年{age}岁' .format(name = name, age = age))
# print('我叫{}，今年{}岁' .format(name, age))


#range()只能从小到大
# 1-100能被5整除的数
# for i in range(1, 101):
#     if i % 5 == 0:
#         print(i)

# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%s*%s=%s' %(j, i, i * j), end = ' ')
#     print()

# *
# * *
# * * *
# * * * *
# for i in range(1, 5):
#     for j in range(i): #for j in range(1, i + 1):
#         print('* ', end = '') #end = ''不换行
#     print() #换行

#    *     1 3 1
#   ***    2 2 3
#  *****   3 1 5
# *******  4 0 7
# for i in range(1, 5):
#     for k in range(4 -i): #空格
#         print(' ', end = '')
#
#     for j in range(2 * i - 1):
#         print('*', end = '') #end = ''不换行
#     print() #换行

#    *    1 3 1
#   * *   2 2 2
#  *   *  3 1 2
# ******* 4 0 7

# for i in range(1, 5):
#     for k in range(4 -i):
#         print(' ', end = '')
#     for j in range(2 * i - 1):
#         if i == 1 or i == 4:
#             print('*', end = '')
#         elif j == 0 or j == 2 * i - 2:
#             print('*', end = '')
#         else:
#             print(' ', end = '')
#     print() #换行

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# for i in range(1, 5):
#     for k in range(4 -i): #空格
#         print(' ', end = '')
#
#     for j in range(2 * i - 1):
#         print('*', end = '') #end = ''不换行
#     print() #换行
# # for i in range(3, 0, -1):  #再打印一边
# #     for k in range(4 -i): #空格
# #         print(' ', end = '')
# #
# #     for j in range(2 * i - 1):
# #         print('*', end = '') #end = ''不换行
# #     print() #换行
# for i in range(1, 4):  #再打印一边
#     for k in range(i): #空格
#         print(' ', end = '')
#
#     for j in range(2 * (4 - i) - 1):
#         print('*', end = '') #end = ''不换行
#     print() #换行

#空心菱形
#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *
# num = 4
# for i in range(-num, num):
#     for j in range(-num, num):
#         if abs(i) + abs(j) == num - 1:
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()

#列表
# list = [1, 2, 3, 4, 5]
#赋值
# list[0] = 6
#遍历
# print(list[0]) #6 #列表支持修改数据
# print(list[0:3:2]) #[6, 3] 取下标从0-3步长为2的值
# print(list[4::-1]) #反向打印 #print(list[::-1])
#删除
# del list[0]
# print(list[0]) #2
#长度
# print(len(list)) #5
#组合
# list1 = [6]
# list2 = list + list1
# print(list2) #[1, 2, 3, 4, 5, 6]
#查
# print(10 in list) #False
#增加元素
# list.append(6)
# print(list) #[1, 2, 3, 4, 5, 6]
#一个元素出现的次数
# print(list.count(3)) #1
#元素所在位置
# print(list.index(3)) #2
#插入
# list.insert(1,2)
# print(list) #[1, 2, 2, 3, 4, 5]
#移除第一个出现的位置
# list.remove(3)
# # print(list) #[1, 2, 4, 5]
#反转reverse
# list.reverse()
# print(list) #[5, 4, 3, 2, 1]

#冒泡排序
# list = [1, 5, 2, 4, 3]
# length = len(list)
# for i in range(0, length - 1):
#     for j in range(0, length - 1 - i):
#         if list[j] > list[j + 1]:
#             list[j], list[j + 1] = list[j + 1], list[j]
# print(list)
