x = input("请输入一个五位数：")
if x[0:1] == x[4:5]:
    if x[1:2] == x[3:4]:
        print(x,"是一个回文数。")
else:
    print(x,"不是一个回文数。")
