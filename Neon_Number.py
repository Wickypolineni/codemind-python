n=int(input())
a=n*n
temp=0
while a>0:
    temp=temp+a%10
    a=a//10
if n==temp:
    print("Neon Number")
else:
    print ("Not Neon Number")