n = int(input())
d = 0
for i in range(n):
    if i*(i+1)==n:
        d=1
        break
if d==1:
    print("YES")
else:
    print("NO")