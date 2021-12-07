i=1
j=1000000
n=1
max=-1
while i<j:
    s=i
    while i!=1:
        if i%2==0:
            i=i//2
            n+=1
        else:
            i=3*i+1
            n+=1
    print(s,'    ',n)
    if n>max:
        max=n
        q=s
    n=1
    i=s+1
print(q,max)
    