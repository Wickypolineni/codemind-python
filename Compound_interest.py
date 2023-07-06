p, r, t = map(int, input().split())
a = (1 + (r / 100)) ** t
b = a * p
print("%.2f" %b)