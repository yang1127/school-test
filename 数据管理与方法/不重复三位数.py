x = [1,2,3,4]
count = 0
for i in x:
    for j in x:
        for z in x:
            if i != j and i != z and j != z:
                print(str(i)+str(j)+str(z),end = "，")
                count += 1
            if count > 5:
                print(" ")
                count = 0
