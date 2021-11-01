mark_1=int (input("enter mark_1 "))
mark_2=int (input("enter mark_2 "))
mark_3=int (input("enter mark_3 "))
total_mark=mark_3+ mark_2+ mark_1
percentage_mark=(total_mark/300)*100
if(percentage_mark>90):
                        print("percentage=",percentage_mark,"A grade")
elif(percentage_mark>80):
                        print("percentage=",percentage_mark,"B grade")
elif(percentage_mark>70):
                        print("percentage=",percentage_mark,"C grade")
elif(percentage_mark>60):
                        print("percentage=",percentage_mark,"D grade")
elif(percentage_mark>50):
                        print("percentage=",percentage_mark,"E grade")
else:
                        print("percentage=",percentage_mark,"fAil")
