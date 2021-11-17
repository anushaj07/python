a=input("enter some value")
b=a.split(",")
c=list(map(int,b))
d=[i for i in c if i%2!=0]
print(d)
