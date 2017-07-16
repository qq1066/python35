#!/usr/bin/env python3
# _*_ codeing: UTF-8 _*_
print("中文")
#python学习手册第四版
##第八章 列表和字典
###python3.0中的字典变化
####排序字典键
D = {'a':1, 'c':3, 'b':2}
Ks = D.keys()
print(sorted(Ks))
# for k in sorted(Ks, key=str.lower, reverse=True): print(k, D[k])
#for k in sorted(D): print(k, D[k])
my = {k: D[k] for k in sorted(D)}
print(D)
