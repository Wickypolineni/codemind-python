n1=int(input())
n2=int(input())
x=n2+1
k=[]
c=0
for i in range(n1,x):
    b=i
    while (i!=0):
        a=i%10
        if a==0:
            break
        elif b%a!=0: 
            break
        i=i//10
    else:
        k.append(b)
print(*k)
        
        
        
        