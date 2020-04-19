x=input("请输入一个字符串：")
eng_num = 0
tal_num = 0
mat_num = 0
oth_num = 0
for y in x:
    if y.isalpha():
        eng_num += 1
    elif y.isspace():
        tal_num += 1
    elif y.isdigit():
        mat_num += 1
    else:
        oth_num += 1
print("英文字母:",eng_num ,"个，空格:",tal_num,"个，数字:",mat_num,"个，其他:",oth_num,"个")
