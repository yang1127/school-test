grade = int(input('请输入成绩:'))
if grade < 60:
    print('不及格')
elif 60 <= grade and grade < 70:
    print('及格')
elif 70<= grade and grade < 80:
    print('中')
elif 80 <= grade and grade < 90:
    print('良')
else: 
    print('优秀')
