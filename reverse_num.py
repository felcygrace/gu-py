n=int(input())
c=0
while n>0:
  s=n%10
  c=c*10+s
  n=n//10
print(c)
