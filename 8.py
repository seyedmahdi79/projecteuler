# import math
# a=1 
# b=1 
# c=1
# while a+b+math.sqrt(a**2+b**2)!=1000 and  a**2+b**2!=c**2:
#     if 
import time
    
start=time.time()    
for i in range(2,500):
    for j in range(1,i):
        k=1000-i-j
        if  i**2+j**2==k**2:
            print("{}*{}*{}={}-------{}".format(i,j,k,i*j*k,time.time()-start))