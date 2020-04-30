x = ["13915556234","13025621456","15325645124","15202362459"]
a = "456789"
b = "01289"
for i in x:
    if len(i) == 11 and i[:2] == '13' and i[2] in a:
        print(i,"是移动手机号码")
    elif len(i) == 11 and i[:2] == '15' and i[2] in b:
        print(i,"是移动手机号码")
    else:
        print(i,"不是移动手机号码")
