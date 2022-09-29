n = int(input())  
n_o_d = len(str(n)) 
temp = n**2  
l_d = temp%pow(10,n_o_d) 
if l_d == n:  
  print("Automorphic Number")  
else:  
  print("Not an Automorphic Number")  