def sumupton(n):
    sum1 = 0
    while(n>0):
        sum1 = sum1 + n
        n = n -1 
    return sum1
print(sumupton(5))

def sumn(n):
    a = 0
    if(n>0):
        a= n + sumn(n-1)
    return a
print(sumn(10))


