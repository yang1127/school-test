for x in range(0,34):
    for y in range(0,51):
        for z in range(0,101):
            if x*3 + y*2 + z*0.5 == 100 and x + y + z == 100:
                print("大马有：",x,"匹，中马有：",y,"匹，小马有：",z,"匹")
                
