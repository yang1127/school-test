a = int(input("请输入一个三位数的正整数："))
# 百位 十位 个位
a1 = a // 100
a2 = a // 10 % 10
a3 = a % 10
sum = a1 * a1 * a1 + a2 * a2 * a2 + a3 * a3 * a3
print("各位数的立方和是:%d" %sum)
