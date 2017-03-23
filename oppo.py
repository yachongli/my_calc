a = [1,2,32,32,3,4,5,3,4,5,8,0,83,4,80]

a_len = len(a)

while 1 <= a_len:
    for i in range(0,a_len-1):
        if a[i] > a[i+1] :
            a[i],a[i+1] = a[i+1],a[i]
    a_len-=1

print a
