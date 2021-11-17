a=input("enter some integer values")
b=a.split(" ")
print(b)
c=list(map(int,b))
print(c)
print(len(c))
leng=len(c)
for i in range (leng):
                    if c[i]>=100:
                                    c[i]='over'
                
                    
                                

print(c)
