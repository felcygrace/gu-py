n=int(input())
sum1=1
while n>0:  
  a=n%10
  sum1=sum1*a
  n=n//10
print(sum1)
