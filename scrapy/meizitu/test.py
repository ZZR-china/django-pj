# encoding=utf-8
# # -*- coding: utf-8 -*-

sc = '\u4e00\u7ec4\u8d85\u6e05\u7eaf\u7684\u5973\u5b69\uff0c\u770b\u7684\u6211\u90fd\u9189\u4e86'
print(sc)

s1 = sc.encode('utf-8')
print(s1)

s2 = s1.decode('utf-8')  
print(s2)