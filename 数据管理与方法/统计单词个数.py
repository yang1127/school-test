str = input("请输入字符串：")
count = 1
for i in str:
    if i == " ":
        count += 1;
print("单词个数:",count)
