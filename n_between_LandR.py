n=int(input())
l=int(input())
r=int(input())
a=0
for i in range(l,r+1):
  if i==n:
    a=True
if a==True:
  print("yes")
else:
  print("no")
