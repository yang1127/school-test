money = int(input('请输入工资:'))
# 税
tax1 = 0
tax2 = (money - 5000) * 0.03
tax3 = (money - 5000) * 0.1 - 2520
tax4 = (money - 5000) * 0.2 - 16920
# 应交税
if 0 < money and money <=5000:
    print('应交税款为:%d' %tax1)
elif 5000 <= money and money <=36000:
    print('应交税款为:%f' %tax2)
elif 36000 <= money and money <=144000:
    print('应交税款为:%f' %tax3)
else:
    print('应交税款为:%f' %tax4)
