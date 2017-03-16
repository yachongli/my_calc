#utf-coding:utf-8
import random
import datetime

#随机两个包含1万个元素的list
list1,list2 = [],[]
for x in range(10000):
    a = random.randint(-99999999999,99999999999)
    if a not in list1:
        list1.append(a)
for x in range(100000):
    a = random.randint(-99999999999,99999999999)
    if a not in list2 and a not in list1:
        list2.append(a)
print len(list1),len(list2)
#打印开始时间，这是第一种方法，采用传统的双循环的处理方法，10000^2就是一个亿啊

print "第一种方法\n",str(datetime.datetime.now())
min = float("inf")                           #设置min为无限大
for i in list1:                              #双循环开始
    for j in list2:
        # print abs(i-j)
        if abs(i-j) < min:
            min = abs(i-j)
print  min,"\n",str(datetime.datetime.now()),"\n"         #打印结束时间


#打印开始时间。第二种方法，我的方法，基本思路是双循环变单循环，两个10000就是20000
#使用python内建函数 ，无论在什么时候，python的内建函数绝对比你的方法快
print "第二种方法\n", str(datetime.datetime.now())
min = float("inf")
#两个list合并，去重，看看长度是否减小，如果有减小，就证明了一件事，两个list中有元素相同，这两个元素相减绝对等于0
list3 = list(set(list1+list2))
if len(list3) != len(list1+list2):
    min = 0
else:
    #将合并后的list排序
    list3.sort()
    for i in range(len(list3)-1):
        #已经排序了，我们只需要让后一个减前一个，然后再保证这两个数据原来不是在相同的list中即可
        if abs(list3[i+1]-list3[i]) <min and \
            (list3[i+1] in list1 or list3[i] in list1 )\
            and (list3[i+1] in list2 or list3[i] in list2):
            min = abs(list3[i+1]-list3[i])
print  min,"\n",str(datetime.datetime.now()),"\n"


