
a = int(input())
sum1 = 0
for i in range(1, a):
    if(a % i == 0):
        sum1 = sum1 + i
if (sum1 == a):
    print("True")
else:
    print("False")