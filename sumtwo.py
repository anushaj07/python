nums=[2,99,4,11,5,7]
target = 9

def sumtwo(l,t):
    ans =[]
    for i in range (0,len(l)):
        for j in range(i+1,len(l)):
            if l[i] + l[j] == t:
                ans.extend([(i,j)])
    return ans

print(sumtwo(nums,target))
            
        