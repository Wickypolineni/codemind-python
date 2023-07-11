t = int(input())
l = list(map(int, input().split()))
m = len(l) // 2
f = l[:m]
s = l[m:]
k = s[::-1]
a = k + f
print(*a)