def maxi(n):
    temp=n
    x=-1
    i=0
    while n:
        if n%10==6:
            x=i
        n=n//10
        i+=1
    if x!=-1:
        v=temp+(3*(10**x))
    return v
n = int(input())
if n==9999:
    print(9999)
else:
    m=maxi(n)
    print(m)