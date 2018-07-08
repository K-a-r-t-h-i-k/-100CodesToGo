s=str(input())
l1=list(s)
l=list(map(int,l1))
ones={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
teens={1:"eleven",2:"twelve",3:"thirteen",4:"fourteen",5:"fifiteen",6:"sixteen",7:"seventeen",8:"eighteen",9:"nineteen"}
tens={1:"ten",2:"twenty",3:"thirty",4:"fourty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninty"}
a=[]
if(l[-2]==1 and l[-1]!=0):
    a.append(teens[l[-1]])
elif(l[-1]==0) :
    a.append(tens[l[-2]])
else:
    a.append(tens[l[-2]])
    a.append(ones[l[-1]])
a.insert(0,ones[l[-3]]+" hundred")
a.insert(0,ones[l[-4]]+" thousand")
print(" ".join(a))

