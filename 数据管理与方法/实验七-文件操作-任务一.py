#开始读取
f = open("Py7-1.txt", "r")
print(f.read())
print("\n")
f.close()

#修改
f1 = open("Py7-1.txt", "r+")
#将指针置为第二处重复处
f1.seek(16,0)
f1.writelines("万里长征人未还")
#再将指针置回开始位置
f1.seek(0,0)
print(f1.read())
f1.close()

