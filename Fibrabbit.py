def fibnoci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibnoci(n-1) + fibnoci(n-2)
a = fibnoci(5)
print(a)
#performance is bad 
L = [1,2,3,4,5]
