def find_max(L):

      if(len(L)==1):

            return L[0]

      else:

            rest=find_max(L[1:])

            return(L[0] if L[0]>rest else rest)
      
a = find_max([10,11,12,8,4])
print(a)