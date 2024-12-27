def sumofdigits(num):
    sum = 0
    if(num//10==0):
        return num
    else:
        while(num>0):
            rem = num % 10
            num = num//10
            sum = sum + rem
        return sum
print(sumofdigits(54321))

def sumofdigitrec(num):
    if(num//10==0):
        return num
    else:
        


