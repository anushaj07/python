def fac(n):
    fac_num =[]
    if n == 1:
        return 1
    else :
        fac_num.append(1)
        for i in range(1,n):
            fac_num.append(fac_num[i-1]*(i+1))
    return fac_num[-1]
n = fac(2)
print(n)
        #memmoriation