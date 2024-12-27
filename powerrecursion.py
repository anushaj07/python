def power (a,b):
    if (b == 0):
        return 1
    else :
        return a * power(a,b-1)
    
ans = power(5,4)
print(ans)