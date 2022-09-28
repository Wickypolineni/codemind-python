def f(n):
    s=0
    for i in n:
        s+=int(i)
    return str(s)
n = input()
while len(n)!=1:
    n=f(n)
    
print(n)