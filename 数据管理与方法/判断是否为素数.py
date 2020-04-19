x = int(input("请输入一个正整数："))
if x < 2:
    print(x,"不是素数。")
else:
    for i in range(2,x):
        if x % i == 0:
            print(x,"不是素数。")
            break
    else:
        print(x,"是素数。")
        
