x=int(input())  
y=int(input())  
sum_x=0  
sum_y=0  
for i in range(1,x):  
    if x%i==0:  
        sum_x+=i  
for j in range(1,y):  
    if y%j==0:  
        sum_y+=j  
if(sum_x==y and sum_y==x):  
    print('Amicable')  
else:  
    print('Not Amicable')  