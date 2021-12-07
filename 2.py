list1=[1,2]
number=int(input())
i=2
while list1[-1]<=number and list1[i-1]+list1[i-2]<number:
    list1.append(list1[i-1]+list1[i-2])
    i=i+1
print(list1)    
list1=[i  for i in list1 if i%2==0]
print(sum(list1))