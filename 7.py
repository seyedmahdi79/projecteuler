my_list=[2]
x=3
while len(my_list)<100001:
    if all(x%i!=0  for i in my_list ):
       my_list.append(x)
    x=x+1
    
print(my_list[-1])
