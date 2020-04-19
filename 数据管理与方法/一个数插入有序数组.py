a = [10,23,35,46,57,68,79,80,92,103]
print("原始数组是：",a)
aa = int(input("请输入新数字："))
a.append(aa)
a.sort()
print("插入新数后的数组是：",a)
