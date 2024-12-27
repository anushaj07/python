def coin_change(L,amount):
    denomination=[]
    i=0
    while(i < len(L)):
        a = int(amount / L[i])
        amount = amount - a *L[i]
        denomination.append(a)
        i +=1
    return denomination
L = [500,100,50,20,10,5,2,1]
den = coin_change(L,657)
print(den)