import math
i=1
n=0
q=''
b=[]
p=0
while True:
    s=(i*(i+1)//2)
    g=2
    while s!=1:
        if n!=0 and p!=g:
            b.append(n+1)
            n=0
        if s%g==0:
            s=s//g
            p=g
            n+=1
        else:
            g+=1
    b.append(n+1)
    if math.prod(b)>500:
        print((i*(i+1)//2))
        break
    b=[]
    q=''
    i+=1
    n=0
        
        
        