n=int(input())
m=int(input())
if n>m:
  smallest=m
else:
  smallest=n
for i in range(1,smallest+1):
  if((m%i==0) and (n%i==0)):
    smallest=i
print(smallest)
