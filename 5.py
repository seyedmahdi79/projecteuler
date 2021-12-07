g=9699690
i=0
flag=0
s=1
while i==0:
    for j in range(11,21):
        if g%j!=0:
            flag=1
            break
    print(g)
    if flag==0:
        i=g
    g=g+9699690
    flag=0
print(i)