a = int(input('输入三角形的边长a: '))
b = int(input('输入三角形的边长b: '))
c = int(input('输入三角形的边长c: '))

print('三角形三边分别为:a = %0.1f, b = %0.1f, c = %0.1f' %(a, b ,c))

# 计算半周长
s = (a + b + c) / 2
 
# 计算面积,使用海伦公式求解
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('三角形面积为 {}'.format(area))
