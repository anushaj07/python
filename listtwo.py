a=input("enter some integer values")
b=input("enter some integer values")
c=a.split(" ")
d=list(map(int,c))
e=b.split(" ")
f=list(map(int,e))
print(d)
print(f)
len_a=len(d)
len_b=len(f)
flag=0
if len_a==len_b:
                print("list are of same length")
else :
            print("list are not of same length")
if sum(d)==sum(f):
                   print("sum are equal",sum(d))
else:
        print("sum are not equal:")
       
for i in range (len_a):
    for j in range(len_b):
                        if d[i]==f[j]:
                                        print(d[i],"occur in both")
                                        flag+=1
                       

if flag==0:
            print("no elements occur in both")
