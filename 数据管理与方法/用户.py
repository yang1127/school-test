name = input("请输入您的姓名：")
gender = input("请输入您的性别：")
age = input("请输入您的年龄：")
# 通过字典设置参数
dic = {"name":name, "gender":gender, "age":age}
print("您的姓名是: {}, {}, 年龄{}岁".format(dic["name"], dic["gender"], dic["age"]))
