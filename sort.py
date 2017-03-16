from random import randint
from datetime import datetime

print str(datetime.now())
list1 = []
for i in xrange(100000):
    a = randint(-1000000,1000000)
    if a not in list1:
        list1.append(a)
print len(list1)
print str(datetime.now())