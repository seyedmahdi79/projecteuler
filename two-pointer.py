def two_pointer(my_list,number):
  i=0
  j=len(my_list)
  while i!=j:
        if my_list[i]+my_list[j-1]>number:
            j=j-1
        elif my_list[i]+my_list[j-1]==number:
            return True
        else:
            i=i+1 
  if i>=j:
      return False
            
            
my_list=[1,3,4,5,8,17]
number=int(input())
print(two_pointer(my_list,number))