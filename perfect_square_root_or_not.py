import math
n=int(input())
def ps(n):
	if n>=0:
		sr=int(math.sqrt(n))
		return ((sr*sr) == n)
	return false
if (ps(n)):
	print("True")
else:
	print("False")
