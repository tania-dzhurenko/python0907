print ('1 zavdanna:')
def chuslo (x):
    if (x%3==0) and (x%5==0):
        return ('Fuzz Buss')
    elif x%3==0:
        return ('Fuzz')
    elif x%5==0:
        return ('Buzz')
    else:
        return str(x)
print (chuslo (15))
print (chuslo (6))
print (chuslo (5))
print (chuslo (2))
print (type(chuslo (2)))

print ('2 zavdanna:')
def kvadrat(y):
    for i in range (2,y):
        if i%2==0:
            print (i*i)
kvadrat (10)

print ('3 zavdanna:')
l=[0, 1]
def zv (n):
    if n < len (l):
        return (l[n]**n)
    else:
        return -1
print (zv(0))

