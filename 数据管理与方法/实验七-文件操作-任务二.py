#导包
import xlwt

f = xlwt.Workbook(encoding='utf-8')

#创建一个sheet
sheet = f.add_sheet('grade')
          
grades = [
    {'id':"S09", '性别':"女", '成绩1':"89.2", '成绩2': "88.4", '成绩3':"86", '成绩4':"87.9"},
    {'id':"S10", '性别':"女", '成绩1':"90.5", '成绩2': "86.3", '成绩3':"87", '成绩4':"87.9"},
    {'id':"S11", '性别':"男", '成绩1':"88.7", '成绩2': "89.4", '成绩3':"89", '成绩4':"89.0"},
]

for row, grade in enumerate(grades):
    for col, key in enumerate(sorted([key for key in grade])):
        sheet.write(row, col, grade[key])

#保存Excel文件
f.save("./ex06.xlsx")

