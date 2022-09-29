n=int(input())
d=0
temp=n
if n<0:
    n=n*(-1)
while  n:
    a=n%10
    n=n//10
    d=d*10+a
if temp<0:
    print(d*-1)
else:
    print(d)
