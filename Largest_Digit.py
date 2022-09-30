n=int(input())
a=len(str(n))
b=0
for x in range(a):
    if(n%10>b):
        b=n%10
        n=n//10     
    else:
       n=n//10   
print(b)