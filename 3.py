
n=int(input())
i=2
while i<n:
    while n%i==0:
       n=n/i
    i=i+1
print(n)
