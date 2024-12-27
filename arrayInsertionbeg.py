def insert_beg(arr, n, item):
    if( n != max):
       i=n-1
       while(i>=0):
          arr[i+1]=arr[i]
          i-=1
       arr[i+1]=item
       print(arr)
    else:
       print('Overflow')

ann = [10,11,12,13]
n = 4 
ite = 9
print(insert_beg(ann,3,ite))

def del_beg(arr,n):
   if(n != 0):
      i = 1
      while(i<=n-1):
        arr[i-1] = arr[i]
        i+=1
      print(arr)
   else:
      print("Under flow")
      
print(del_beg(ann,3))
    

      