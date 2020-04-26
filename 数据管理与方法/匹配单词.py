import re
b = 'site sea sue sweet see case sse ssee loses'
print('原字符串',b)
a = re.findall(r"\bs\S*?e\b",b)
print("结果为：",a)
